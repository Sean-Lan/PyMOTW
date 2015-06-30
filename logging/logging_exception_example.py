import logging
import os
logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'),
                    level = logging.DEBUG)
log = logging.getLogger('root')
try:
    raise Exception, 'this is an exception'
except:
    log.exception('exception_log')
