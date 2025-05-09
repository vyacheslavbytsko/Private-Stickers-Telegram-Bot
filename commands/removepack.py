import telegram

from classes.stickerpack import Stickerpack
from commands import choosepack
from l10n import l10n
from misc import Message


async def command_removepack(message: Message) -> None:
    await choosepack.choose_stickerpack(message, "removepack", "removepack.choose_stickerpack", False, lambda stickerpack: remove_stickerpack(message, stickerpack))


async def remove_stickerpack(message: Message, stickerpack: Stickerpack):
    if message.user == stickerpack.owner:
        await message.reply_text(l10n("removepack.by_the_way_you_are_the_owner", message.lang))

    await message.reply_text(l10n("removepack.this_action_is_irreversible", message.lang), parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)
    message.user.wait_for_reply("removepack", None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        if reply.text != l10n("removepack.i_am_totally_sure", reply.lang):
            await message.reply_text(l10n("removepack.you_typed_that_message_incorrectly", reply.lang))
            return

        stickerpacks_ids = reply.user.get_added_stickerpacks_ids()
        stickerpacks_ids.remove(stickerpack.id)
        reply.user.set_stickerpacks_ids(stickerpacks_ids)

        await message.reply_text(l10n("removepack.stickerpack_was_removed", reply.lang))