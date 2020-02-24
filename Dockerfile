FROM python:3.8-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=true

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt
