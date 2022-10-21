from app.config import Config
from flask import render_template
import colorama
colorama.init(strip=False)

import logging
import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler(str('logs/')+'logs'+'-'+str(datetime.datetime.now().strftime('%Y-%m-%d---%H-%M'))+'.log','a')

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)#

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

from app import server
from app.aws import AWSInstance
from app.rq_worker_setup import RQWorkerSetup

server.config.from_object(Config)
server.logger.setLevel(logging.DEBUG)
awsInstance = AWSInstance()

@server.route("/")
def hello():
    import os
    for name, value in os.environ.items():
        print("{0}: {1}".format(name, value))
    RQWorkerSetup()
    logger.debug("You have landed on the main route")
    return ("You have landed on the main route")

@server.route("/health")
def health():
    logger.debug("Container is up and setup was completed successfully!")
    return render_template('health.html')


