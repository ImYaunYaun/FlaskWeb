FROM python:latest

WORKDIR /app

COPY . /app

RUN apt-get update

RUN apt-get install nano

RUN pip install -r requirements.txt

CMD python3 main.py 