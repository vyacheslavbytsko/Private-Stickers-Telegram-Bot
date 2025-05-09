from l10n import l10n
from misc import Message


async def command_finish(message: Message) -> None:
    # because this function is only called when no pending actions are here
    # (it's the architecture of code), just say that person doesn't have any pending actions.
    await message.reply_text(l10n("finish.you_dont_have_pending_actions", message.lang))