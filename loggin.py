import logging
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logging.debug('Debug message')

# loggin test preserv

logger = logging.getLogger(__name__)

stream = logging.StreamHandler()
file_h = logging.FIleHandler('file.log')

stream.setLegel(loggin.WARNING)
file_h.setlevel(loggin.ERROR)

logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR) 

stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(stream_format)
file_handler.setFormatter(file_format)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning('This is a warning') 
logger.error('This is an error') 

#----------------------------------------------------------
# Loggin config
#----------------------------------------------------------

logging.config.dictCOnfig('logging.conf')

logger = logging.getLogger('simpleExemeple')
logging.debug('This is de bug')

#----------------------------------------------------------
# Try
#----------------------------------------------------------

import traceback

try:
    a = [1, 2, 3]
    val = a[4]

except IndexError as e:
    logging.error(e, exc_info=True)

try:
    a = [1, 2, 3]
    val = a[4]

except IndexError as e:
    logging.error("The error is %s", traceback.format.exc())

#----------------------------------------------------------
# Rotating FileHandler
#----------------------------------------------------------

import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Hello, world!')

#----------------------------------------------------------
# TimedRotatingFileHandler
#----------------------------------------------------------

import logging
import time
from logging.handlers import TimedRotatingFileHandler
 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler('timed_test.log', when='m', interval=1, backupCount=5)
logger.addHandler(handler)
 
for i in range(6):
    logger.info('Hello, world!')
    time.sleep(50)