FROM hub.hamdocker.ir/library/python:3.8-slim-buster

WORKDIR /app

COPY hello.py .

RUN pip install flask

EXPOSE 8080

CMD ["python", "hello.py"]

