# LAB5

* VNC:

    * 此次 LAB 需要 VNC 遠端桌面, 設定 VNC :

        ```
        桌面 --> Raspi Config --> interface --> VNC
        ```

    * 用 VNC 連進去後到 VNC perfermence --> options --> enalbe direct mode

* pi camera

    * 測試相機能否正常拍照:

        ```
        raspistill -n -t 3000 -o test.png -e png -w 640 -h 480
        ```

    * 記得開啟 ras pi 的 camera, 找 camera 然後 enable:

        ```
        $ raspi-config
        ```

* 此次 LAB 後半段需要串流網頁, 助教提供的程式碼是使用 flask, 所以複製時不要亂動資料夾全部一起複製

