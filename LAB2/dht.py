# import time
# import RPi.GPIO as GPIO

# """
# VCC: pin2
# GND: pin6
# data: pin16
# """

# dataPin = 16

# def gpio_init():
#     GPIO.setmode(GPIO.BOARD)

# def dht11_init():
#     GPIO.setup(dataPin, GPIO.HIGH)
#     time.sleep(0.05)
#     GPIO.setup(dataPin,GPIO.LOW)
#     time.sleep(0.02)
#     GPIO.setup(dataPin, GPIO.HIGH)

# def dht11_res():
#     GPIO.set

# def readdata():
#     pass

# """
# RH int + dec
# T  int + dec
# checksum
# """

# if __name__=="__main__":
#     gpio_init()
#     dht11_init()
#     (RH_int,RH_dec,T_int,T_dec,checksum) = readdata()


import dht11 as dht
import RPi.GPIO as GPIO

dataPin = 16


def gpio_init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

def dht_init():
    instance = dht11.DHT11(pin=dataPin)
    return instance

if __name__ == "__main__":
    try:
        gpio_init()
        data = dht_init()
        if(data.is_valid()):
            print("Temp:%d, Hum:%d", data.temperature, data.humidity)
        else:
            print("error of reading data")
    except:
        print("error")
    finally:
        GPIO.cleanup()
