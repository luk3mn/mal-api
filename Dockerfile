# Use an official Python runtime as the base image
FROM python:3.8-slim-buster
# FROM python:3.9

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

# CMD ["python3","run.py"]