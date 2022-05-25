FROM python:3.8

RUN apt-get update

WORKDIR /src/

COPY requirements.txt /src/

RUN pip install -r /src/requirements.txt

COPY . .