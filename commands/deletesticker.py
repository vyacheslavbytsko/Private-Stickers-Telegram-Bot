import telegram

from classes.sticker import Sticker
from classes.stickerpack import Stickerpack
from commands import choosesticker
from l10n import l10n
from misc import Message


async def command_deletesticker(message: Message) -> None:
    await choosesticker.choose_sticker(message, "deletesticker", True, lambda sticker: delete_sticker(message, sticker))


async def delete_sticker(message: Message, sticker: Sticker):
    await message.reply_text(l10n("deletesticker.this_action_is_irreversible", message.lang), parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)
    message.user.wait_for_reply("deletesticker", None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        if reply.text != l10n("deletesticker.i_am_totally_sure", reply.lang):
            await message.reply_text(l10n("deletesticker.you_typed_that_message_incorrectly", reply.lang))
            return

        stickerpack = await Stickerpack(sticker.from_stickerpack_id).init_from_db()

        sticker.file_id = "."
        sticker.keywords = []
        sticker.save_changes_to_db()

        stickerpack.stickers.remove(sticker)
        stickerpack.save_changes_to_db()

        await message.reply_text(l10n("deletesticker.sticker_was_deleted", reply.lang))