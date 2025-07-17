# Используем официальный Python-образ
FROM python:3.13.5-alpine3.22

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости и код внутрь контейнера
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Запускаем бота
CMD ["python", "main.py"]