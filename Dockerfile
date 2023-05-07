FROM python:3.8-slim-buster

WORKDIR /app

COPY hello.py .

RUN pip install flask

EXPOSE 3000

CMD ["python", "app.py"]

