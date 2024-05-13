import misc
from l10n import l10n
from misc import Message


async def command_cancel(message: Message) -> None:
    if message.user.id in misc.waiting_for_reply.keys():
        misc.waiting_for_reply.pop(message.user.id)
        await message.reply_text(l10n("cancel.action_is_cancelled", message.lang))
    else:
        await message.reply_text(l10n("cancel.you_dont_have_pending_actions", message.lang))