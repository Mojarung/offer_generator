# Dockerfile

# Базовый образ с Python
FROM python:3.10-slim-bookworm

# Установка системных зависимостей для WeasyPrint и кириллических шрифтов
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libgtk-3-0 \
    libpango-1.0-0 \
    libcairo2 \
    fonts-liberation && \
    rm -rf /var/lib/apt/lists/*

# Установка рабочей директории
WORKDIR /code

# Копирование и установка Python-зависимостей
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Копирование кода приложения
COPY ./app /code/app
EXPOSE 8080
# Команда для запуска приложения (может быть переопределена в docker-compose)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]