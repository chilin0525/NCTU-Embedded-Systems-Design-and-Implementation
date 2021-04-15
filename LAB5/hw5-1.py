import time
import picamera
import schedule

def job():
    with picamera.PiCamera() as camera:
        camera.start_preview()
        try:
            for i, filename in enumerate(camera.capture_continuous('image{counter:02d}.jpg')):
                print(filename)
                time.sleep(1)
                if i == 9:
                    break
        finally:
            camera.stop_preview()


schedule.every().day.at("00:27").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
