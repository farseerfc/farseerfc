我眼中的 Wayland 的是與非
=====================================

:slug: wayland-good-and-bad
:lang: zh
:date: 2015-02-15 22:45
:tags: linux, wayland, xorg

連着 `五六年了 <http://www.phoronix.com/scan.php?page=news_topic&q=Wayland&selection=20>`_
，每年都有人說 wayland_ 要來了， X11 即將壽終正寢了。
畢竟 X11 這個顯示服務器遠在 Linux 誕生之前就有了，歲數都比我大，歷史遺留問題
一大堆，安全性、擴展性都跟不上時代了。

.. _wayland: http://wayland.freedesktop.org/

看樣子 2015年的確像是 Wayland 終於能用了 
--------------------------------------------------------------------

根據 `Arch 的 Wiki <https://wiki.archlinux.org/index.php/Wayland>`_ 上跟蹤着的 wayland 進展，
`toolkit 方面 <https://wiki.archlinux.org/index.php/Wayland#GUI_libraries>`_ 
GTK+ 3, Qt 5, EFL, Clutter, SDL 等等的幾個圖形庫都完整支持 wayland 並且在 
archlinux 中默認啓用了。
`WM 和 DE 方面 <https://wiki.archlinux.org/index.php/Wayland#Window_managers_and_desktop_shells>`_
Gnome 3 已經有了實驗性支持， KDE 5 方面大部分 QT5 程序都已經支持了就等 kwin_wayland
作爲 Session Manager 成熟起來，E19 很早就支持了，以及目前 wayland 上的 
WM/Compositor 除了作爲實驗性參考實現的 weston 和上述 DE 之外，還有不少
`有趣 <https://github.com/Cloudef/loliwm>`_ 又
`好玩 <https://github.com/evil0sheep/motorcar>`_ 的新 WM 。
另外各個發行版支持程度方面 Fedora 21 上的 Gnome 3 也有實驗性支持了。
總體上可以說從 Xorg 遷移到 Wayland 的準備已經基本就緒了。

於是問題就是 **我們是否應該換到 Wayland** 
--------------------------------------------------------------------

換句話說， **wayland 相比較於現在的 Xorg 來說到底有什麼優勢** ？