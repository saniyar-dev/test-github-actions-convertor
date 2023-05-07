FROM python:3.8-slim-buster

WORKDIR /app

COPY hello.py .

CMD ["python", "hello.py"]

