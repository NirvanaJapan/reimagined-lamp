FROM python:3.7.4

ADD requirements.txt /
RUN pip install -r requirements.txt
