import RPi.GPIO as GPIO
import time

tripin   = 16
echopin  = 18

def gpio_setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(tripin, GPIO.OUT)
    GPIO.setup(echopin, GPIO.IN)

def hcsr04_setup():
    GPIO.output(tripin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(tripin, GPIO.LOW)

def sol(start,end,speed):
    speed /= 2.0
    time = float(end-start)
    return speed*time*100.0

def gpio_shutdown():
    GPIO.cleanup()

if __name__=="__main__":
    print("go")
    try:
        gpio_setup()
        hcsr04_setup()
        print("gogo")
        while(GPIO.input(echopin) == GPIO.LOW):
            print("bug")
            start = time.time()
        print("start")
        while(GPIO.input(echopin) == GPIO.HIGH):
            end  = time.time()
        print("distance is %.2f", sol(start,end,340.0))
    except:
        print("stop by ctrl-c")
    finally:    
        gpio_shutdown()
