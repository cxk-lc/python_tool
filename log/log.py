# -*- coding: utf-8 -*-

import logging
from logging.config import fileConfig

fileConfig('logging.conf')
logger = logging.getLogger('file')  # 同时输出到文件与控制台

if __name__ == '__main__':
    logger.debug('test')
