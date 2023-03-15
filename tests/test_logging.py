# Importance of Filehandler in logging test

import logging

def test_loggingDemo():

    logger = logging.getLogger(__name__)    # using __name__ will print testcase name to which logs belong to

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)     # takes file handler object nothing but location of logs

    logger.setLevel(logging.INFO)   # from logger.info it will print in o/p
    logger.debug("A debug statement is executed.")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has occured")
    logger.critical("Critical issue")

# After you run this logfile.log is created. Open it and check.