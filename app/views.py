from app.config import Config
from flask import render_template
import colorama
colorama.init(strip=False)
import logging
from app.log import logger

from app import server
from app.aws import AWSInstance

server.config.from_object(Config)
server.logger.setLevel(logging.DEBUG)
awsInstance = AWSInstance()

@server.route("/")
def hello():
    logger.debug("You have landed on the main route")
    return ("You have landed on the main route")

@server.route("/health")
def health():
    logger.debug("healthy!")
    return render_template('health.html')


