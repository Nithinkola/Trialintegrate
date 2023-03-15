# This BaseClass is imported by test_fixturesData

import inspect
import logging

class BaseClass:
    def getLogger(self):

        # Remember these two lines below to get exact name of method to which logs belong to.
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # Below code gives BaseClass is file to which logs belong to.
        #logger = logging.getLogger(__name__)  # using __name__ will print testcase name to which logs belong to

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # takes file handler object nothing but location of logs
        logger.setLevel(logging.DEBUG)  # Present from logging.debug it will print o/p's.
                                        # logging.INFO means from logger.info it will print in o/p
        return logger


#Check test_fixturesData.py file its inheriting BaseClass.