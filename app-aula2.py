import logging
from flask import Flask, request
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

@app.route("/")
def hello():
    app.logger.error(('The referrer was {}'.format(request.referrer)))
    return "Hello World - aula 2 - Jocemar!"
