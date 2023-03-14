from apscheduler import events
from apscheduler.schedulers.blocking import BlockingScheduler, Event
from datetime import datetime, date


def job(param1='param1'):
    """
    作为 APScheduler 的最小执行单元，创建 Job 对象时指定的任务函数
    """
    print(param1)
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# BlockingScheduler
scheduler = BlockingScheduler()

"""
Job 对象的一些参数说明：

func：Job执行的函数

trigger：apscheduler定义的触发器，确定轮询时间

args：Job执行函数需要的位置参数

kwargs：Job执行函数需要的关键字参数

id： 指定 job 的唯一id

name： job 的名字

misfire_grace_time：Job的延迟执行时间（单位秒，默认为 undefined，可设置为None表
示允许任何时长的延时），例如Job的计划执行时间是21:00:00，但因服务重启或其他原因
导致21:00:31才执行，如果设置此key为40,则该job会继续执行，否则将会丢弃此job。

coalesce：Job是否合并执行，是一个bool值。例如scheduler停止20s后重启启动，而job的
触发器设置为5s执行一次，因此此job错过了4个执行时间，如果设置为是，则会合并到一次
执行，否则会逐个执行

max_instances：执行此job的最大实例数，executor执行job时，根据job的id来计算执行次
数，根据设置的最大实例数来确定是否可执行

next_run_time：Job下次的执行时间，创建Job时可以指定一个时间[datetime],不指定的话
则默认根据trigger获取触发时间

jobstore: 用于存储作业的作业存储区别名。

executor：apscheduler定义的执行器，根据 name 获取对应 job 的执行器执行

**trigger_args：Trigger 触发器相关参数
"""

"""
Trigger 触发器目前有三种：
指定时间的DateTrigger
指定间隔时间的IntervalTrigger
类似 linux crontab 的 CronTrigger。
"""

"""
触发器参数：date

run_data (date|datetime): 指定一个执行时间，只执行一次
"""

# scheduler.add_job(job, 'date', run_date=date(2023, 3, 14))
# scheduler.add_job(job, 'date', run_date=datetime(2023, 3, 14, 12, 17, 0),
#                   args=['触发器参数 date'])
"""
触发器参数 date
2023-03-14 12:17:00
"""

"""
触发器参数：interval
间隔调度

weeks (int): 间隔几周
days (int): 间隔几天
hours (int): 间隔几小时
minutes (int): 间隔几分钟
seconds (int): 间隔多少秒
start_date (datetime|str): 开始日期
end_date (datetime|str): 结束日期
timezone (datetime.tzinfo|str): 时区
"""

# scheduler.add_job(job, 'interval', seconds=2,
#                   args=['触发器参数：interval， 时间间隔: 2秒'])

"""
触发器参数：cron

year (int|str): 4-digit year -（表示四位数的年份，如2008年）

month (int|str): month (1-12) -（表示取值范围为1-12月）

day (int|str): day of the (1-31) -（表示取值范围为1-31日）

week (int|str): ISO week (1-53) -（格里历2006年12月31日可以写成2006年-W52-7（扩
展形式）或2006W527（紧凑形式））

day_of_week (int|str): number or name of weekday (0-6 or mon,tue,wed,thu,fri,
sat,sun) – （表示一周中的第几天，既可以用0-6表示也可以用其英语缩写表示）

hour (int|str): hour (0-23) – （表示取值范围为0-23时）
minute (int|str): minute (0-59) – （表示取值范围为0-59分）
second (int|str): second (0-59) – （表示取值范围为0-59秒）

start_date (datetime|str): earliest possible date/time to trigger on (inclusive) 
– （表示开始时间）
end_date (datetime|str): latest possible date/time to trigger on (inclusive) – 
（表示结束时间）

timezone (datetime.tzinfo|str): time zone to use for the date/time calculations 
(defaults to scheduler timezone) -（表示时区取值）
"""

# 6-8,11-12月第三个周五 00:00, 01:00, 02:00, 03:00运行
scheduler.add_job(job, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
# 每周一到周五运行 直到2024-05-30 00:00:00
scheduler.add_job(job, 'cron', day_of_week='mon-fri', hour=5, minute=30,
                  end_date='2024-05-30')

# scheduler.start()  # 开始任务
# test_job = scheduler.add_job()
# test_job.remove()  # 通过任务实例移除任务
# scheduler.pause()  # 暂停未运行的任务  也可在启动调度器的时候，通过 paused=True 将任务直接设置成暂停状态
# scheduler.pause_job()  # 指定 job_id 暂停任务
# scheduler.resume()  # 恢复被暂停的任务
# scheduler.resume_job()  # 指定 job_id 恢复任务
# scheduler.get_jobs()  # 获取所有的任务，返回列表
# scheduler.get_job()  # 获取指定 job_id 任务
# scheduler.modify_job()  # 指定 job_id 修改任务
# scheduler.remove_job()  # 指定 job_id 移除任务
# scheduler.reschedule_job()  # 指定 job_id 重新创建任务（修改触发器，重新计算时间）


print(scheduler.__class__)

"""
Executor 执行器

Executor在scheduler中初始化，另外也可通过scheduler的add_executor动态添加Executor。
每个executor都会绑定一个alias，这个作为唯一标识绑定到Job，在实际执行时会根据Job
绑定的executor找到实际的执行器对象，然后根据执行器对象执行Job。

executors.asyncio：同步io，阻塞
executors.gevent：io多路复用，非阻塞
executors.pool: 线程ThreadPoolExecutor和进程ProcessPoolExecutor
executors.twisted：基于事件驱动
"""

"""
Jobstore 作业存储

Jobstore在scheduler中初始化，另外也可通过scheduler的add_jobstore动态添加Jobstore。
每个jobstore都会绑定一个alias，scheduler在Add Job时，根据指定的jobstore在scheduler
中找到相应的jobstore，并将job添加到jobstore中。作业存储器决定任务的保存方式， 默
认存储在内存中（MemoryJobStore），重启后就没有了。

jobstores.memory：内存
jobstores.mongodb：存储在mongodb
jobstores.redis：存储在redis
jobstores.rethinkdb：存储在rethinkdb
jobstores.sqlalchemy：支持sqlalchemy的数据库如mysql，sqlite等
jobstores.zookeeper：zookeeper

不同的任务存储器可以在调度器的配置中进行配置
"""

"""
Event 事件

Event是APScheduler在进行某些操作时触发相应的事件，用户可以自定义一些函数来监听这
些事件，当触发某些Event时，做一些具体的操作。常见的比如。Job执行异常事件 
EVENT_JOB_ERROR。Job执行时间错过事件 EVENT_JOB_MISSED。

EVENT_SCHEDULER_STARTED
EVENT_SCHEDULER_START
EVENT_SCHEDULER_SHUTDOWN
EVENT_SCHEDULER_PAUSED
EVENT_SCHEDULER_RESUMED
EVENT_EXECUTOR_ADDED
EVENT_EXECUTOR_REMOVED
EVENT_JOBSTORE_ADDED
EVENT_JOBSTORE_REMOVED
EVENT_ALL_JOBS_REMOVED
EVENT_JOB_ADDED
EVENT_JOB_REMOVED
EVENT_JOB_MODIFIED
EVENT_JOB_EXECUTED
EVENT_JOB_ERROR
EVENT_JOB_MISSED
EVENT_JOB_SUBMITTED
EVENT_JOB_MAX_INSTANCES
"""


def my_listener(event):
    if event.exception:
        print('The job crashed :(')
    else:
        print('The job worked :)')


# 监听指定时间，时间发生后执行 my_listener
scheduler.add_listener(my_listener,
                       events.EVENT_JOB_EXECUTED | events.EVENT_JOB_ERROR)
