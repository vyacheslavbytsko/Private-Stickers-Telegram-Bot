import time as timelib
from typing import Self

import misc
from classes.user import User
from exceptions import NoSuchStickerpackInviteException
from misc import stringify, listify


def create_db() -> None:
    misc.db.execute(
        "CREATE TABLE IF NOT EXISTS StickerpacksInvites (inviteCode TEXT PRIMARY KEY, stickerpackId TEXT NOT NULL, "
        "quantity INTEGER, time INTEGER, name TEXT, usedBy TEXT)")


class StickerpackInvite:
    def __init__(self, invite_code: str, stickerpack_id: str = None, quantity: int = None, time: int = None,
                 name: str = None, used_by=None) -> None:
        if used_by is None:
            used_by = []
        self.invite_code = invite_code
        self.stickerpack_id = stickerpack_id
        self.quantity = quantity
        self.time = time
        self.name = name
        self.used_by = [User(used_by_id).get_user() for used_by_id in used_by]

    async def init_from_db(self) -> Self:
        cursor = misc.db.execute("SELECT * FROM StickerpacksInvites WHERE inviteCode = ?", [self.invite_code])
        row = cursor.fetchone()
        if row is None:
            cursor.close()
            raise NoSuchStickerpackInviteException(
                "There's no stickerpack invite with given inviteCode in the database.")

        self.stickerpack_id = row[1]
        self.quantity = row[2]
        self.time = row[3]
        self.name = row[4]
        self.used_by = [User(user_id).get_user() for user_id in listify(row[5])]

        cursor.close()

        if self.stickerpack_id == "" or self.stickerpack_id is None:
            raise NoSuchStickerpackInviteException("Stickerpack invite was deleted.")
        if (len(self.used_by) >= self.quantity) and (self.quantity != -1):
            raise NoSuchStickerpackInviteException(
                "Stickerpack invite is overused hence invalid. It cannot be used anymore.")
        if (int(timelib.time()) >= self.time) and (self.time != -1):
            raise NoSuchStickerpackInviteException(
                "Stickerpack invite is expired hence invalid. It cannot be used anymore.")

        return self

    def save_changes_to_db(self, new_stickerpackinvite: bool = False) -> Self:
        misc.db.execute(("INSERT " if new_stickerpackinvite else "REPLACE ") +
                        "INTO StickerpacksInvites(inviteCode, stickerpackId, quantity, time, name, usedBy) VALUES (?, "
                        "?, ?, ?, ?, ?)",
            [self.invite_code, self.stickerpack_id, self.quantity, self.time, self.name,
             stringify([str(user.id) for user in self.used_by])])
        misc.db.commit()
        return self
