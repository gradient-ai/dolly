FROM python:3.8-slim-buster

RUN apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y git
COPY ./* ./
RUN pip install -r requirements.txt
RUN pip install -U gradio

CMD python app.py --share