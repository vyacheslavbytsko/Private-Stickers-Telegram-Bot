FROM python:3.13.5-alpine3.22

WORKDIR /app

RUN apk update
RUN apk upgrade
RUN apk add --no-cache ffmpeg

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]