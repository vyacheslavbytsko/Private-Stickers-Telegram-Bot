#!/bin/bash
cd /home/tecoxivebe38/Private-Stickers-Telegram-Bot
docker build -t private-stickers-telegram-bot .
exec docker run --rm \
  --name privsticksbot \
  -v "$(pwd)/data:/app/data:Z" \
  private-stickers-telegram-bot