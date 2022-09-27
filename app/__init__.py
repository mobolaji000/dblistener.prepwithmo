from flask import Flask

from app.config import Config

server = Flask(__name__)
server.config.from_object(Config)


