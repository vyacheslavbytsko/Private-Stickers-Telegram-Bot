from typing import List, Self

from classes.user import User
from classes.sticker import Sticker

from exceptions import NoSuchStickerpackException

import misc
from misc import stringify, listify


def create_db() -> None:
    misc.db.execute("CREATE TABLE IF NOT EXISTS Stickerpacks (id TEXT PRIMARY KEY, owner INTEGER NOT NULL, "
                    "stickers TEXT, name TEXT, status INTEGER NOT NULL)")


class Stickerpack:
    def __init__(self, id: str, owner: User = None, stickers: List[Sticker] = [], name: str = None,
                 status: int = -1) -> None:
        self.id = id
        self.owner = owner
        self.stickers = stickers
        self.name = name
        self.status = status

    async def init_from_db(self) -> Self:
        cursor = misc.db.execute("SELECT * FROM Stickerpacks WHERE id = ?", [self.id])
        row = cursor.fetchone()
        if row is None:
            cursor.close()
            raise NoSuchStickerpackException("There's no stickerpack with given ID in the database.")

        self.owner = User(row[1]).get_user()
        self.stickers = [await Sticker(sticker_id).init_from_db() for sticker_id in listify(row[2])]
        self.name = row[3]
        self.status = row[4]

        cursor.close()
        return self

    def save_changes_to_db(self, new_stickerpack: bool = False) -> Self:
        misc.db.execute(("INSERT" if new_stickerpack else "REPLACE") + " INTO Stickerpacks(id, owner, stickers, name, status) VALUES (?, ?, ?, ?, ?)",
                        [self.id, self.owner.id,
                         stringify([sticker.id for sticker in self.stickers]),
                         self.name, self.status])
        misc.db.commit()
        return self
