from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

from app.config import Config

server = Flask(__name__)
server.config.from_object(Config)

db = SQLAlchemy(server,engine_options={"pool_pre_ping": True},session_options={'expire_on_commit': False},metadata=metadata)

from app import views


