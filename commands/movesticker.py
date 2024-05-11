import misc
from classes.sticker import Sticker
from classes.stickerpack import Stickerpack
from commands import choosesticker
from l10n import l10n
from misc import Message


async def command_movesticker(message: Message) -> None:
    await choosesticker.choose_sticker(message, "movesticker", True, lambda sticker: choose_position(message, sticker))


async def choose_position(message: Message, sticker: Sticker):
    stickerpack = await Stickerpack(sticker.from_stickerpack_id).init_from_db()

    if len(stickerpack.stickers) == 0:
        await move_sticker(message, sticker, 1)
        return

    await message.reply_text(l10n("movesticker.send_position_of_sticker", message.lang, [str(len(stickerpack.stickers)+1)]))
    message.user.wait_for_reply("movesticker", None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        if not misc.is_int(reply.text):
            await message.reply_text(l10n("movesticker.write_a_number", reply.lang))
            return

        position = int(reply.text)
        if position < 1 or position > len(stickerpack.stickers) + 1:
            await message.reply_text(
                l10n("movesticker.write_a_number_from_sth_to_sth", reply.lang, ["1", str(len(stickerpack.stickers)+1)]))
            return

        await move_sticker(message, sticker, position)


async def move_sticker(message: Message, sticker: Sticker, position: int):
    stickerpack = await Stickerpack(sticker.from_stickerpack_id).init_from_db()

    stickerpack.stickers.remove(sticker)
    stickerpack.stickers.insert(position - 1, sticker)
    stickerpack.save_changes_to_db()

    await message.reply_text(l10n("movesticker.done", message.lang))
