我眼中的 Wayland 的是與非
=====================================

:slug: wayland-good-and-bad
:lang: zh
:date: 2015-03-12 22:45
:tags: linux, wayland, xorg

.. contents::

.. panel-default:: 
	:title: Wayland

	.. image:: {filename}/images/wayland.png
	  :alt: Wayland

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

於是問題就是 **我們是否應該換到 Wayland** ？
要回答這個問題，我們需要瞭解 Wayland 到底 **是什麼** 與 **不是什麼** ，
瞭解它 **試圖解決的問題** 與它 **帶來的問題** ，說明我理解到的這些也就是我寫這篇文章的目的。


先說說 Wayland 是何來歷 
--------------------------------------------------------------------

Wayland 是什麼？ `官網 <http://wayland.freedesktop.org/>`_ 這麼說::

	Wayland is intended as a simpler replacement for X…

	Wayland is a protocol for a compositor to talk to its clients 
	as well as a C library implementation of that protocol…

也就是說 Wayland 是一個用來實現 :ruby:`混成器|Compositor` 的協議和庫，
實現了 Wayland 協議的混成器可以用來替代我們的 X 圖形服務器。
那麼 **混成器** 這又是個什麼東西，我們爲什麼需要它呢？
要理解爲什麼我們需要 **混成器** （或者它的另一個叫法，
:ruby:`混合窗口管理器|Compositing Window Manager` ），我們需要回顧一下歷史，
瞭解一下混成器出現之前主要的窗口管理器，也就是
:ruby:`棧式窗口管理器|Stacking Window Manager` 的實現方式。


早期的棧式窗口管理器
++++++++++++++++++++++++++++++++++++++++++++++++


.. panel-default:: 
	:title: 棧式窗口管理器的例子，Windows 3.11 的桌面，圖片來自維基百科

	.. image:: {filename}/images/Windows_3.11_workspace.png
	  :alt: 棧式窗口管理器的例子，Windows 3.11 的桌面



我們知道最初圖形界面的應用程序是全屏的，獨佔整個顯示器（現在很多遊戲機和手持設備的實現仍舊如此）。
所有程序都全屏並且任何時刻只能看到一個程序的輸出，這個限制顯然不能滿足人們使用計算機的需求，
於是就有了 `窗口 <http://en.wikipedia.org/wiki/WIMP_(computing)>`_ 
的概念，有了 `桌面隱喻 <http://en.wikipedia.org/wiki/Desktop_metaphor>`_ 。

在 :ruby:`桌面隱喻|Desktop Metaphor` 中每個窗口只佔用顯示面積的一小部分，有其顯示的位置和大小，
可以互相遮蓋。於是棧式窗口管理器就是在圖形界面中實現桌面隱喻的核心功能，
其實現方式大體就是：給每個窗口一個相對的“高度”或者說“遠近”，比較高的窗口顯得距離用戶比較近，
會覆蓋其下比較低的窗口。繪圖的時候窗口管理器會從把窗口按高低排序，按照從低到高的順序
使用 `畫家算法 <http://zh.wikipedia.org/wiki/%E7%94%BB%E5%AE%B6%E7%AE%97%E6%B3%95>`_
繪製整個屏幕。

這裏還要補充一點說明，在當時圖形界面的概念剛剛普及的時候，繪圖操作是非常“昂貴”的。
可以想象一下 800x600 像素的顯示器輸出下，每幀
`真彩色 <http://zh.wikipedia.org/wiki/%E7%9C%9F%E5%BD%A9%E8%89%B2>`_
位圖就要佔掉 :math:`800 \times 600 \times 3 \approx 1.4 \text{MiB}` 的內存大小，30Hz 的刷新率
（也就是30FPS）下每秒從 CPU 傳往繪圖設備的數據單單位圖就需要
:math:`1.4 \times 30 = 41 \text{MiB}` 的帶寬。對比一下當時的
`VESA 接口 <http://en.wikipedia.org/wiki/VESA_Local_Bus>`_ 總的數據傳輸能力也就是
:math:`25 \text{MHz} \times 32 \text{bits} = 100 \text{MiB/s}` 左右，
而 Windows 3.1 的最低內存需求是 1MB，對當時的硬件而言無論是顯示設備、內存或是CPU，
這無疑都是一個龐大的負擔。

於是在當時的硬件條件下採用棧式窗口管理器有一個巨大 **優勢** ：如果正確地採用畫家算法，
並且合理地控制重繪時 **只繪製沒有被別的窗口覆蓋的部分** ，那麼無論有多少窗口互相
遮蓋，都可以保證每次繪製屏幕的最大面積不會超過整個顯示器的面積。
同樣因爲實現方式棧式窗口管理器也有一些難以迴避的 **限制** ：

#. 窗口必須是矩形的，不能支持不規則形狀的窗口。
#. 不支持透明或者半透明的顏色。
#. 爲了優化效率，在縮放窗口和移動窗口的過程中，窗口的內容不會得到重繪請求，
   必須等到縮放或者移動命令結束之後窗口纔會重繪。


NeXTSTEP 與 Mac OS X 中混成器的發展
++++++++++++++++++++++++++++++++++++++++++++++++

.. panel-default:: 
	:title: NeXTSTEP 圖片來自維基百科

	.. image:: {filename}/images/NeXTSTEP_desktop.png
	  :alt: NeXTSTEP 圖片來自維基百科


轉眼進入了千禧年， Windows 稱霸了 PC 產業，蘋果爲重振 Macintosh 請回了 Jobs 基於 NeXTSTEP_
開發 Mac OSX 。 NeXTSTEP 在當時提供的 GUI 界面技術相比較於同年代的 X 和 Windows 有一個很特別的地方：
拖動滾動條或者移動窗口的時候，窗口的內容是實時更新的，這比只顯示一個縮放大小的框框來說被認爲更直觀。
而實現這個特性的基礎是在 NeXTSTEP 中運用了 
`Display PostScript (DPS) <http://en.wikipedia.org/wiki/Display_PostScript>`_
技術，簡單地說，就是每個窗口並非直接輸出到位圖，而是把內容輸出到 (Display) PostScript 格式表達的中間格式
交給窗口管理器，然後窗口管理器再在需要的時候把 PostScript 解釋成位圖顯示在屏幕上。

.. _NeXTSTEP: http://en.wikipedia.org/wiki/NeXTSTEP

.. ditaa::

	/--------\          +----------+     Window    +--------+
	|        |  Render  |   Saved  |     Server    |        |
	| Window |--------->|    DPS   |-------------->| Screen |
	|cGRE    |          |cPNK  {d} |               |cBLU    |
	\--------/          +----------+               +--------+


比起讓窗口直接繪製，這種方案在滾動和移動窗口的時候不需要重新渲染保存好的 DPS ，所以能實現實時渲染。
到了實現 Mac OS X 的時候，爲了同時兼容老的 Mac程序 API (carbon) 以及更快的渲染速度（還有考慮到
Adobe 對蘋果收取的高昂的 Display PostScript 授權費）， Mac OS X 的 Quartz 技術在矢量圖的 PDF
格式和最終渲染之間又插入了一層抽象：

.. ditaa::

	/--------\          +-------+             +----------+   Quartz     +--------+
	| Cocoa  | Quartz2D |       |  Rasterize  | Rendered | Compositor   |        |
	| Window |--------->|  PDF  |------------>|  Bitmap  |------------->| Screen |
	|cGRE    |          |cPNK{d}| (QuartzGL†) |cYEL  {d} | (Quartz      |cBLU    |
	\--------/          +-------+             +----------+  Extreme†)   +--------+
	     |                                      ^      ^
	     |                                      |      |            /--------\ 
	     |            Core OpenGL               |      | QuickDraw  | Carbon |
	     \--------------------------------------/      \------------| Window |
	                                                                |cGRE    |
	     † Optional                                                 \--------/


.. panel-default:: 
	:title: Mission Control 圖片來自維基百科

	.. image:: {filename}/images/Mac_OS_X_Lion_Preview_-_Mission_Control.jpg
	  :alt: Mission Control 圖片來自維基百科

也就是說無論任何窗口用何種方式繪圖，都會繪製輸出在一個保存在內存中的位圖交給混成器，
而後者再在需要的時候將位圖繪製在屏幕上。這種架構使得 2001年3月發佈的 Mac OS X v10.0
成爲了第一個廣泛使用的具有軟件混成器的操作系統。

到了 Mac OX X v10.2 的時候，蘋果又引入了 Quartz Extreme 讓最後的混成渲染這一步發生在
顯卡上。然後在 2003年1月公開亮相的 Mac OS X v10.3 中，他們公佈了 Exposé (後來叫 Mission Control)
功能，把窗口的縮略圖（而不是事先繪製的圖標）顯示在桌面上，方便用戶挑選打開的窗口。

由於有了混成器的這種實現方式，使得可能把窗口渲染的圖像做進一步加工，添加三維和動畫效果。
這使得 Mac OS X 有了美輪美奐的動畫效果和 Exposé 這樣的方便易用的功能。

插曲: Project Looking Glass
++++++++++++++++++++++++++++++++++++++++++++++++

在蘋果那邊剛開始使用混成器渲染窗口的時候，昔日的 :ruby:`昇陽公司|Sun Microsystems`
則在 Linux 上作出了另一個更炫酷的東西，被他們命名爲 Project Looking Glass
（別和 Google 的 Project Glass 混淆呀）。

換句話說， **wayland 相比較於現在的 Xorg 來說到底有什麼優勢** ？ 
--------------------------------------------------------------------
w
