#!/bin/bash
cd /home/tecoxivebe38/Private-Stickers-Telegram-Bot
docker build -t private-stickers-telegram-bot .
exec docker run --rm \
  -u 1000:1000 \
  --name privsticksbot \
  -v "$(pwd)/data:/app/data" \
  private-stickers-telegram-bot