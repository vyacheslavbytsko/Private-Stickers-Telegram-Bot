import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import misc
from commands.addsticker import choose_stickerpack
from l10n import l10n
from misc import Message


async def command_usersentphoto(message: Message) -> None:
    if message.tgmessage.photo is None or len(message.tgmessage.photo) == 0:
        await message.reply_text(l10n("usersentphoto.internal", message.lang))
        return

    keyboard = [
        [InlineKeyboardButton(l10n("usersentphoto.i_want_to_convert_photo", message.lang),
                              callback_data="convertphoto")],
        [InlineKeyboardButton(l10n("usersentphoto.i_want_to_add_photo", message.lang), callback_data="addphoto")],
        [InlineKeyboardButton(l10n("usersentphoto.i_want_to_cancel", message.lang), callback_data="/cancel")]
    ]

    await message.reply_text(l10n("usersentphoto.what_you_want_to_do", message.lang),
                             reply_markup=InlineKeyboardMarkup(keyboard))
    message.user.wait_for_reply("usersentphoto", None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        allowed_answers = ["convertphoto", "addphoto"]
        if reply.text not in allowed_answers:
            await reply.reply_text(l10n("usersentphoto.you_typed_that_message_incorrectly", reply.lang))
            return

        await misc.photo2sticker(reply.user, message.tgmessage, lambda tgsticker: got_sticker(tgsticker))

        async def got_sticker(tgsticker: telegram.Sticker):
            match reply.text:
                case "convertphoto":
                    pass
                case "addphoto":
                    await choose_stickerpack(message, pre_sent_sticker=tgsticker)
