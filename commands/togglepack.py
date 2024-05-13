from classes.stickerpack import Stickerpack
from commands import choosepack
from l10n import l10n
from misc import Message


async def command_togglepack(message: Message) -> None:
    await choosepack.choose_stickerpack(message, "togglepack",
                                        "togglepack.choose_stickerpack",
                                        False,
                                        lambda stickerpack: toggle_stickerpack(message, stickerpack))


async def toggle_stickerpack(message: Message, stickerpack: Stickerpack):
    if stickerpack.status == 1:
        stickerpack.status = 0
    elif stickerpack.status == 0:
        stickerpack.status = 1
    stickerpack.save_changes_to_db()

    if stickerpack.status == 1:
        await message.reply_text(l10n("togglepack.stickerpack_enabled", message.lang))
    elif stickerpack.status == 0:
        await message.reply_text(l10n("togglepack.stickerpack_disabled", message.lang))