import asyncio
import importlib
import logging
import os

import misc
from classes import stickerpackinvite as stickerpackinvite_module, user as user_module, sticker as sticker_module, \
    stickerpack as stickerpack_module
from classes.stickerpack import Stickerpack
from classes.user import User, pop_users

from l10n import l10n
from misc import Message, stringify

from telegram import Update, InlineQueryResultCachedSticker, InputTextMessageContent
from telegram.ext import Application, ContextTypes, InlineQueryHandler, MessageHandler, filters, CallbackQueryHandler


class Command:
    def __init__(self, name: str) -> None:
        self.name = name
        self.modul = importlib.import_module(f"commands.{name}")
        self.func = getattr(self.modul, f"command_{name}")


commands_filenames = list(filter(lambda filename: filename.endswith(".py"), os.listdir("commands")))
commands = [Command(command_filename.removesuffix(".py")) for command_filename in commands_filenames]


def command_by_name(name: str) -> Command | None:
    for command in commands:
        if command.name == name:
            return command
    return None


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("apscheduler.executors.default").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


async def manage_text_messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text, user, message = misc.three_bogatyrs(update)

    if text is not None:
        if text.startswith("/"):
            logger.info(
                f"Command: {(update.message or update.callback_query).from_user.full_name} ({user.id}) - {text}")

    if text == "/cancel":
        await command_by_name("cancel").func(Message(update, context))
        return

    if user.id in list(misc.waiting_for_reply.keys()):
        if text is not None:
            if text.startswith("/"):
                finishable = (misc.waiting_for_reply[user.id][1] or {}).get("finishable", False)
                if not (finishable and text == "/finish"):
                    await message.reply_text(l10n("general.dont_send_another_command_while_in_action", user.lang,
                                                  [f"/{misc.waiting_for_reply[user.id][0]}"]))
                    return
                # else pass /finish to the reply handler
        func = misc.waiting_for_reply[user.id][2](Message(update, context))
        del misc.waiting_for_reply[user.id]
        await func
        return

    if user.lang is None:
        await command_by_name("chooselanguage").func(Message(update, context), manage_text_messages(update, context))
        return

    if text is None:
        if message.sticker is not None:
            await command_by_name("usersentsticker").func(Message(update, context))
        elif message.photo is not None and len(message.photo) > 0:
            await command_by_name("usersentphoto").func(Message(update, context))
        elif message.video is not None:
            await command_by_name("usersentvideo").func(Message(update, context))
        elif message.animation is not None:
            await command_by_name("usersentanimation").func(Message(update, context))
        else:
            await message.reply_text(l10n("general.didnt_understand_ya", user.lang))
        return

    command = command_by_name(text[1:])
    if command is not None and text[0] == "/":
        await command.func(Message(update, context))
    else:
        await message.reply_text(l10n("general.didnt_understand_ya", user.lang))


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    user = User(query.from_user.id).get_user()

    if user.id in misc.waiting_for_reply.keys():
        #
        await query.edit_message_text(l10n("general.good", user.lang))
        await manage_text_messages(update, context)
        await query.answer()


async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.inline_query.query
    user = User(update.inline_query.from_user.id).get_user()

    logger.info(
        f"Inline Query: {update.inline_query.from_user.full_name} ({user.id}) - {user.get_added_stickerpacks_ids()}")

    stickerpacks = [await Stickerpack(stickerpack_id).init_from_db() for stickerpack_id in
                    user.get_added_stickerpacks_ids()]
    stickers = [sticker for stickerpack in stickerpacks for sticker in stickerpack.stickers]

    textual_representation = False
    try:
        if misc.waiting_for_reply[user.id][1]["sticker_textual_representation"]:
            textual_representation = True
    except:
        pass

    results = [
        InlineQueryResultCachedSticker(
            id=sticker.id,
            sticker_file_id=sticker.file_id,
            input_message_content=InputTextMessageContent(
                sticker.id) if textual_representation else None
        ) for sticker in stickers if (query != "" and
                                      stringify([
                                          (await Stickerpack(sticker.from_stickerpack_id).init_from_db()).name,
                                          *sticker.keywords,
                                          sticker.id
                                      ]).lower().count(query.lower())) or query == ""
    ]

    await update.inline_query.answer(results, auto_pagination=True, cache_time=10, is_personal=True)


def start_bot() -> None:
    application = Application.builder().token(open("/app/data/token.txt").readline().strip()).build()

    application.add_handler(MessageHandler(filters.TEXT | filters.ATTACHMENT, manage_text_messages))
    application.add_handler(InlineQueryHandler(inline_query))
    application.add_handler(CallbackQueryHandler(button))

    user_module.create_db()
    sticker_module.create_db()
    stickerpack_module.create_db()
    stickerpackinvite_module.create_db()
    misc.db.commit()

    async def check_media_made(context: ContextTypes.DEFAULT_TYPE) -> None:
        while not misc.media_made.empty():
            await misc.media_made.get()()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        loop.run_until_complete(application.initialize())
        if application.post_init:
            loop.run_until_complete(application.post_init(application))
        loop.run_until_complete(application.updater.start_polling(allowed_updates=Update.ALL_TYPES))
        loop.run_until_complete(application.start())
        application.job_queue.run_repeating(pop_users, 60 * 10)
        application.job_queue.run_repeating(check_media_made, 1)
        loop.run_forever()
    except (KeyboardInterrupt, SystemExit):
        logger.debug("Application received stop signal. Shutting down.")
        try:
            loop.run_until_complete(application.job_queue.stop())
            if application.updater.running:
                loop.run_until_complete(application.updater.stop())
            if application.running:
                loop.run_until_complete(application.stop())
            if application.post_stop:
                loop.run_until_complete(application.post_stop(application))
            loop.run_until_complete(application.shutdown())
            if application.post_shutdown:
                loop.run_until_complete(application.post_shutdown(application))
        finally:
            loop.close()
            misc.db.commit()
            misc.db.close()


if __name__ == "__main__":
    start_bot()