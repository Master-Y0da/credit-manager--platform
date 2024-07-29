
FROM ubuntu:20.04


ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update
RUN apt -y install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt update
RUN apt -y install python3.8 python3-pip 


WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .