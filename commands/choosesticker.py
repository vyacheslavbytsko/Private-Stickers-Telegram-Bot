import traceback

import misc
from classes.sticker import Sticker
from classes.stickerpack import Stickerpack
from l10n import l10n
from misc import Message


async def command_choosesticker(message: Message) -> None:
    await message.reply_text(l10n("choosesticker.internal", message.lang))


async def choose_sticker(message: Message, command: str, own: bool, func):
    await message.reply_text(l10n("choosesticker.send_sticker_via_inline_query", message.lang, [misc.botname]))
    message.user.wait_for_reply(command, {"sticker_textual_representation": True}, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        try:
            if reply.text is None:
                await reply.reply_text(l10n("choosesticker.youve_sent_actual_sticker_not_string", reply.lang))
                reply.user.wait_for_reply(command, {"sticker_textual_representation": True}, lambda reply: handle_reply(reply))
                return

            sticker = await Sticker(reply.text).init_from_db()
            stickerpack = await Stickerpack(sticker.from_stickerpack_id).init_from_db()

            if own and reply.user != stickerpack.owner:
                await message.reply_text(l10n("choosesticker.you_dont_own_stickerpack", reply.lang))
                return
            elif not own and sticker.from_stickerpack_id not in reply.user.get_all_stickerpacks_ids():
                await message.reply_text(l10n("choosesticker.you_dont_have_or_own_stickerpack", message.lang))
                return
            if sticker not in stickerpack.stickers:
                await message.reply_text(l10n("choosesticker.sticker_is_not_in_this_stickerpack", reply.lang))
                return

            await reply.tgmessage.reply_sticker(sticker.file_id)
            await func(sticker)
        except AttributeError:
            await reply.reply_text(l10n("choosesticker.youve_sent_actual_sticker_not_string", reply.lang))
            reply.user.wait_for_reply(command, {"sticker_textual_representation": True}, lambda reply: handle_reply(reply))
        except:
            print(traceback.format_exc())
            await message.reply_text(l10n("choosesticker.there_was_an_exception", reply.lang))
