# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

ADD server.py /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD [ "python3", "./server.py"]


