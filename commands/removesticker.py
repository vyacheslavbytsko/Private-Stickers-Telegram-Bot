from commands import deletesticker, choosesticker
from misc import Message


async def command_removesticker(message: Message) -> None:
    await choosesticker.choose_sticker(message, "removesticker",
                                       True, lambda sticker: deletesticker.delete_sticker(message, sticker))