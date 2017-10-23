FROM python:3.5
MAINTAINER Nihal Harish <nihal.harish@stonybrook.edu>

RUN pip install pyDistAlgo

RUN pip install pycrypto

RUN pip install RandomWords

RUN pip install uuid

RUN mkdir -p /usr/app/src

RUN mkdir -p /usr/app/logs

RUN mkdir -p /usr/app/config

WORKDIR /usr/app/src

COPY config/ /usr/app/config/

COPY src/ /usr/app/src/

COPY logs/ /usr/app/logs/

RUN python3 -m da.compiler replica.da

RUN python3 -m da.compiler client.da

RUN python3 -m da.compiler olympus.da

expose 8080
expose 15000

