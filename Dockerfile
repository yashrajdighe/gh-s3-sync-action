FROM python:3.15.2-slim

RUN apt update && apt install awscli -y --no-install-recommends

WORKDIR /app

COPY main.py .
COPY entrypoint.sh .

ENTRYPOINT ["/app/entrypoint.sh"]