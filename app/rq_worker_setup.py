from redis import Redis
from rq import Queue
from dblistener import DBListener#
import os
from app import db
from sqlalchemy.sql import text
from app.queries import student_table_trigger_text,tutor_table_trigger_text,lead_table_trigger_text,prospect_table_trigger_text

q = Queue(connection=Redis(host='redis', port=6379, decode_responses=True,password=os.environ.get('REDIS_PASSWORD')),default_timeout=-1)
result = q.enqueue(DBListener(os.environ.get('psycopg_url'), os.environ.get('psycopg_db'), os.environ.get('psycopg_port'), os.environ.get('dbUserName'),os.environ.get('dbPassword')).dblisten)



try:
    with db.engine.connect() as con:
        con.execute(text(student_table_trigger_text))
        con.execute(text(tutor_table_trigger_text))
        con.execute(text(lead_table_trigger_text))
        con.execute(text(prospect_table_trigger_text))
except:
    db.session.rollback()
    raise
finally:
    db.session.close()