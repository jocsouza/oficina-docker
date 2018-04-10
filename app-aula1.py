import logging
from flask import Flask, request
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.error(('The referrer was {}'.format(request.referrer)))
    return "Hello World - aula 1 - Jocemar!"
