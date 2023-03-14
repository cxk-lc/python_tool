import time

from timeloop import Timeloop
from datetime import timedelta

tl = Timeloop()


@tl.job(interval=timedelta(seconds=2))
def test_job_print_time():
    print(f'now is {time.ctime()}')


tl.start()
time.sleep(5)
tl.stop()

"""
[2023-03-14 15:55:19,147] [timeloop] [INFO] Starting Timeloop..
[2023-03-14 15:55:19,147] [timeloop] [INFO] Registered job <function test_job_print_time at 0x000002509AFBC670>
[2023-03-14 15:55:19,147] [timeloop] [INFO] Timeloop now started. Jobs will run based on the interval set
now is Tue Mar 14 15:55:21 2023
now is Tue Mar 14 15:55:23 2023
[2023-03-14 15:55:24,154] [timeloop] [INFO] Stopping job <function test_job_print_time at 0x000002509AFBC670>
[2023-03-14 15:55:24,154] [timeloop] [INFO] Timeloop exited.
"""
