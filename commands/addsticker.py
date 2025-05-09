import traceback
from uuid import uuid4

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputSticker

import misc
from classes.sticker import Sticker
from classes.stickerpack import Stickerpack
from commands import choosepack
from l10n import l10n
from misc import Message


async def command_addsticker(message: Message) -> None:
    await choose_stickerpack(message)


async def choose_stickerpack(message: Message, pre_sent_sticker: telegram.Sticker = None) -> None:
    await (choosepack.choose_stickerpack(
        message,
        "addsticker",
        "addsticker.choose_stickerpack",
        True,
        lambda stickerpack: send_sticker(message, stickerpack, pre_sent_sticker),
        True,
        lambda: choose_stickerpack(message, pre_sent_sticker)
    ))


async def send_sticker(message: Message, stickerpack: Stickerpack, pre_sent_sticker: telegram.Sticker = None) -> None:
    if pre_sent_sticker is not None:
        await choose_privacy(message, stickerpack, pre_sent_sticker)
        return

    await message.reply_text(l10n("addsticker.send_the_sticker", message.lang))
    message.user.wait_for_reply("addsticker", None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        if reply.tgmessage.sticker is not None:
            sticker = reply.tgmessage.sticker
            await choose_privacy(message, stickerpack, sticker)
        elif reply.tgmessage.photo is not None and len(reply.tgmessage.photo) > 0:
            await misc.photo2sticker(reply.user, reply.tgmessage,
                                     lambda sticker: choose_privacy(message, stickerpack, sticker))
        elif reply.tgmessage.video is not None:
            await misc.video2sticker(reply.user, reply.tgmessage,
                                     lambda sticker: choose_privacy(message, stickerpack, sticker))
        elif reply.tgmessage.animation is not None:
            await misc.animation2sticker(reply.user, reply.tgmessage,
                                     lambda sticker: choose_privacy(message, stickerpack, sticker))
        elif reply.tgmessage.document is not None:
            # TODO: l10n
            await message.reply_text("Converting files to stickers is in development.")
            return
        else:
            await message.reply_text(l10n("addsticker.no_send_sticker", reply.lang))
            message.user.wait_for_reply("addsticker", None, lambda reply: handle_reply(reply))
            return


async def choose_privacy(message: Message, stickerpack: Stickerpack, tgsticker: telegram.Sticker):
    if tgsticker.set_name is None or tgsticker.set_name.endswith(f"_by_{misc.botname}"):
        await message.reply_text(l10n("addsticker.this_sticker_is_private", message.lang))
        await send_keywords(message, stickerpack, tgsticker, [])
    else:
        keyboard = [[
            InlineKeyboardButton(l10n("addsticker.yes", message.lang), callback_data="yes"),
            InlineKeyboardButton(l10n("addsticker.no", message.lang), callback_data="no")
        ]]
        await message.reply_text(l10n("addsticker.this_sticker_is_public", message.lang),
                                 reply_markup=InlineKeyboardMarkup(keyboard))
        message.user.wait_for_reply("addsticker", None,
                                    lambda reply: handle_reply(reply, tgsticker))

        async def handle_reply(reply: Message, tgsticker: telegram.Sticker):
            if reply.text == "yes":
                try:
                    sticker_format = "animated" if tgsticker.is_animated else "video" if tgsticker.is_video else "static"
                    internal_telegram_stickerpack_id = "set_" + str(uuid4())[:10].replace("-", "") + "_by_" + misc.botname
                    public_sticker_bytes = bytes(await(
                        await reply.tgmessage.get_bot().get_file(tgsticker.file_id)).download_as_bytearray())

                    match sticker_format:
                        case "video" | "animated":
                            try:
                                await reply.tgmessage.get_bot().delete_sticker_set(internal_telegram_stickerpack_id)
                            except Exception:
                                pass
                            try:
                                await reply.tgmessage.get_bot().create_new_sticker_set(reply.user.id,
                                                                                       internal_telegram_stickerpack_id,
                                                                                       misc.stickerset_created_by_bot, [
                                                                                           InputSticker(
                                                                                               public_sticker_bytes,
                                                                                               tgsticker.emoji,
                                                                                               sticker_format
                                                                                           )
                                                                                       ])
                            except telegram.error.BadRequest as e:
                                if e.message == "Can't parse input sticker: expected a unicode emoji":
                                    await reply.tgmessage.get_bot().create_new_sticker_set(reply.user.id,
                                                                                           internal_telegram_stickerpack_id,
                                                                                           misc.stickerset_created_by_bot,
                                                                                           [
                                                                                               InputSticker(
                                                                                                   public_sticker_bytes,
                                                                                                   ['🙂'],
                                                                                                   sticker_format
                                                                                               )
                                                                                           ])
                                else:
                                    raise e

                            private_sticker_id = (await reply.tgmessage.get_bot().get_sticker_set(internal_telegram_stickerpack_id)).stickers[0].file_id

                            try:
                                await reply.tgmessage.get_bot().delete_sticker_set(internal_telegram_stickerpack_id)
                            except Exception:
                                await reply.tgmessage.get_bot().delete_sticker_from_set(private_sticker_id)

                            await reply.reply_text(l10n("addsticker.your_private_sticker", reply.lang))
                            tgsticker = (await reply.tgmessage.reply_sticker(private_sticker_id)).sticker
                        case "static":
                            await message.reply_text(l10n("addsticker.your_private_sticker", reply.lang))
                            tgsticker = (
                                await message.tgmessage.reply_sticker(public_sticker_bytes, tgsticker.emoji)).sticker

                except telegram.error.BadRequest:
                    print(traceback.format_exc())
                    await message.reply_text(l10n("inputsticker"
                                                  ".there_was_an_exception",
                                                  reply.lang))
                    reply.user.wait_for_reply("addsticker", None,
                                              lambda reply: handle_reply(reply, tgsticker))
                    return
            elif reply.text == "no":
                pass
            else:
                await message.reply_text(l10n("addsticker.privacy_choose_only_yes_or_no", reply.lang))
                reply.user.wait_for_reply("addsticker", None,
                                          lambda reply: handle_reply(reply, tgsticker))
                return

            await send_keywords(message, stickerpack, tgsticker, [])


async def send_keywords(message: Message, stickerpack: Stickerpack, tgsticker: telegram.Sticker, keywords: list = None):
    if keywords is None:
        keywords = []
    await message.reply_text(l10n("addsticker.send_keywords", message.lang))
    message.user.wait_for_reply("addsticker", {"finishable": True},
                                lambda reply: handle_reply(reply, stickerpack))

    async def handle_reply(reply: Message, stickerpack: Stickerpack):
        if reply.text is None:
            await reply.reply_text(l10n("addsticker.no_send_keywords", reply.lang))
            reply.user.wait_for_reply("addsticker", {"finishable": True},
                                      lambda reply: handle_reply(reply, stickerpack))
            return

        if reply.text != "/finish":
            keywords.append(reply.text)
            await reply.reply_text(l10n("addsticker.send_more_keywords", reply.lang))
            reply.user.wait_for_reply("addsticker", {"finishable": True},
                                      lambda reply: handle_reply(reply, stickerpack))
            return

        await choose_position(message, stickerpack, tgsticker, keywords)


async def choose_position(message: Message, stickerpack: Stickerpack, tgsticker: telegram.Sticker, keywords: list):
    if len(stickerpack.stickers) == 0:
        await input_sticker(message, stickerpack, tgsticker, keywords, 1)
        return

    keyboard = [[
        InlineKeyboardButton(l10n("addsticker.start_position", message.lang), callback_data="1"),
        InlineKeyboardButton(l10n("addsticker.end_position", message.lang), callback_data=str(len(stickerpack.stickers) + 1))
    ]]

    await message.reply_text(
        l10n("addsticker.send_position_of_sticker_to_insert", message.lang, [str(len(stickerpack.stickers) + 1)]),
        reply_markup=InlineKeyboardMarkup(keyboard))
    message.user.wait_for_reply("addsticker", None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        if not misc.is_int(reply.text):
            await reply.reply_text(l10n("addsticker.write_a_number", reply.lang), reply_markup=InlineKeyboardMarkup(keyboard))
            reply.user.wait_for_reply("addsticker", None, lambda reply: handle_reply(reply))
            return

        position = int(reply.text)
        if position < 1 or position > len(stickerpack.stickers) + 1:
            await reply.reply_text(
                l10n("addsticker.write_a_number_from_sth_to_sth", reply.lang, [1, str(len(stickerpack.stickers) + 1)]), reply_markup=InlineKeyboardMarkup(keyboard))
            reply.user.wait_for_reply("addsticker", None, lambda reply: handle_reply(reply))
            return

        await input_sticker(message, stickerpack, tgsticker, keywords, int(reply.text))


async def input_sticker(message: Message, stickerpack: Stickerpack, tgsticker: telegram.Sticker, keywords: list, insert_position: int = 0):
    sticker = Sticker(str(uuid4()), tgsticker.file_id, stickerpack.id,
                      keywords)
    sticker.save_changes_to_db(new_sticker=True)

    stickerpack.stickers.insert(insert_position - 1, sticker)

    stickerpack.save_changes_to_db()

    await message.reply_text(l10n("addsticker.done_adding_sticker", message.lang, [misc.botname]))
