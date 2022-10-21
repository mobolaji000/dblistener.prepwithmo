import requests
import threading
import time
import os
import traceback
from log import logger

def start_runner():
    def start_loop():
        not_started = True
        while not_started:
            logger.debug('In start loop')
            time.sleep(5)
            try:
                url_to_start_reminder = os.environ.get("url_to_start_reminder")
                r = requests.get(url_to_start_reminder)
                logger.debug("Status code is: "+str(r.status_code))
                if r.status_code != 500 and r.status_code != 504:
                    logger.debug('Server started, quiting start_loop')
                    not_started = False
                logger.debug('Status code is: '+str(r.status_code))
            except Exception as e:
                # logger.debug(e)
                # traceback.logger.debug_exc()
                logger.exception('There has been an exception. Server not yet started')
            time.sleep(5)

    logger.debug('Started runner')
    thread = threading.Thread(target=start_loop)
    thread.start()

# running the flask db option breaks this multithreading code to ping url_to_start_reminder
start_runner()
from app import server


