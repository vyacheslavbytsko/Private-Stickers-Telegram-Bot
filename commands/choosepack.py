from classes.stickerpack import Stickerpack
from commands import createpack
from exceptions import NoSuchStickerpackException
from l10n import l10n
from misc import Message


async def command_choosepack(message: Message) -> None:
    await message.reply_text(l10n("choosepack.internal", message.lang))


async def choose_stickerpack(message: Message, command: str, l10n_str: str, own: bool, func,
                             offer_creating_new: bool = False, func_if_new_failed=None) -> None:
    if own:
        await choose_own_stickerpack(message, command, l10n_str, func, offer_creating_new, func_if_new_failed)
    else:
        await choose_added_stickerpack(message, command, l10n_str, func, offer_creating_new, func_if_new_failed)


async def choose_own_stickerpack(message: Message, command: str, l10n_str: str, func,
                                 offer_creating_new: bool = False, func_if_new_failed=None):
    if not offer_creating_new:
        stickerpacks = message.user.get_own_stickerpacks_ids()
        if len(stickerpacks) == 0:
            await message.reply_text(l10n("choosepack.you_dont_have_own_stickerpacks", message.lang))
            return
        elif len(stickerpacks) == 1:
            stickerpack = await Stickerpack(stickerpacks[0]).init_from_db()
            await message.reply_text(l10n("choosepack.you_have_only_one_own_stickerpack_choosing_it",
                                          message.lang, [stickerpack.name]))
            await func(stickerpack)
            return

    await message.reply_text(l10n(l10n_str, message.lang),
                             reply_markup=message.user.own_stickerpacks_ids_reply_markup(offer_creating_new=offer_creating_new))
    message.user.wait_for_reply(command, None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        stickerpack_id = reply.text

        if stickerpack_id == "new" and offer_creating_new:
            await createpack.create_stickerpack(reply, lambda stickerpack: func(stickerpack), func_if_new_failed)
            return

        try:
            stickerpack = await Stickerpack(stickerpack_id).init_from_db()
            if reply.user != stickerpack.owner:
                await reply.reply_text(l10n("choosepack.you_dont_own_stickerpack", reply.lang))
                return
            if stickerpack.id not in reply.user.get_all_stickerpacks_ids():
                await reply.reply_text(l10n("choosepack.you_dont_have_stickerpack_in_library", reply.lang))
                return
            await func(stickerpack)
        except NoSuchStickerpackException:
            await reply.reply_text(l10n("choosepack.this_stickerpack_does_not_exist", reply.lang))


async def choose_added_stickerpack(message: Message, command: str, l10n_str: str, func,
                                   offer_creating_new: bool = False, func_if_new_failed=None):
    if not offer_creating_new:
        stickerpacks = message.user.get_added_stickerpacks_ids()
        if len(stickerpacks) == 0:
            await message.reply_text(l10n("choosepack.you_dont_have_stickerpacks", message.lang))
            return
        elif len(stickerpacks) == 1:
            stickerpack = await Stickerpack(stickerpacks[0]).init_from_db()
            await message.reply_text(l10n("choosepack.you_have_only_one_stickerpack_choosing_it",
                                          message.lang, [stickerpack.name]))
            await func(stickerpack)
            return

    await message.reply_text(l10n(l10n_str, message.lang),
                             reply_markup=message.user.added_stickerpacks_ids_reply_markup(offer_creating_new=offer_creating_new))
    message.user.wait_for_reply(command, None, lambda reply: handle_reply(reply))

    async def handle_reply(reply: Message):
        stickerpack_id = reply.text

        if stickerpack_id == "new" and offer_creating_new:
            await createpack.create_stickerpack(reply, lambda stickerpack: func(stickerpack), func_if_new_failed)
            return

        try:
            stickerpack = await Stickerpack(stickerpack_id).init_from_db()
            if stickerpack.id not in reply.user.get_added_stickerpacks_ids():
                await reply.reply_text(l10n("choosepack.you_dont_have_stickerpack", reply.lang))
                return
            await func(stickerpack)
        except NoSuchStickerpackException:
            await reply.reply_text(l10n("choosepack.this_stickerpack_does_not_exist", reply.lang))
