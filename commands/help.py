from l10n import l10n
from misc import Message


async def command_help(message: Message) -> None:
    await message.reply_text(l10n("help.message", message.lang))