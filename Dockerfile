# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt