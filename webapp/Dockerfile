FROM alpine:latest

RUN apk update && apk add --no-cache python3 py3-pip

WORKDIR /
ADD ./requirements.txt /
RUN pip3 install -r requirements.txt
ADD ./main.py /

CMD python3 main.py
