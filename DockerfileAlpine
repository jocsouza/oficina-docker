FROM alpine:3.6 

RUN apk add --no-cache python py2-pip

ENV FLASK_APP=app.py

WORKDIR /usr/src

COPY . /usr/src/

RUN pip install -r requirements.txt

CMD ["flask","run", "-h", "0.0.0.0"]

