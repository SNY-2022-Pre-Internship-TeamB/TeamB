FROM python:3.9.10-slim

WORKDIR /backend
COPY requirements.txt /backend
RUN pip install -r requirements.txt
COPY . /backend

WORKDIR ./api