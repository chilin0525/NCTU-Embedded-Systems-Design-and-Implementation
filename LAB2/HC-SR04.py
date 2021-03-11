import Rpi.GPIO
import time

TRIGER = 16
ECHO   = 18

def function gpio_setup():
    pass

def function hcsr04_setup():
    Rpi.GPIO.output(TRIGER,1)
    time.sleep(0.00001)
    Rpi.GPIO.output(TRIGER,0)

def function sol(start,end):
    speed /= 2
    return speed*(end-start)*100

if __name__=="__main__":

