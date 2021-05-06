# LAB7

## Eddystone

* whether blueteeth of device enable or not:
    ```hciconfig -a hci0 features | grep LE```: 應該要有 LE support

**quiz1**:
    * start: ```sudo ./advertise-url -u http://nctu.0711282```
    * stop: ```sudo ./advertise-url -s```

**quiz2**:
    * start: ```sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 06 1A FF 00 4C 02 15 E2 0A 39 F4 73 F5 4B C4 A1 2F 00 00 00 71 12 82 00 00 00 00 C8 00```
    * stop: ```sudo ./ibeacon -z```