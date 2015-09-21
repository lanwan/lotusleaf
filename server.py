import os
import sys

import logging
from logging.handlers import TimedRotatingFileHandler
__loghandle = TimedRotatingFileHandler('listen_log.txt', when='D', interval=1, backupCount=5)
__loghandle.setFormatter( logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') )
logging.root.addHandler(__loghandle)

#import testhttpsvr
#testhttpsvr.run()

import testtornado
testtornado.run()



