import RPi.GPIO
import time

TRIGER = 16
ECHO   = 18

def gpio_setup():
    RPi.GPIO.setmode(RPi.GPIO.BOARD)
    RPi.GPIO.setup(TRIGER, RPi.GPIO.OUT)
    RPi.GPIO.setup(ECHO, RPi.GPIO.IN)

def hcsr04_setup():
    RPi.GPIO.output(TRIGER,1)
    time.sleep(0.00001)
    RPi.GPIO.output(TRIGER,0)

def sol(start,end,speed):
    speed /= 2.0
    time = float(end-start)
    return speed*time*100.0

def gpio_shutdown():
    RPi.GPIO.cleanup()

if __name__=="__main__":
    print("go")
    try:
        gpio_setup()
        hcsr04_setup()
        print("gogo")
        while(RPi.GPIO.input(ECHO) == RPi.GPIO.LOW):
            start = time.time()
        print("start")
        while(RPi.GPIO.input(ECHO) == RPi.GPIO.HIGH):
            end  = time.time()
        print("distance is %.2f", sol(start,end,340.0))
    except:
        print("stop by ctrl-c")
    finally:    
        gpio_shutdown()
