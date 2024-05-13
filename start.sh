#!/bin/bash
docker build -t private-stickers-telegram-bot .
exec docker run --rm \
  --name privsticksbot \
  -v "$(pwd)/data:/app/data:Z" \
  private-stickers-telegram-bot