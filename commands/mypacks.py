from misc import Message


async def command_mypacks(message: Message) -> None:
    await message.reply_text("Your packs:\n" + "\n".join(message.user.get_added_stickerpacks_ids()))