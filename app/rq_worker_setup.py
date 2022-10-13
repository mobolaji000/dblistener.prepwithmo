from redis import Redis
from rq import Queue
from dblistener import DBListener#
import os

q = Queue(connection=Redis(host='redis', port=6379, decode_responses=True,password=os.environ.get('REDIS_PASSWORD')),default_timeout=-1)
result = q.enqueue(DBListener(os.environ.get('psycopg_url'), os.environ.get('psycopg_db'), os.environ.get('psycopg_port'), os.environ.get('dbUserName'),os.environ.get('dbPassword')).dblisten)
