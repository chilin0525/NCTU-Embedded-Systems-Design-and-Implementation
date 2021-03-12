import RPi.GPIO as GPIO
import time
import cv2 as cv

tripin = 16
echopin = 18
led = 12


def gpio_setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(tripin, GPIO.OUT)
    GPIO.setup(echopin, GPIO.IN)
    GPIO.setup(led, GPIO.OUT)


def hcsr04_setup():
    GPIO.output(tripin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(tripin, GPIO.LOW)


def sol(start, end, speed):
    speed /= 2.0
    time = float(end-start)
    return speed*time*100.0


def slow():
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(led, GPIO.LOW)


def slow():
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(led, GPIO.LOW)


def gpio_shutdown():
    GPIO.cleanup()


if __name__ == "__main__":
    while(1):
        gpio_setup()
        hcsr04_setup()
        while(GPIO.input(echopin) == GPIO.LOW):
            start = time.time()
        while(GPIO.input(echopin) == GPIO.HIGH):
            end = time.time()
        distance = sol(start, end, 340.0)
        print("distance is " + str(distance))
        if cv.waitKey(0) & 0xFF == ord('q'):
            break
    
    gpio_shutdown()
