FROM python:3.11-slim-bullseye

WORKDIR /src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
