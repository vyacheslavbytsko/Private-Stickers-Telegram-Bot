import telegram

from classes.stickerpack import Stickerpack
from classes.stickerpackinvite import StickerpackInvite
from l10n import l10n
from misc import Message


async def command_deletepackinvite(message: Message) -> None:
    await send_invite(message)


async def send_invite(message: Message):
    await message.reply_text(l10n("deletepackinvite.send_invite_you_own", message.lang))
    message.user.wait_for_reply("deletepackinvite", None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        try:
            stickerpackinvite = await StickerpackInvite(reply.text).init_from_db()
            stickerpack = await Stickerpack(stickerpackinvite.stickerpack_id).init_from_db()

            if reply.user != stickerpack.owner:
                await message.reply_text(l10n("deletepackinvite.you_dont_own_invites_stickerpack", reply.lang))
                return

            await confirm_choice(message, stickerpackinvite)
        except:
            await message.reply_text(l10n("deletepackinvite.couldnt_find_invite_code", reply.lang))


async def confirm_choice(message: Message, stickerpackinvite: StickerpackInvite):
    await message.reply_text(l10n("deletepackinvite.this_action_is_irreversible", message.lang), parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)
    message.user.wait_for_reply("deletepackinvite", None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        if reply.text != l10n("deletepackinvite.i_am_totally_sure", reply.lang):
            await message.reply_text(l10n("deletepackinvite.you_typed_that_message_incorrectly", reply.lang))
            return

        stickerpackinvite.name = ""
        stickerpackinvite.quantity = -1
        stickerpackinvite.time = -1
        stickerpackinvite.used_by = []
        stickerpackinvite.stickerpack_id = ""
        stickerpackinvite.save_changes_to_db()

        await message.reply_text(l10n("deletepackinvite.invite_was_deleted", reply.lang))