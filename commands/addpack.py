from classes.stickerpackinvite import StickerpackInvite
from exceptions import NoSuchStickerpackInviteException
from l10n import l10n
from misc import Message


async def command_addpack(message: Message) -> None:
    await send_invite(message)


async def send_invite(message: Message):
    await message.reply_text(l10n("addpack.send_invite", message.lang))
    message.user.wait_for_reply("addpack", None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        try:
            stickerpackinvite = await StickerpackInvite(reply.text).init_from_db()
            if stickerpackinvite.stickerpack_id in message.user.get_added_stickerpacks_ids():
                await message.reply_text(l10n("addpack.you_already_have_this_stickerpack", message.lang))
                return

            stickerpacks_ids = reply.user.get_added_stickerpacks_ids()
            stickerpacks_ids.append(stickerpackinvite.stickerpack_id)
            reply.user.set_stickerpacks_ids(stickerpacks_ids)

            stickerpackinvite.used_by.append(reply.user)
            stickerpackinvite.save_changes_to_db()

            await message.reply_text(l10n("addpack.stickerpack_added_successfully", reply.lang))
        except NoSuchStickerpackInviteException:
            await message.reply_text(l10n("addpack.couldnt_find_invite_code", message.lang))
