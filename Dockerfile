FROM python:alpine3.16

WORKDIR /home/

COPY *.py /home/
COPY *.sh /home/
RUN chmod +x *.sh
RUN mkdir -p "/home/output/"

CMD [ "sh", "./run.sh" ]