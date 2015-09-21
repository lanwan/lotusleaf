import os
import site


import logging
from logging.handlers import TimedRotatingFileHandler
__loghandle = TimedRotatingFileHandler(os.path.join(os.getcwd(), 'lotusleaf_log.txt'), when='D', interval=1, backupCount=5)
__loghandle.setFormatter( logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') )
logging.root.addHandler(__loghandle)


__sites_path = os.path.join(os.getcwd(), 'sites//')
logging.info(__sites_path)
if os.path.exists(__sites_path):
	site.addsitedir(__sites_path)
else:
	logging.warn("%s does not exists!",__sites_path)

#import testhttpsvr
#testhttpsvr.run()

import testweb
testweb.run()



