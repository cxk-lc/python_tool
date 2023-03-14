import schedule
import time


"""
可以通过装饰器 @repeat() 将定时任务直接装饰在任务函数上

在任务函数中使用 schedule.cancel_job() 函数来控制取消任务

可以在定时器后面加.tag()来打标签，然后使用 schedule.clear() 指定标签取消任务

使用 schedule.run_all() 可立即触发所有任务（一般用于测试）
"""


def job():
    print("I'm working...")
    print(time.strftime('%H:%M:%S', time.localtime()))


schedule.every().seconds.do(job)  # 每 x 秒执行一次
schedule.every().seconds.unit().do(job)  # 每 x 秒执行一次直到 xx 时间为止，datetime相关的时间对象、字符串
schedule.every().minutes.do(job)  # 每 x 分钟执行一次
schedule.every().hour.do(job)  # 每 x 小时执行一次
schedule.every().day.at("10:30").do(job)  # 每 x 天的 xx 时间执行一次
schedule.every().to().minutes.do(job)  # 每 x to y 分钟执行一次
schedule.every().monday.do(job)  # 每个周一执行一次
schedule.every().minute.at(":00").do(job)  # 每分钟的 xx 秒执行一次

while True:
    schedule.run_pending()  # 按顺序触发所有的定时任务
    time.sleep(1)

# @repeat(every().second, 'World')
# @repeat(every().minute, 'Mars')
# def hello(planet):
#     print('Hello', planet)
#
#
# while True:
#     run_pending()

