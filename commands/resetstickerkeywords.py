from classes.sticker import Sticker
from commands import choosesticker
from l10n import l10n
from misc import Message


async def command_resetstickerkeywords(message: Message) -> None:
    await choosesticker.choose_sticker(message, "resetstickerkeywords", True,
                                       lambda sticker: send_keywords(message, sticker, []))


async def send_keywords(message: Message, sticker: Sticker, keywords=None):
    if keywords is None:
        keywords = []
    await message.reply_text(l10n("resetstickerkeywords.send_keywords", message.lang))
    message.user.wait_for_reply("resetstickerkeywords", {"finishable": True},
                                lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        if reply.text is None:
            await reply.reply_text(l10n("resetstickerkeywords.no_send_keywords", reply.lang))
            reply.user.wait_for_reply("resetstickerkeywords", {"finishable": True},
                                      lambda reply: handle_reply(reply))
            return

        if reply.text != "/finish":
            keywords.append(reply.text)
            await reply.reply_text(l10n("resetstickerkeywords.send_more_keywords", reply.lang))
            reply.user.wait_for_reply("resetstickerkeywords", {"finishable": True},
                                      lambda reply: handle_reply(reply))
            return

        sticker.keywords = keywords
        sticker.save_changes_to_db()

        await message.reply_text(l10n("resetstickerkeywords.done", reply.lang))