FROM python:alpine3.16

WORKDIR /home/data/
COPY *.py /home/data/
ENTRYPOINT [ "Counter.py" ]