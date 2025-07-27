# Используем базовый образ Python
FROM python:3.10

# Установка системных зависимостей
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    tesseract-ocr \
    libtesseract-dev \
    build-essential \
    && apt-get clean

# Устанавливаем рабочую директорию
WORKDIR /app

#RUN pip install --upgrade pip setuptools wheel
#
#RUN pip install passport-mrz-extractor pyfcm docopt

#RUN pip install python-decouple
# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /app

# Переменная окружения для корректного отображения вывода в консоли
ENV PYTHONUNBUFFERED 1

# Открываем порт для Django
EXPOSE 8005

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8005"]

