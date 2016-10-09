#Base image
FROM python:3.6.0b1
MAINTAINER Einer Rafael

ENV PYTHONUNBUFFERED=1
ENV CODE=/code

COPY requirements.txt /
RUN pip3 install -r requirements.txt

WORKDIR $CODE
VOLUME $CODE

#FROM library/postgres
#ADD init.sql /docker-entrypoint-initdb.d/