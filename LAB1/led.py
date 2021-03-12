import RPi.GPIO as GPIO
import time

LED_PIN = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        print("LED is on")
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        print("LED is off")
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")
finally:
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
