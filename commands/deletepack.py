import telegram

from classes.stickerpack import Stickerpack
from classes.user import User
from commands import choosepack
from l10n import l10n
from misc import Message


async def command_deletepack(message: Message) -> None:
    await choose_stickerpack(message)


async def choose_stickerpack(message: Message):
    await choosepack.choose_stickerpack(message, "deletepack", "deletepack.choose_stickerpack",
                                        True, lambda stickerpack: delete_stickerpack(message, stickerpack))


async def delete_stickerpack(message: Message, stickerpack: Stickerpack):
    await message.reply_text(l10n("deletepack.this_action_is_irreversible", message.lang), parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)
    message.user.wait_for_reply("deletepack", None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        if reply.text != l10n("deletepack.i_am_totally_sure", reply.lang):
            await reply.reply_text(l10n("deletepack.you_typed_that_message_incorrectly", reply.lang))
            reply.user.wait_for_reply("deletepack", None, lambda reply: handle_reply(reply))
            return
        
        stickerpack.status = -1
        stickerpack.owner = User(-1)
        stickerpack.stickers = []
        stickerpack.name = "."
        stickerpack.save_changes_to_db()

        await reply.reply_text(l10n("deletepack.stickerpack_was_deleted", reply.lang))