# GPIO

check gpio:

```
pinout
```

## GPIO.setmode

* ```GPIO.setmode(GPIO.BOARD)``` : 指定為板子上的 physical pins 號碼
* ```GPIO.setmode(GPIO.BCM)``` : 指定為 GPIO 的號碼

## GPIO.setup

* ```GPIO.setup(port_or_pin, GPIO.IN)```
* ```GPIO.setup(port_or_pin, GPIO.OUT)```

## GPIO.output

* ```GPIO.output(port_or_pin, 1)```
* ```GPIO.output(port_or_pin, HIGH)```
* ```GPIO.output(port_or_pin, 0)```
* ```GPIO.output(port_or_pin, LOW)```

## GPIO.clearup

* ```GPIO.cleanup()```
