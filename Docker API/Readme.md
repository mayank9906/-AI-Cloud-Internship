# Dockerized Async File Process

## Install

pip install -r requirements.txt

## Run without Docker

uvicorn main:app --reload

## Build Docker

docker build -t async-api .

## Run Docker

docker run -p 8000:8000 --env-file .env async-api

## Swagger

http://localhost:8000/docs