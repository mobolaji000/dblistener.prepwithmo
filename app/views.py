from app.config import Config
from flask import render_template
import os
import colorama
colorama.init(strip=False)



import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler(str('logs/')+str(os.path.basename(__file__)[:-3])+'.log','a')

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

from app import server
from app.aws import AWSInstance

server.config.from_object(Config)
server.logger.setLevel(logging.DEBUG)#
awsInstance = AWSInstance()



@server.route("/")
def hello():
    #server.logger.debug('Processing default request')
    logger.debug("You have landed on the wrong page")
    return ("You have landed on the wrong page")

@server.route("/health")
def health():
    print("healthy!")
    return render_template('health.html')


