# _*_ coding:utf-8 _*_
import logging
import logging.handlers
import logging.config
import os
import configparser
import re


class CustomLogger:
    def __init__(self, config_path):
        self.load_conf(config_path)

        # loading log config
        logging.config.fileConfig('logger_config.conf')
        # Create a logger
        self.logger = logging.getLogger()

    @staticmethod
    def load_conf(config_path):
        # Read the configuration file
        config = configparser.ConfigParser()
        config.read(config_path)

        # Get fileHandler conf
        file_handler = config['handlers']['keys'].split(',')[0]
        handler_file_handler_conf = config.get(f'handler_{file_handler}', 'args')

        CustomLogger.path_check(handler_file_handler_conf)

    @staticmethod
    def path_check(handler_file_handler_conf):
        # Check if the path where the log files are stored exists.
        log_file_path, file_open_mode = \
            tuple(handler_file_handler_conf.strip('()').split(','))
        log_file_path = re.sub(r"['\"]", "", log_file_path)
        log_file_dirname = os.path.dirname(log_file_path)
        print(log_file_dirname)
        if not os.path.exists(log_file_dirname):
            os.makedirs(log_file_dirname)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


# usage example
if __name__ == "__main__":
    # path to the configuration file
    path = './logger_config.conf'
    # create an instance of CustomLogger, passing the configuration file path
    logger = CustomLogger(path)

    # output log messages
    logger.info('this is an info message.')
    logger.debug('this is a debug message.')
    logger.warning('this is a warning message.')
    logger.error('this is an error message.')
    logger.critical('this is a critical message.')
