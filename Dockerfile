FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel

RUN mkdir /app
RUN mkdir /app/output

WORKDIR /app

ADD ./requierements.txt .

RUN pip install -r requierements.txt

ADD ./download.py .

RUN python download.py

ADD main.py .
