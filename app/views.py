from app.config import Config
from flask import render_template, flash, session, redirect, url_for, request, jsonify, send_file, Response
from werkzeug.urls import url_parse

import os
import pytz
import datetime
import json
import termcolor
import colorama
colorama.init(strip=False)
from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth
import traceback
import uuid
import google_auth_oauthlib,google
import pickle




import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

from app import server
from app.aws import AWSInstance

server.config.from_object(Config)
server.logger.setLevel(logging.DEBUG)
awsInstance = AWSInstance()



@server.route("/")
def hello():
    #server.logger.debug('Processing default request')
    return ("You have landed on the wrong page")

@server.route("/health")
def health():
    print("healthy!")
    return render_template('health.html')

