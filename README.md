# Private Stickers Telegram Bot

Telegram bot to create private stickerpacks using InlineQuery feature.

## Description

<b>Stickerpacks</b> feature is a crucial functionality of Telegram, the world-wide famous messenger. But stickerpacks themselves are public, meaning any user can use stickerpack via its unique symbolic ID. My bot offers the way to fix this privacy issue by allowing users to create, edit and delete private stickerpacks and to manage access control for them via invite codes.

This bot uses [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library.

## Capabilites

Basic commands are:

- `/createpack` - create new stickerpack
- `/addpack` - add already existing stickerpack via invite code
- `/addsticker` - add sticker to the stickerpack you own

For more commands and their descriptions, head over to [@PrivSticksBot](https://t.me/PrivSticksBot).

## How to install

1. Clone the repo
2. Create `data` folder and open it
3. Create file `token.txt` with the token of your telegram bot
4. Create file `botname.txt` with the name of the bot e.g. PrivSticksBot
5. Create file `admins.txt` with line-separated Telegram ids of admins
6. Run docker image: `sh start.sh`

## How to use

You can use my bot via [this link](https://t.me/PrivSticksBot). 

1. Create or add stickerpack using `/createpack` or `/addpack`.
2. Add stickers using `/addsticker`. You can also set their keywords and/or make them private.
3. Mention `@PrivSticksBot` in any chat. You can also add some query to get relevant stickers e.g. `@PrivSticksBot cat`.
