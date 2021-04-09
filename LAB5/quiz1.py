import time
import picamera
import schedule 
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


schedule.every().day.at('13:40').do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
