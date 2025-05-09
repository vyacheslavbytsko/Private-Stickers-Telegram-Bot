from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from commands.addsticker import choose_stickerpack
from l10n import l10n
from misc import Message


async def command_usersentsticker(message: Message) -> None:
    if message.tgmessage.sticker is None:
        await message.reply_text(l10n("usersentsticker.internal", message.lang))
        return

    keyboard = [
        [InlineKeyboardButton(l10n("usersentsticker.i_want_to_add_sticker", message.lang), callback_data="addsticker")],
        [InlineKeyboardButton(l10n("usersentsticker.i_want_to_cancel", message.lang), callback_data="/cancel")]
    ]

    await message.reply_text(l10n("usersentsticker.what_you_want_to_do", message.lang),
                             reply_markup=InlineKeyboardMarkup(keyboard))
    message.user.wait_for_reply("usersentsticker", None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        allowed_answers = ["addsticker"]
        if reply.text not in allowed_answers:
            await reply.reply_text(l10n("usersentsticker.you_typed_that_message_incorrectly", reply.lang))
            return

        # sticker is here already
        match reply.text:
            case "addsticker":
                await choose_stickerpack(message, pre_sent_sticker=message.tgmessage.sticker)