import logging
import os
import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler(str('logs/')+str(os.path.basename(__file__)[:-3])+'-'+str(datetime.datetime.now().strftime('%Y-%m-%d'))+'.log','a')

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)