FROM python:3.10.12-slim

RUN adduser worker --disabled-password
USER worker

WORKDIR /usr/src/app

RUN pip install --no-cache-dir uvicorn[standard] fastapi

ENV PATH="/home/worker/.local/bin:${PATH}"

COPY . .

EXPOSE 8000

CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000
