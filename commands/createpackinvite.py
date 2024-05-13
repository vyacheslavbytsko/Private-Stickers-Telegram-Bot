from uuid import uuid4

import telegram

import misc
from classes.stickerpack import Stickerpack
from classes.stickerpackinvite import StickerpackInvite
from commands import choosepack
from l10n import l10n
from misc import Message

import time as timelib


async def command_createpackinvite(message: Message) -> None:
    await choosepack.choose_stickerpack(message, "createpackinvite", "createpackinvite.choose_stickerpack", True, lambda stickerpack: choose_number_of_people(message, stickerpack))


async def choose_number_of_people(message: Message, stickerpack: Stickerpack):
    await message.reply_text(l10n("createpackinvite.how_many_people_can_add_your_stickerpack_via_this_invite", message.lang))
    message.user.wait_for_reply("createpackinvite", None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        if not misc.is_int(reply.text):
            await message.reply_text(l10n("createpackinvite.write_a_number", reply.lang))
            message.user.wait_for_reply("createpackinvite", None, lambda reply: handle_reply(reply))
            return

        quantity = int(reply.text)
        if quantity < 0:
            await message.reply_text(l10n("createpackinvite.write_a_positive_number_or_zero", reply.lang))
            message.user.wait_for_reply("createpackinvite", None, lambda reply: handle_reply(reply))
            return

        await choose_expire_time(message, stickerpack, quantity)


async def choose_expire_time(message: Message, stickerpack: Stickerpack, quantity: int):
    await message.reply_text(l10n("createpackinvite.for_how_many_hours_this_invite_can_be_used", message.lang))
    message.user.wait_for_reply("createpackinvite", None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        if not misc.is_int(reply.text):
            await reply.reply_text(l10n("createpackinvite.write_a_number", reply.lang))
            return

        time = int(reply.text)
        if time < 0:
            await reply.reply_text(l10n("createpackinvite.write_a_positive_number_or_zero", reply.lang))
            return

        await write_name(message, stickerpack, quantity, time)


async def write_name(message: Message, stickerpack: Stickerpack, quantity: int, time: int):
    await message.reply_text(l10n("createpackinvite.write_the_name_of_invite", message.lang))
    message.user.wait_for_reply("createpackinvite", {"finishable": True}, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        name = reply.text if reply.text != "/finish" else ""

        stickerpackinvite = StickerpackInvite(
            str(uuid4()),
            stickerpack.id,
            quantity if quantity > 0 else -1,
            int(timelib.time()) + (time * 3600) if time != 0 else -1,
            name,
            []
        ).save_changes_to_db(new_stickerpackinvite=True)

        await message.reply_text(l10n("createpackinvite.your_invite_code_is", reply.lang, [stickerpackinvite.invite_code]),
                                 parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)

