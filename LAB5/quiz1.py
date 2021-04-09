import time
import picamera
from schedule import *
from datetime import date

def job():
    with picamera.PiCamera() as camera:
        camera.start_preview()
        try:
            for i, filename in enumerate(camera.capture_continuous('{counter:03d}.jpg')):
                print(filename)
                time.sleep(1)
                if i == 59:
                    break
        finally:
            camera.stop_preview()


sched = Scheduler()
sched.start()

exec_date = date(2021, 4, 9, 13, 34, 30)

job = sched.add_date_job(my_job, exec_date, ['text'])
