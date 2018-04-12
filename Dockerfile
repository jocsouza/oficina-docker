FROM alpine:3.6 

RUN apk add --no-cache python py2-pip curl

ENV FLASK_APP=app.py

WORKDIR /usr/src

EXPOSE 5000

COPY . /usr/src/

RUN pip install -r requirements.txt

HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:5000/ || exit 1

CMD ["flask","run", "-h", "0.0.0.0"]

