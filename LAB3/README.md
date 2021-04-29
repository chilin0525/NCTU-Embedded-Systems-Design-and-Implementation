# set up

## enable I2C on rpi

```
sudo raspi-config
```

and select interfacing options

check :

```
sudo ls -al /dev/*i2c*
```

```
sudo i2cdetect -y 1
```

```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: 30 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- 53 -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- 69 -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- 77 
```

## ADXL34x


spec 上忘了在哪裡看到 [Adafruit_Python_ADXL345](https://github.com/adafruit/Adafruit_Python_ADXL345) 這個套件已經過時, 在這邊使用 [Adafruit_CircuitPython_ADXL34x](https://github.com/adafruit/Adafruit_CircuitPython_ADXL34x) 較佳

* install

    ```shell
    sudo pip3 install adafruit-circuitpython-ADXL34x
    ```