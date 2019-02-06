用 usbip 轉發 raspberry pi 的 USB 鍵盤鼠標給 Arch Linux 的 PC
====================================================================

:id: usbip-forward-raspberrypi
:translation_id: usbip-forward-raspberrypi
:lang: zh
:date: 2019-02-07 02:14
:tags: linux, archlinux, raspberrypi, usbip, usb, forward
:issueid: 80

惠狐 :fref:`megumifox` 寫了篇 `用PulseAudio將電腦的聲音用手機放出來 <https://blog.megumifox.com/public/2019/02/06/%E7%94%A8pulseaudio%E5%B0%86%E7%94%B5%E8%84%91%E7%9A%84%E5%A3%B0%E9%9F%B3%E7%94%A8%E6%89%8B%E6%9C%BA%E6%94%BE%E5%87%BA%E6%9D%A5/>`_
，文末提到想知道我怎麼用樹莓派轉發 USB 的，於是寫篇文章記錄一下。

起因
----------

家裏有個裝了 Arch Linux ARM 的樹莓派3B 閒置着，裝了 Arch Linux ARM 偶爾插上電更新一下，
不過因爲性能實在不適合做別的事情於是一直在吃灰。某日和老婆看片的時候，鍵盤鼠標被長長的 USB
線扯着感覺很難受，於是偶發奇想，能不能利用一下樹莓派的多達 4 個 USB 2.0 端口接鼠標鍵盤呢，
這樣鼠標鍵盤就可以跟着樹莓派來回走，不用拖着長長的 USB 線了。

上網搜了一下， Linux 環境有個 usbip 工具正好能做到這個。原理也很直觀， usbip 能把 USB
端口上的數據包裝成 IP 協議通過網絡轉發出去，從而兩個網絡間相互聯通的電腦就可以遠程轉發 USB 了。
設置好的話，就像是一臺 PC 多了幾個位於樹莓派上的 USB 端口，插上樹莓派的 USB 設備統統作爲 PC
的設備。

這篇文章假設有一個裝了 Arch Linux 的 PC ，和一個裝了 Arch Linux ARM 的樹莓派，
並且兩者間能通過網絡互相訪問到。別的發行版上大概也可以這麼做，只是我沒有試過。 usbip
工具似乎普遍被發行版打包了，除此之外需要的也只是 Linux 內核提供好的功能而已。

設置 Arch Linux ARM 的樹莓派端
------------------------------------------------------------

假設樹莓派上面網絡已經設置妥當，開機插電就能自動聯網。接下來安裝 usbip 工具：

.. code-block:: console

    $ pacman -Syu usbip


接下來需要記錄一下樹莓派的 IP 地址：

.. code-block:: console

    $ ip addr
    3: wlan0: ......
    inet 192.168.0.117/24 brd 192.168.0.255 scope global noprefixroute wlan0
    ......

接下來，我給 udev 添加了一個規則，當插入 usb 設備的時候，執行我的腳本 usbipall.sh
把 usb 設備通過 usbip 共享出去：

.. code-block:: console

    $ cat /etc/udev/rules.d/usbipall.rules
    ACTION=="add", SUBSYSTEM=="usb", RUN+="/usr/bin/bash /usr/local/bin/usbipall.sh"

這個 rules 文件 `可以在我的 dotfiles 裏面找到 <https://github.com/farseerfc/dotfiles/blob/master/usbiprpi/usbipall.rules>`_ 。

然後規則調用的 usbipall.sh 我這麼寫的， `文件同樣在我的 dotfiles 裏面 <https://github.com/farseerfc/dotfiles/blob/master/usbiprpi/usbipall.sh>`_：

.. code-block:: bash

    #/bin/sh
    (
    allusb=$(usbip list -p -l)
    for usb in $allusb
    do
        busid=$(echo $usb | sed "s|#.*||g;s|busid=||g")
        if [[ $busid = "1-1.1" ]]
        then
            # ignoring usb ethernet
            continue
        fi
        echo "$(date -Iseconds): Exporting $busid"
        usbip bind --busid=$busid
    done
    ) >>/var/log/usbipall.log 2>&1

這個腳本做了這樣幾件事。

#. 調用 :code:`usbip list --local` 列出本地所有 usb 設備。
#. 針對每個設備：
    #. 取出它的 busid
    #. 判斷是不是樹莓派的 USB 以太網卡，不是的話繼續
    #. 通過 :code:`usbip bind --busid=` 命令把這個 usb 設備導出到網上
#. 最後把所有輸出記錄到 /var/log/usbipall.log 日誌裏面

樹莓派這邊設置就完成了。從此之後插入的 usb 設備就會統統導出出去。

這裏需要注意一下，啓用了 udev 規則之後，就沒法插鍵盤鼠標到樹莓派上控制它了……我都是從另一端 ssh
上樹莓派操作的。如果有什麼地方設置錯誤，可能需要把樹莓派的 SD 卡拔下來插到電腦上，刪除掉 rules
文件……

仔細檢查設置正確了之後，重新載入 udev 規則，或者重啓樹莓派：

.. code-block:: console

    # systemctl restart systemd-udevd

這樣樹莓派這邊就設置好了。


設置 Arch Linux 的 PC 端
------------------------------------------------------------

同樣假設 PC 這邊也已經聯網。接下來同樣安裝 usbip 工具：

.. code-block:: console

    $ pacman -Syu usbip

然後我寫了個小腳本去鏈接樹莓派端， `這個文件 usbiprpi3.sh 也在我的 dotfiles <https://github.com/farseerfc/dotfiles/blob/master/usbiprpi/usbiprpi3.sh>`_：

.. code-block:: bash

    #/bin/sh
    rpi3="192.168.0.117"

    modprobe vhci-hcd

    allusb=$(usbip list -p -r $rpi3 | cut -d":" -f1 -s | sed 's|^[ \t]*||;/^$/d')
    for busid in $allusb
    do
            if [[ $busid = "1-1.1" ]]
            then
                    # ignoring usb ethernet
                    continue
            fi
            echo "Attaching $busid"
            usbip attach --remote=$rpi3 --busid=$busid
    done

其中腳本第一行填入上面記錄下來的樹莓派的 IP 地址，接下來腳本做了這麼幾件事：

#. 用 modprobe 確認加載 vhci-hcd 通用虛擬鍵鼠驅動
#. 用 :code:`usbip list --remote=` 列出遠程設備上已經導出了的 USB 設備，取出他們的 busid
#. 對每個設備用 :code:`usbip attach` 接上該設備

然後就已經準備妥當，接下來是見證奇蹟的時刻：

.. code-block:: console

    $ sleep 10; sudo ./usbiprpi3.sh
    Attaching 1-1.4.3
    Attaching 1-1.4.1

因爲只有一套鍵盤鼠標，所以先 sleep 個 10 秒，在此期間快速把鍵鼠拔下來插到樹莓派的 USB 口上去。
如果對自己手速沒自信也可以把時間設長一點。然後用 root 權限執行 usbiprpi3.sh 。

一切正常的話，先能觀測插上樹莓派的鍵盤鼠標被樹莓派初始化了一下，比如鍵盤燈會亮，
然後這些設備會被導出出去，從而鍵盤燈滅掉，然後 10 秒等待結束後他們被遠程接到了 PC 端，
又會被初始化一下，同時 PC 端這邊會有上述 Attaching 的輸出。然後鍵盤鼠標就能像平常一樣用啦。

使用體驗
------------------------------------------------------------

因爲就是通過 IP 轉發 USB 嘛，所以就和普通地接 USB 的體驗差不多，當然前提是網絡環境足夠穩定。
在我家間隔 5 米到無線路由器的環境下，基本感覺不到網絡延遲的影響。
通過這種方式聊天上網應該和直接接 USB 設備完全一樣。本文就是在通過樹莓派轉發的前提下用鍵盤打字寫的。

不過如果網絡負載本身就很大的話，可能會一些延遲，比如我開着 OBS 直播打東方的時候，原本就手殘
的我感覺更加手殘了……

試過拿着樹莓派在房間到處走，走到無線信號覆蓋不到的地方， usbip 會斷掉，PC 上的現象就像是 USB
設備被拔下來了……所以如果無線網絡不穩的話，可能需要對上面腳本做個循環？不過那樣可能會用起來很彆扭吧。

以及，上述操作 usbip 是走 TCP 3240 端口，數據包大概完全沒有加密，所以考慮安全性的話，
最好還是在內網環境使用。不過轉念一想，萬一有別人接上了我導出出去的 USB ，也就是截獲我的鍵盤，
PC 這邊沒法 attach 設備了，應該馬上會發現吧，似乎對攻擊者也沒有什麼好處？我能控制他的鍵盤了耶~

