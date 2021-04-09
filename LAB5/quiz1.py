import time
import picamera
import schedule
import datetime

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


print(datetime.datetime.now().date, datetime.datetime.now().month,
      datetime.datetime.now().day, datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second)
