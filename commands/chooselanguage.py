from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from l10n import l10n
from misc import Message


async def command_chooselanguage(message: Message, func=None) -> None:
    await choose_language(message, func)


async def choose_language(message: Message, func=None):
    keyboard = [
        [InlineKeyboardButton("Русский", callback_data="ru_RU")],
        [InlineKeyboardButton("English", callback_data="en_US")]
    ]

    await message.reply_text("Выберите язык.\n\nChoose preferred language.",
                             reply_markup=InlineKeyboardMarkup(keyboard))
    message.user.wait_for_reply("chooselanguage", None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        if reply.text not in ["ru_RU", "en_US"]:
            await reply.reply_text("Язык не найден. Выберите другой.\n\nLanguage not found. Choose another.")
            reply.user.wait_for_reply("chooselanguage", None, lambda reply: handle_reply(reply))
            return

        user = reply.user
        user.write_language_to_db(reply.text)
        user.lang = reply.text

        await message.reply_text(l10n("chooselanguage.youll_be_able_to_change_language_later", user.lang))
        if func is not None:
            await func
