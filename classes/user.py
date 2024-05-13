from datetime import datetime
from typing import Self, List

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

import misc
from l10n import l10n
from misc import stringify, listify

cached_users = {}


def create_db() -> None:
    misc.db.execute(
        "CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, lang TEXT, stickerpacks TEXT, boughtSlots INTEGER)")


class User:
    def __init__(self, id: int, lang: str = "en", bought_slots: int = 0) -> None:
        self.id = id if misc.is_int(id) else int(id)
        self.lang = lang
        self.bought_slots = bought_slots

    def __eq__(self, value: Self) -> bool:
        return self.id == value.id

    def get_user(self) -> Self:
        if self.id not in cached_users.keys():
            misc.db.execute('INSERT OR IGNORE INTO Users (id, lang, stickerpacks, boughtSlots) VALUES (?, ?, ?, ?)',
                            (self.id, None, None, None))
            misc.db.commit()
            cursor = misc.db.execute("SELECT lang, boughtSlots FROM Users WHERE id = ?", [self.id])
            lang, bought_slots = cursor.fetchone()
            cursor.close()
            user = User(self.id, lang, bought_slots)
            cached_users[user.id] = (user, 0)
        expires_at = int(datetime.now().timestamp()) + 1 * 60 * 60
        cached_users[self.id] = (cached_users[self.id][0], expires_at)
        return cached_users[self.id][0]

    def update_user(self) -> Self:
        cached_users.pop(self.id)
        return self.get_user()

    def write_language_to_db(self, lang: str) -> None:
        misc.db.execute("UPDATE Users SET lang = ? WHERE id = ?", [lang, self.id])
        misc.db.commit()
        self.update_user()

    def get_added_stickerpacks_ids(self) -> List[str]:
        cursor = misc.db.execute("SELECT * FROM Users WHERE id = ?", [self.id])
        stickerpacks_by_ids = list(filter(lambda stickerpack_id: misc.does_stickerpack_exist(stickerpack_id),
                                          listify(cursor.fetchone()[2] or "")))
        cursor.close()
        return stickerpacks_by_ids

    def get_own_stickerpacks_ids(self) -> List[str]:
        cursor = misc.db.execute("SELECT * FROM Stickerpacks WHERE owner = ?", [self.id])
        stickerpacks_by_ids = list(filter(lambda stickerpack_id: misc.does_stickerpack_exist(stickerpack_id),
                                          [stickerpack_row[0] for stickerpack_row in cursor.fetchall()]))
        cursor.close()
        return stickerpacks_by_ids

    def get_all_stickerpacks_ids(self) -> List[str]:
        return list({*self.get_added_stickerpacks_ids(), *self.get_own_stickerpacks_ids()})

    def set_stickerpacks_ids(self, stickerpacks_ids: List[str]) -> None:
        misc.db.execute("UPDATE Users SET stickerpacks = ? WHERE id = ?", [stringify(stickerpacks_ids), self.id])
        misc.db.commit()

    def added_stickerpacks_ids_reply_markup(self, offer_creating_new: bool = False):
        stickerpacks_ids = self.get_added_stickerpacks_ids()
        keyboard = []
        for stickerpack_id in stickerpacks_ids:
            name = misc.db.execute("SELECT name FROM Stickerpacks WHERE id = ?", [stickerpack_id]).fetchone()[0]
            keyboard.append([InlineKeyboardButton(name, callback_data=stickerpack_id)])
        if offer_creating_new:
            keyboard.append([InlineKeyboardButton(l10n("choosepack.create_new_stickerpack", self.lang), callback_data="new")])
        return InlineKeyboardMarkup(keyboard)

    def own_stickerpacks_ids_reply_markup(self, offer_creating_new: bool = False):
        stickerpacks_ids = self.get_own_stickerpacks_ids()
        keyboard = []
        for stickerpack_id in stickerpacks_ids:
            name = misc.db.execute("SELECT name FROM Stickerpacks WHERE id = ?", [stickerpack_id]).fetchone()[0]
            keyboard.append([InlineKeyboardButton(name, callback_data=stickerpack_id)])
        if offer_creating_new:
            keyboard.append([InlineKeyboardButton(l10n("choosepack.create_new_stickerpack", self.lang), callback_data="new")])
        return InlineKeyboardMarkup(keyboard)

    def wait_for_reply(self, command: str, data: dict, func ) -> None:
        misc.waiting_for_reply[self.id] = (command, data, func)


async def pop_users(context: ContextTypes.DEFAULT_TYPE) -> None:
    global cached_users
    for userid in list(cached_users.keys()):
        user, expires_at = cached_users[userid]
        if expires_at <= int(datetime.now().timestamp()):
            del cached_users[userid]

