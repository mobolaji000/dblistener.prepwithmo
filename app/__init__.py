from flask import Flask
from app import views

from app.config import Config

server = Flask(__name__)
server.config.from_object(Config)#


