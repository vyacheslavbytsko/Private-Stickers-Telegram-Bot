import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import misc
from commands.addsticker import choose_stickerpack
from l10n import l10n
from misc import Message


async def command_usersentanimation(message: Message) -> None:
    if message.tgmessage.animation is None:
        await message.reply_text(l10n("usersentanimation.internal", message.lang))
        return

    keyboard = [
        [InlineKeyboardButton(l10n("usersentanimation.i_want_to_convert_animation", message.lang), callback_data="convertanimation")],
        [InlineKeyboardButton(l10n("usersentanimation.i_want_to_add_animation", message.lang), callback_data="addanimation")],
        [InlineKeyboardButton(l10n("usersentanimation.i_want_to_cancel", message.lang), callback_data="/cancel")]
    ]

    await message.reply_text(l10n("usersentanimation.what_you_want_to_do", message.lang),
                             reply_markup=InlineKeyboardMarkup(keyboard))
    message.user.wait_for_reply("usersentanimation", None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        allowed_answers = ["convertanimation", "addanimation"]
        if reply.text not in allowed_answers:
            await reply.reply_text(l10n("usersentanimation.you_typed_that_message_incorrectly", reply.lang))
            return

        await misc.animation2sticker(reply.user, message.tgmessage, lambda tgsticker: got_sticker(tgsticker))

        async def got_sticker(tgsticker: telegram.Sticker):
            match reply.text:
                case "convertanimation":
                    pass
                case "addanimation":
                    await choose_stickerpack(message, pre_sent_sticker=tgsticker)