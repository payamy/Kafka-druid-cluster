FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

RUN apk --no-cache upgrade \
    && pip install --upgrade pip \
    && apk --no-cache add tzdata build-base gcc libc-dev g++ make git bash

RUN git clone https://github.com/edenhill/librdkafka.git && cd librdkafka \
    && git checkout tags/v2.2.0 && ./configure --clean \
    && ./configure --prefix /usr/local \
    && make && make install

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./main.py /main.py
