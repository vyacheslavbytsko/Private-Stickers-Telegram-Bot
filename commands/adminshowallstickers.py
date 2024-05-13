import misc
from classes.sticker import Sticker
from misc import Message


async def command_adminshowallstickers(message: Message) -> None:
    if message.user.id not in list(map(int, open("/app/data/admins.txt").read().split(","))):
        await message.reply_text(f"You ({message.user.id}) are not the admin of this bot.")
        return

    cursor = misc.db.execute("SELECT * FROM Stickers", [])
    stickers = [await Sticker(row[0]).init_from_db(throw_exception=False) for row in cursor]
    cursor.close()

    for sticker in stickers:
        try:
            await message.reply_text(sticker.id)
            await message.tgmessage.reply_sticker(sticker.file_id)
        except:
            await message.reply_text("Unable to send sticker.")
