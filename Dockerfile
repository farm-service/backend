FROM python:3.11-alpine

WORKDIR /backend

COPY ./requirements.txt .

RUN python -m pip install -r requirements.txt

COPY ./app ./app

CMD uvicorn app:create_app --host 0.0.0.0 --port 8000
