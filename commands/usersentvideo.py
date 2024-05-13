import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import misc
from commands.addsticker import choose_stickerpack
from l10n import l10n
from misc import Message


async def command_usersentvideo(message: Message) -> None:
    if message.tgmessage.video is None:
        await message.reply_text(l10n("usersentvideo.internal", message.lang))
        return

    keyboard = [
        [InlineKeyboardButton(l10n("usersentvideo.i_want_to_convert_video", message.lang), callback_data="convertvideo")],
        [InlineKeyboardButton(l10n("usersentvideo.i_want_to_add_video", message.lang), callback_data="addvideo")],
        [InlineKeyboardButton(l10n("usersentvideo.i_want_to_cancel", message.lang), callback_data="/cancel")]
    ]

    await message.reply_text(l10n("usersentvideo.what_you_want_to_do", message.lang),
                             reply_markup=InlineKeyboardMarkup(keyboard))
    message.user.wait_for_reply("usersentvideo", None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        allowed_answers = ["convertvideo", "addvideo"]
        if reply.text not in allowed_answers:
            await reply.reply_text(l10n("usersentvideo.you_typed_that_message_incorrectly", reply.lang))
            return

        await misc.video2sticker(reply.user, message.tgmessage, lambda tgsticker: got_sticker(tgsticker))

        async def got_sticker(tgsticker: telegram.Sticker):
            match reply.text:
                case "convertvideo":
                    pass
                case "addvideo":
                    await choose_stickerpack(message, pre_sent_sticker=tgsticker)