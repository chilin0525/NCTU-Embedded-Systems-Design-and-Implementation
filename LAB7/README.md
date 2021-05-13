# LAB7

## Eddystone

* whether blueteeth of device enable or not:
    ```hciconfig -a hci0 features | grep LE```: 應該要有 LE support

**quiz1**:
    * start: ```sudo ./advertise-url -u http://nctu.0711282```
    * stop: ```sudo ./advertise-url -s```

    * sudo hcitool -i hci0 cmd 0x08 0x0008 1a 02 01 1a 03 03 aa fe 12 16 aa fe 10 ed 02 6e 63 74 75 2e 30 37 31 31 32 38 32 00 00 00 00 00 00 00 00 00 00 00




**quiz2**:
    * sudo hciconfig hci0 up
    * sudo hciconfig hci0 leadv 3
    * sudo hciconfig hci0 noscan
    * start: ```sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 06 1A FF 00 4C 02 15 E2 0A 39 F4 73 F5 4B C4 A1 2F 00 00 00 71 12 82 00 00 00 00 C8 00```
    * stop: ```sudo ./ibeacon -z```

    * sudo ./ibeacon -u 00000000000000000000000000711282 -M 0 -m 0