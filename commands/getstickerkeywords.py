from classes.sticker import Sticker
from commands import choosesticker
from l10n import l10n
from misc import Message


async def command_getstickerkeywords(message: Message) -> None:
    await choosesticker.choose_sticker(message, "getstickerkeywords", False, lambda sticker: show_keywords(message, sticker))


async def show_keywords(message: Message, sticker: Sticker):
    await message.reply_text(l10n("getstickerkeywords.keywords_of_sticker_are", message.lang, [", ".join(sticker.keywords)]))
