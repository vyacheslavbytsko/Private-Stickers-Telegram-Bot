from l10n import l10n
from misc import Message


async def command_feedback(message: Message) -> None:
    await message.reply_text(l10n("feedback.message", message.lang))
