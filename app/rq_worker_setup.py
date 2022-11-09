from redis import Redis
from rq import Queue
from app.dblistener import DBListener#
import os
from app import db
from sqlalchemy.sql import text
from app.queries import student_table_trigger_text,tutor_table_trigger_text,lead_table_trigger_text,prospect_table_trigger_text

import logging
import datetime
import pytz

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()#
file_handler = logging.FileHandler(str('logs/')+'logs'+'-'+str(pytz.timezone('US/Central').localize(datetime.datetime.now()).strftime('%Y-%m-%d---%H-%M'))+'.log','a')

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

class RQWorkerSetup():
    def __init__(self):
        q = Queue(connection=Redis(host='redis', port=6379, decode_responses=True,password=os.environ.get('REDIS_PASSWORD'),health_check_interval=10,socket_connect_timeout=5,retry_on_timeout=True,socket_keepalive=True),default_timeout=-1)
        result = q.enqueue(DBListener(os.environ.get('psycopg_url'), os.environ.get('psycopg_db'), os.environ.get('psycopg_port'), os.environ.get('DBUSERNAME'),os.environ.get('DBPASSWORD')).dblisten)

        try:
            with db.engine.connect() as con:
                con.execute(text(student_table_trigger_text))
                con.execute(text(tutor_table_trigger_text))
                con.execute(text(lead_table_trigger_text))
                con.execute(text(prospect_table_trigger_text))
            logger.info("Triggers to listen to tables executed successfully")
        except Exception as e:
            db.session.rollback()
            logger.exception("Exception in executing triggers")
            raise e
        finally:
            db.session.close()
