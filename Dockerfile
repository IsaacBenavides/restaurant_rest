FROM python:3.8.0

RUN apt-get update

WORKDIR /src/

COPY requirements.txt /src/

RUN pip install -r requirements.txt

COPY . .