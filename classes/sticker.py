from typing import List, Self

from exceptions import NoSuchStickerException

import misc
from misc import stringify, listify


def create_db() -> None:
    misc.db.execute(
        "CREATE TABLE IF NOT EXISTS Stickers (id TEXT PRIMARY KEY, fileId TEXT NOT NULL, fromStickerpackId TEXT NOT NULL, keywords TEXT)")


class Sticker:
    def __init__(self, id: str, file_id: str = "", from_stickerpack_id: str = None, keywords: List[str] = []) -> None:
        self.id = id
        self.file_id = file_id
        self.from_stickerpack_id = from_stickerpack_id
        self.keywords = keywords

    def __eq__(self, value: Self) -> bool:
        return self.id == value.id

    async def init_from_db(self, throw_exception: bool = True) -> Self:
        cursor = misc.db.execute("SELECT * FROM Stickers WHERE id = ?", [self.id])
        row = cursor.fetchone()
        if row is None:
            cursor.close()
            if throw_exception:
                raise NoSuchStickerException("There's no sticker with given ID in the database: " + self.id)
            else:
                return None

        self.file_id = row[1]
        self.from_stickerpack_id = row[2]
        self.keywords = listify(row[3])

        cursor.close()
        return self

    def save_changes_to_db(self, new_sticker: bool = False) -> Self:
        misc.db.execute((
                            "INSERT" if new_sticker else "REPLACE") + " INTO Stickers(id, fileId, fromStickerpackId, keywords) VALUES (?, ?, ?, ?)",
                        [self.id, self.file_id, self.from_stickerpack_id, stringify(self.keywords)])
        misc.db.commit()
        return self
