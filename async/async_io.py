import asyncio
import time


# 事件循环
# 在一个任务列表中轮询所有的任务，直到全部完成。
"""
async def func1():
    time.sleep(2)
    print(f'协程任务1：{time.ctime()}')


async def func2():
    time.sleep(1)
    print(f'协程任务2：{time.ctime()}')


task_list = [func1(), func2()]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(task_list))
loop.close()

python 3.7以上版本，可省略手动创建事件循环
asyncio.run(task_list)
"""


