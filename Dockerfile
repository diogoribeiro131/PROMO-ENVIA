FROM python:3-alpine

WORKDIR /app

COPY . .

CMD python app.py

RUN pip install --upgrade pip
RUN pip install requests
RUN pip install bs4
RUN pip install telebot