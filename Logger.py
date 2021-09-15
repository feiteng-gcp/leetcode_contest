import logging, IO_Helper, traceback
import logging.config

def getLogger(logger_name):
    
    # try:    
    #     log_path = "logging/crawling_raw/{0}.log".format(logger_name)
    #     logging_file_path = 'logging.conf'
    #     logging.config.fileConfig(logging_file_path, defaults={'log_file_name':log_path})
    #     logger = logging.getLogger(log_path)
    #     val = 1 / 0
    # except Exception as err:
        # traceback.print_exc()
        # print('Swithching to root logger')
    log_file_name = 'logging/' + logger_name+ '.log'
    logger = logging.getLogger(log_file_name)
    logger.setLevel(logging.DEBUG)
    consoleHandler = logging.StreamHandler()
    fileHandler = logging.FileHandler(log_file_name)
    consoleHandler.setLevel(logging.DEBUG)
    fileHandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    consoleHandler.setFormatter(formatter)
    fileHandler.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(consoleHandler)
    logger.addHandler(fileHandler)
    # pass
    return logger