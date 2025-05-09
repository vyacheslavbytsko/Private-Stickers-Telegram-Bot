import traceback
from uuid import uuid4

from classes.stickerpack import Stickerpack
from l10n import l10n
from misc import Message


async def command_createpack(message: Message) -> None:
    await create_stickerpack(message)


async def create_stickerpack(message: Message, func_if_created=None, func_if_failed=None):
    await message.reply_text(l10n("createpack.write_name_of_new_stickerpack", message.lang))
    message.user.wait_for_reply("createpack", None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        try:
            stickerpack = Stickerpack(str(uuid4()), reply.user, [], reply.text, True)
            stickerpack.save_changes_to_db(new_stickerpack=True)

            stickerpacks_ids = reply.user.get_added_stickerpacks_ids()
            stickerpacks_ids.append(stickerpack.id)
            reply.user.set_stickerpacks_ids(stickerpacks_ids)

            await reply.reply_text(l10n("createpack.new_stickerpack_is_created", reply.lang))
            if func_if_created is not None:
                await func_if_created(stickerpack)
        except:
            print(traceback.format_exc())
            await message.reply_text(l10n("createpack.there_was_an_exception", reply.lang))
            if func_if_failed is not None:
                await func_if_failed()

