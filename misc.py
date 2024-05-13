import os
import queue
import traceback
from threading import Thread
from uuid import uuid4
from PIL import Image
from typing import List
from telegram import InputSticker, Update
from telegram.ext import ContextTypes

import sqlite3 as lite

import telegram

from l10n import l10n

if not os.path.isfile('/app/data/privsticksbot.db'):
    raise Exception('privsticksbot.db not found')

db = lite.connect('/app/data/privsticksbot.db')

media_made = queue.Queue()

botname = "PrivSticksBot"

stickerset_created_by_bot = "Created by @{botname}"


def stringify(arr: list) -> str:
    return ",".join(arr)


def listify(arr: str) -> list:
    if arr is None: return []
    result = arr.split(",")
    if len(result) == 1 and result[0] == '': return []
    return result


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


async def not_in_available_statuses(message: telegram.Message, user_status: str, available_statuses: List[str]):
    if user_status not in available_statuses:
        await message.reply_text("Another action is pending. To cancel, /cancel")
        return True
    return False


def does_stickerpack_exist(stickerpack_id: str) -> bool:
    cursor = db.execute("SELECT * FROM Stickerpacks WHERE id = ? AND status != -1", [stickerpack_id])
    row = cursor.fetchone()
    cursor.close()
    if row is None: return False
    return True


def expand2square(pil_img: Image.Image):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new("RGBA", (width, width), (0, 0, 0, 0))
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new("RGBA", (height, height), (0, 0, 0, 0))
        result.paste(pil_img, ((height - width) // 2, 0))
        return result


waiting_for_reply = {}

from classes.user import User


class Message:
    def __init__(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.update = update
        self.context = context
        self.text, self.user, self.tgmessage = three_bogatyrs(self.update)
        self.reply_text = self.tgmessage.reply_text
        self.lang = self.user.lang


async def photo2sticker(user: User, message: telegram.Message, func) -> None:
    if message.photo[-1].file_size > telegram.constants.FileSizeLimit.FILESIZE_DOWNLOAD:
        await message.reply_text(l10n("general.photo_is_too_big", user.lang))
        return

    await message.reply_text(l10n("general.trying_to_convert_photo_to_sticker", user.lang))

    filename = "temp/photosticker{}".format(user.id)
    filename_out = "temp/outphotosticker{}.webp".format(user.id)

    if not os.path.isdir("temp"):
        os.mkdir("temp")

    if os.path.isfile(filename):
        os.remove(filename)

    if os.path.isfile(filename_out):
        os.remove(filename_out)

    await (await message.get_bot().get_file(message.photo[-1].file_id)).download_to_drive(filename)

    def make_photo():
        image = Image.open(filename)

        image.thumbnail((512, 512))
        #image = expand2square(image)

        #image.save(cropped_image_bytes_io, format="WEBP")
        image.save(filename_out, format="WEBP")

        media_made.put(after_making_photo)
        #media_made[user.id] = after_making_photo

    thread = Thread(target=make_photo)
    thread.start()

    async def after_making_photo():
        try:
            await message.reply_text(l10n("general.your_sticker_from_photo", user.lang))
            present_sticker_from_photo_message = await message.reply_sticker(open(filename_out, "rb"), emoji='🙂')
            present_sticker_from_photo = present_sticker_from_photo_message.sticker

            os.remove(filename)
            os.remove(filename_out)

            await func(present_sticker_from_photo)
        except Exception as e:
            print(traceback.format_exc())
            if os.path.isfile(filename):
                os.remove(filename)
            if os.path.isfile(filename_out):
                os.remove(filename_out)
            # TODO: l10n
            await message.reply_text("Couldn't convert photo to sticker. Please try again.")
            raise e


async def video2sticker(user: User, message: telegram.Message, func) -> None:
    if message.video.file_size > telegram.constants.FileSizeLimit.FILESIZE_DOWNLOAD:
        await message.reply_text(l10n("general.video_is_too_big", user.lang))
        return

    await message.reply_text(l10n("general.trying_to_convert_video_to_sticker", user.lang))

    filename = "temp/videosticker{}.{}".format(user.id, message.video.mime_type.split("/")[-1])
    filename_logs = "temp/logsvideosticker{}".format(user.id)
    filename_out = "temp/outvideosticker{}.{}".format(user.id, message.video.mime_type.split("/")[-1])

    if not os.path.isdir("temp"):
        os.mkdir("temp")

    if os.path.isfile(filename):
        os.remove(filename)
    if os.path.isfile(filename_out):
        os.remove(filename_out)
    if os.path.isfile(filename_logs + "-0.log"):
        os.remove(filename_logs + "-0.log")

    await (await message.get_bot().get_file(message.video.file_id)).download_to_drive(filename)

    def make_video():
        import subprocess
        import shlex

        command = shlex.split(
            f"ffmpeg -y -i \"{filename}\" -vf \"fps=30,scale=if(gte(iw\\,ih)\\,512\\,-2):if(lt(iw\\,ih)\\,512\\,-2)\" -ss 00:00:00 -to 00:00:03 -an -b:v 500k -format webm -pass 1 -passlogfile \"{filename_logs}\" -vcodec vp9 -f webm /dev/null")
        subprocess.run(command, stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'))
        command2 = shlex.split(
            f"ffmpeg -y -i \"{filename}\" -vf \"fps=30,scale=if(gte(iw\\,ih)\\,512\\,-2):if(lt(iw\\,ih)\\,512\\,-2)\" -ss 00:00:00 -to 00:00:03 -an -b:v 500k -format webm -pass 2 -passlogfile \"{filename_logs}\" -vcodec vp9 -f webm \"{filename_out}\"")
        subprocess.run(command2, stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'))


        media_made.put(after_making_video)
        #media_made[user.id] = after_making_video

    thread = Thread(target=make_video)
    thread.start()

    async def after_making_video():
        try:
            internal_telegram_stickerpack_id = "set_" + str(uuid4())[:10].replace("-", "") + "_by_" + botname

            try:
                await message.get_bot().delete_sticker_set(internal_telegram_stickerpack_id)
            except Exception:
                pass

            await message.get_bot().create_new_sticker_set(user.id, internal_telegram_stickerpack_id,
                                                           stickerset_created_by_bot, [
                                                               InputSticker(open(filename_out, "br").read(), ['🙂'], "video")
                                                           ])

            os.remove(filename)
            os.remove(filename_out)
            os.remove(filename_logs + "-0.log")

            sticker_id = (await message.get_bot().get_sticker_set(internal_telegram_stickerpack_id)).stickers[0].file_id

            try:
                await message.get_bot().delete_sticker_set(internal_telegram_stickerpack_id)
            except Exception:
                await message.get_bot().delete_sticker_from_set(sticker_id)

            await message.reply_text(l10n("general.your_sticker_from_video", user.lang))
            present_sticker_from_video = (await message.reply_sticker(sticker_id)).sticker

            await func(present_sticker_from_video)
        except Exception as e:
            if os.path.isfile(filename):
                os.remove(filename)
            if os.path.isfile(filename_out):
                os.remove(filename_out)
            if os.path.isfile(filename_logs+"-0.log"):
                os.remove(filename_logs+"-0.log")
            # TODO: l10n
            await message.reply_text("Couldn't convert video to sticker. Please try again.")
            raise e


async def animation2sticker(user: User, message: telegram.Message, func) -> None:
    if message.animation.file_size > telegram.constants.FileSizeLimit.FILESIZE_DOWNLOAD:
        await message.reply_text(l10n("general.animation_is_too_big", user.lang))
        return

    await message.reply_text(l10n("general.trying_to_convert_animation_to_sticker", user.lang))

    filename = "temp/animationsticker{}.{}".format(user.id, message.animation.mime_type.split("/")[-1])
    filename_logs = "temp/logsanimationsticker{}".format(user.id)
    filename_out = "temp/outanimationsticker{}.{}".format(user.id, message.animation.mime_type.split("/")[-1])

    if not os.path.isdir("temp"):
        os.mkdir("temp")

    if os.path.isfile(filename):
        os.remove(filename)
    if os.path.isfile(filename_out):
        os.remove(filename_out)
    if os.path.isfile(filename_logs + "-0.log"):
        os.remove(filename_logs + "-0.log")

    await (await message.get_bot().get_file(message.animation.file_id)).download_to_drive(filename)

    def make_animation():
        import subprocess
        import shlex

        command = shlex.split(
            f"ffmpeg -y -i \"{filename}\" -vf \"fps=30,scale=if(gte(iw\\,ih)\\,512\\,-2):if(lt(iw\\,ih)\\,512\\,-2)\" -ss 00:00:00 -to 00:00:03 -an -b:v 500k -format webm -pass 1 -passlogfile \"{filename_logs}\" -vcodec vp9 -f webm /dev/null")
        subprocess.run(command, stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'))
        command2 = shlex.split(
            f"ffmpeg -y -i \"{filename}\" -vf \"fps=30,scale=if(gte(iw\\,ih)\\,512\\,-2):if(lt(iw\\,ih)\\,512\\,-2)\" -ss 00:00:00 -to 00:00:03 -an -b:v 500k -format webm -pass 2 -passlogfile \"{filename_logs}\" -vcodec vp9 -f webm \"{filename_out}\"")
        subprocess.run(command2, stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'))

        media_made.put(after_making_animation)

    thread = Thread(target=make_animation)
    thread.start()

    async def after_making_animation():
        try:
            internal_telegram_stickerpack_id = "set_" + str(uuid4())[:10].replace("-", "") + "_by_" + botname

            try:
                await message.get_bot().delete_sticker_set(internal_telegram_stickerpack_id)
            except Exception:
                pass

            await message.get_bot().create_new_sticker_set(user.id, internal_telegram_stickerpack_id,
                                                           stickerset_created_by_bot, [
                                                               InputSticker(open(filename_out, "br").read(), ['🙂'],
                                                                            "video")
                                                           ])

            os.remove(filename)
            os.remove(filename_out)
            os.remove(filename_logs + "-0.log")

            sticker_id = (await message.get_bot().get_sticker_set(internal_telegram_stickerpack_id)).stickers[0].file_id

            try:
                await message.get_bot().delete_sticker_set(internal_telegram_stickerpack_id)
            except Exception:
                await message.get_bot().delete_sticker_from_set(sticker_id)

            await message.reply_text(l10n("general.your_sticker_from_animation", user.lang))
            present_sticker_from_animation = (await message.reply_sticker(sticker_id)).sticker

            await func(present_sticker_from_animation)
        except Exception as e:
            if os.path.isfile(filename):
                os.remove(filename)
            if os.path.isfile(filename_out):
                os.remove(filename_out)
            if os.path.isfile(filename_logs + "-0.log"):
                os.remove(filename_logs + "-0.log")
            # TODO: l10n
            await message.reply_text("Couldn't convert animation to sticker. Please try again.")
            raise e


def three_bogatyrs(update: Update):
    text = update.message.text if update.message else update.callback_query.data
    user = User((update.message or update.callback_query).from_user.id).get_user()
    message = update.message or update.callback_query.message
    return text, user, message
