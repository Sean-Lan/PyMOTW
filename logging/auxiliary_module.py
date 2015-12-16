import logging

# create logger
module_logger = logging.getLogger('spam_application.auxiliary')
# fh = logging.FileHandler('spam.log')
# formatter = logging.Formatter('[child]%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
# module_logger.addHandler(fh)

class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger('spam_application.auxiliary.Auxiliary')
        self.logger.info('creating an instance of Auxiliary')
    def do_something(self):
        self.logger.info('doing something')
        a = 1 + 1
        self.logger.info('done doing something')

def some_function():
    module_logger.info('received a call to "some_function"')
