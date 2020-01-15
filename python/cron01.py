###리눅스에서만 가능

from apscheduler.schedulers.blocking import BlockingScheduler
import time

def exec_interval() : # 일정시간 간격으로 수행
    print("hello world ")

def exec_cron():
    str = time.strftime('%c', time.localtime(time.time())) #strftime : time을 str 형태로 변환 
    print("cron:", str)

sched = BlockingScheduler() # 단일 스케줄러. 하나의 프로세서가 돌아갈 떄 사용 
#5초 간격으로 exec_interval()함수 호출하기 
#sched.add_job(exec_interval, 'interval', seconds=60)

sched.add_job(exec_cron, 'cron', minute="*", second="10, 30")
sched.start()


