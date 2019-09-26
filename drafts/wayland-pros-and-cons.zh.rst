我眼中的 Wayland 的是與非
=====================================

:slug: wayland-pros-and-cons
:translation_id: wayland-pros-and-cons
:lang: zh
:date: 2015-03-21 22:45
:tags: linux, wayland, xorg
:series: compositor and wayland

.. contents::

.. panel-default::
	:title: Wayland

	.. image:: {static}/images/wayland.png
	  :alt: Wayland

連着有 `五六年了 <http://www.phoronix.com/scan.php?page=news_topic&q=Wayland&selection=20>`_
，每年都有人說 Wayland_ 要來了， X11 即將壽終正寢了。
畢竟 X11 這個顯示服務器遠在 Linux 誕生之前就有了，歲數都比我大（我出生於X11R3和X11R4之間），
歷史遺留問題一大堆，安全性、擴展性都跟不上時代了。

.. _Wayland: http://wayland.freedesktop.org/


看樣子 2016 年的確像是 Wayland 終於能用了 
--------------------------------------------------------------------

根據 `Arch 的 Wiki <https://wiki.archlinux.org/index.php/Wayland>`_
上跟蹤着的 Wayland 進展，
`toolkit 方面 <https://wiki.archlinux.org/index.php/Wayland#GUI_libraries>`_
GTK+ 3, Qt 5, EFL, Clutter, SDL 等等的幾個圖形庫都完整支持 Wayland 並且在 archlinux
中默認啓用了。
`WM 和 DE 方面 <https://wiki.archlinux.org/index.php/Wayland#Window_managers_and_desktop_shells>`_
Gnome 3 已經有了實驗性支持， KDE 5 方面大部分 QT5 程序都已經支持了就等 kwin_wayland
作爲 Session Manager 成熟起來，E19 很早就支持了，以及目前 Wayland 上的
WM/Compositor 除了作爲實驗性參考實現的 weston 和上述 DE 之外，還有不少
`有趣 <https://github.com/Cloudef/loliwm>`_ 又
`好玩 <https://github.com/evil0sheep/motorcar>`_ 的新 WM 。
另外各個發行版支持程度方面 Fedora 21 上的 Gnome 3 也有實驗性支持了。
總體上可以說從 Xorg 遷移到 Wayland 的準備已經基本就緒了。

於是問題就是 **我們是否應該換到 Wayland** ？
要回答這個問題，我們需要瞭解 Wayland 到底 **是什麼** 與 **不是什麼** ，
瞭解它 **試圖解決的問題** 與它 **帶來的問題**
，從我理解到的角度說明這些問題也就是我寫這篇文章的目的。

那麼 Wayland 是什麼？ `官網 <http://wayland.freedesktop.org/>`_ 這麼說::

	Wayland is intended as a simpler replacement for X…
	Wayland is a protocol for a compositor to talk to its clients as well as a C library implementation of that protocol…

也就是說 Wayland 是一個用來實現 :ruby:`混成器|Compositor` 的協議和庫，
實現了 Wayland 協議的混成器可以用來替代我們的 X 圖形服務器。

要理解混成器是什麼，桌面系統爲什麼需要混成器，請看我之前的一篇文章
`桌面系統的混成器簡史 <{filepath}/tech/brief-history-of-compositors-in-desktop-os.zh.rst>`_ 。

關於目前 X 上實現混成器的方式和其限制，請看上一篇文章
`X 中的混成器與 Composite 擴展 <{filepath}/tech/compositor-in-X-and-compositext.zh.rst>`_ 。

於是我們有了 Wayland
--------------------------------------------------------------------

上面簡要說了 X 中目前實現混成器的基本情況，太多細節被我忽略了沒有提及，
而我選擇性提到的這些問題都是我認爲重要的，對理解 Wayland 有幫助的問題。

爲什麼我們需要 Wayland ？我覺得上面說到的兩點目前 Composite 的缺陷已經很明顯了，
這裏再重複一遍：

#. 同樣的位圖在進程間（應用程序→Xorg）來回傳遞
