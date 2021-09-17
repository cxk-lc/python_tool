# -*- coding: utf-8 -*-
import time
from functools import wraps


def timing(func):
    @wraps(func)
    def inner(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(f'执行耗时：{t2 - t1}s')
        return res

    return inner()
