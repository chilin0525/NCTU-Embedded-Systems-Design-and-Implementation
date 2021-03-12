import RPi.GPIO
import time

TRIGERping = 16
ECHOping   = 18

def gpio_setup():
    RPi.GPIO.setmode(RPi.GPIO.BOARD)
    RPi.GPIO.setup(TRIGERping, RPi.GPIO.OUT)
    RPi.GPIO.setup(ECHOping, RPi.GPIO.IN)

def hcsr04_setup():
    RPi.GPIO.output(TRIGERping,RPi.GPIO.HIGH)
    time.sleep(0.00001)
    RPi.GPIO.output(TRIGERping,RPi.GPIO.LOW)

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
        while(RPi.GPIO.input(ECHOping) == RPi.GPIO.LOW):
            print("bug")
            start = time.time()
        print("start")
        while(RPi.GPIO.input(ECHOping) == RPi.GPIO.HIGH):
            end  = time.time()
        print("distance is %.2f", sol(start,end,340.0))
    except:
        print("stop by ctrl-c")
    finally:    
        gpio_shutdown()
