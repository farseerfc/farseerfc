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

連着有 `五六年了 <http://www.phoronix.com/scan.php?page=news_topic&q=Wayland&selection=20>`_
，每年都有人說 Wayland_ 要來了， X11 即將壽終正寢了。
畢竟 X11 這個顯示服務器遠在 Linux 誕生之前就有了，歲數都比我大（我出生於X11R3和X11R4之間），
歷史遺留問題一大堆，安全性、擴展性都跟不上時代了。

.. _Wayland: http://wayland.freedesktop.org/


看樣子 2015年的確像是 Wayland 終於能用了 
--------------------------------------------------------------------

根據 `Arch 的 Wiki <https://wiki.archlinux.org/index.php/Wayland>`_
上跟蹤着的 wayland 進展，
`toolkit 方面 <https://wiki.archlinux.org/index.php/Wayland#GUI_libraries>`_
GTK+ 3, Qt 5, EFL, Clutter, SDL 等等的幾個圖形庫都完整支持 wayland 並且在 archlinux
中默認啓用了。
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

那麼 Wayland 是什麼？ `官網 <http://wayland.freedesktop.org/>`_ 這麼說::

	Wayland is intended as a simpler replacement for X…

	Wayland is a protocol for a compositor to talk to its clients
	as well as a C library implementation of that protocol…

也就是說 Wayland 是一個用來實現 :ruby:`混成器|Compositor` 的協議和庫，
實現了 Wayland 協議的混成器可以用來替代我們的 X 圖形服務器。
那麼 **混成器** 這又是個什麼東西，我們爲什麼需要它呢？
要理解爲什麼我們需要 **混成器** （或者它的另一個叫法，
:ruby:`混成窗口管理器|Compositing Window Manager` ），我們需要回顧一下歷史，
瞭解一下混成器出現之前主要的窗口管理器，也就是
:ruby:`棧式窗口管理器|Stacking Window Manager` 的實現方式。


其它桌面系統中混成器的發展史 
--------------------------------------------------------------------


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

在 :ruby:`桌面隱喻|Desktop Metaphor` 中每個窗口只佔用顯示面積的一小部分，
有其顯示的位置和大小，可以互相遮蓋。於是棧式窗口管理器就是在圖形界面中實現桌面隱喻的核心功能，
其實現方式大體就是：給每個窗口一個相對的“高度”或者說“遠近”，比較高的窗口顯得距離用戶比較近，
會覆蓋其下比較低的窗口。繪圖的時候窗口管理器會從把窗口按高低排序，按照從低到高的順序使用
`畫家算法 <http://zh.wikipedia.org/wiki/%E7%94%BB%E5%AE%B6%E7%AE%97%E6%B3%95>`_
繪製整個屏幕。

這裏還要補充一點說明，在當時圖形界面的概念剛剛普及的時候，繪圖操作是非常“昂貴”的。
可以想象一下 800x600 像素的顯示器輸出下，每幀
`真彩色 <http://zh.wikipedia.org/wiki/%E7%9C%9F%E5%BD%A9%E8%89%B2>`_
位圖就要佔掉 :math:`800 \times 600 \times 3 \approx 1.4 \text{MiB}` 的內存大小，30Hz
的刷新率（也就是30FPS）下每秒從 CPU 傳往繪圖設備的數據單單位圖就需要
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

以上這些限制在早期的 X11 窗口管理器比如 twm 以及 XP 之前經典主題的 Windows
或者經典的 Mac OS 上都能看到。
在這些早期的窗口環境中，如果你拖動或者縮放一個窗口，那麼將顯示變化後的窗口邊界，
這些用來預覽的邊界用快速的位圖反轉方式繪製。當你放開鼠標的時候纔會觸發窗口的
重繪事件。
雖然有很多方法或者說技巧能繞過這些限制，比如 Windows XP 上就支持了實時的
重繪事件和不規則形狀的窗口剪裁，不過這些技巧都是一連串的 hack ，難以擴展。

NeXTSTEP 與 Mac OS X 中混成器的發展
++++++++++++++++++++++++++++++++++++++++++++++++

.. panel-default::
	:title: NeXTSTEP 圖片來自維基百科

	.. image:: {filename}/images/NeXTSTEP_desktop.png
	  :alt: NeXTSTEP 圖片來自維基百科


轉眼進入了千禧年， Windows 稱霸了 PC 產業，蘋果爲重振 Macintosh 請回了 Jobs 基於 NeXTSTEP_
開發 Mac OSX 。 

NeXTSTEP 在當時提供的 GUI 界面技術相比較於同年代的 X 和 Windows 有一個很特別的地方：
拖動滾動條或者移動窗口的時候，窗口的內容是實時更新的，這比只顯示一個縮放大小的框框來說被認爲更直觀。
而實現這個特性的基礎是在 NeXTSTEP 中運用了
`Display PostScript (DPS) <http://en.wikipedia.org/wiki/Display_PostScript>`_
技術，簡單地說，就是每個窗口並非直接輸出到顯示設備，而是把內容輸出到 (Display) PostScript 
格式交給窗口管理器，然後窗口管理器再在需要的時候把 PostScript 用軟件解釋器解釋成位圖顯示在屏幕上。

.. _NeXTSTEP: http://en.wikipedia.org/wiki/NeXTSTEP

.. ditaa::

	/--------\          +---------+     Window    +--------+
	|        |  Render  |  Saved  |     Server    |        |
	| Window |--------->|   DPS   |-------------->| Screen |
	|cGRE    |          |cPNK  {d}|               |cBLU    |
	\--------/          +---------+               +--------+


比起讓窗口直接繪製，這種方案在滾動和移動窗口的時候不需要重新渲染保存好的 DPS ，
所以能實現實時渲染。到了實現 Mac OS X 的時候，爲了同時兼容老的 Mac 程序 API (carbon)
以及更快的渲染速度，以及考慮到 Adobe 對蘋果收取的高昂的 Display PostScript 授權費，
Mac OS X 的 Quartz 技術在矢量圖的 PDF 格式和最終渲染之間又插入了一層抽象：

.. ditaa::

	
	/--------\
	| Carbon |
	| Window |----------------------------------------\
	|cGRE    |           QuickDraw                    |
	\--------/                                        |
	                                                  v
	/--------\          +----------+             +----------+      Quartz        +--------+
	| Cocoa  | Quartz2D : Internal |  Rasterize  | Rendered |    Compositor      |        |
	| Window |--------->|   PDF    |------------>|  Bitmap  |------------------->| Screen |
	|cGRE    |          |cPNK   {d}| (QuartzGL†) |cYEL   {d}| (Quartz Extreme†)  |cBLU    |
	\--------/          +----------+             +----------+                    +--------+
	                                                  ^      
	/--------\                                        | 
	| OpenGL |            Core OpenGL                 |      
	| Window |----------------------------------------/        † Optional
	|cGRE    |	         
	\--------/	                                                                  



.. panel-default::
	:title: Mission Control 圖片來自維基百科

	.. image:: {filename}/images/Mac_OS_X_Lion_Preview_-_Mission_Control.jpg
	  :alt: Mission Control 圖片來自維基百科

也就是說在 Mac OS X 中無論窗口用何種方式繪圖，都會繪製輸出成一副內存中的位圖交給混成器，
而後者再在需要的時候將位圖混成在屏幕上。這種設計使得 2001年3月發佈的 Mac OS X v10.0
成爲了第一個廣泛使用的具有軟件混成器的操作系統。

到了 Mac OS X v10.2 的時候，蘋果又引入了 Quartz Extreme 讓最後的混成渲染這一步發生在
顯卡上。然後在 2003年1月公開亮相的 Mac OS X v10.3 中，他們公佈了 Exposé (後來改名爲
Mission Control) 功能，把窗口的縮略圖（而不是事先繪製的圖標）並排顯示在桌面上，
方便用戶挑選打開的窗口。

由於有了混成器的這種實現方式，使得可能把窗口渲染的圖像做進一步加工，添加陰影、三維和動畫效果。
這使得 Mac OS X 有了美輪美奐的動畫效果和 Exposé 這樣的方便易用的功能。
或許對於喬布斯而言，更重要的是因爲有了混成器，窗口的形狀終於能顯示爲他 
`夢寐以求 <http://www.folklore.org/StoryView.py?story=Round_Rects_Are_Everywhere.txt>`_ 
的 `圓角矩形 <http://www.uiandus.com/blog/2009/7/26/realizations-of-rounded-rectangles.html>`_
了！

插曲：曇花一現的 Project Looking Glass 3D
++++++++++++++++++++++++++++++++++++++++++++++++

在蘋果那邊剛剛開始使用混成器渲染窗口的 2003 年，昔日的 :ruby:`昇陽公司|Sun Microsystems`
則在 Linux 上用 Java3D 作出了另一個更炫酷到沒有朋友的東西，被他們命名爲
`Project Looking Glass 3D <http://en.wikipedia.org/wiki/Project_Looking_Glass>`_
（縮寫LG3D，別和 Google 的 Project Glass 混淆呀）。這個項目的炫酷實在難以用言語描述，
好在還能找到兩段視頻展示它的效果。

.. youtubeku:: JXv8VlpoK_g XOTEzMzM3MTY0

.. youtubeku:: zcPIEMvyPy4 XOTEzMzQwMjky


.. panel-default::
	:title: LG3D 圖片來自維基百科

	.. image:: {filename}/images/LG3D.jpg
	  :alt: LG3D 圖片來自維基百科

如視頻中展示的那樣， LG3D 完全突破了傳統的棧式窗口管理方式，
在三維空間中操縱二維的窗口平面，不僅像傳統的窗口管理器那樣可以縮放和移動窗口，
還能夠旋轉角度甚至翻轉到背面去。從視頻中難以體會到的一點是， LG3D 在實現方式上與
Mac OS X 中的混成器有一個本質上的不同，那就是處於（靜止或動畫中）縮放或旋轉狀態
下的窗口是 **可以接受輸入事件** 的。這一重要區別在後面 Wayland 的說明中還會提到。
LG3D 項目展示了窗口管理器將如何突破傳統的棧式管理的框架，可以說代表了窗口管理器的未來發展趨勢。

LG3D 雖然沒有放出實現的源代碼，不過官方曾經放出過一個
`預覽版的 LiveCD <http://sourceforge.net/projects/lg3d-livecd/>`_
。只可惜時隔久遠（12年前了）在我的 VirtualBox 上已經不能跑起來這個 LiveCD 了……

更爲可惜的是，就在這個項目剛剛公開展示出來的時候，喬布斯就致電昇陽，
說如果繼續商業化這個產品，昇陽公司將涉嫌侵犯蘋果的知識產權
（時間順序上來看，蘋果最初展示 Exposé 是在 2003年6月23日的 
Apple Worldwide Developers Conference ，而昇陽最初展示
LG3D 是在 2003年8月5日的 LinuxWorld Expo）。
雖然和喬布斯的指控無關，昇陽公司本身的業務也着重於服務器端的業務，
後來隨着昇陽的財政困難，這個項目也就停止開發並不了了之了。


Windows 中的混成器
++++++++++++++++++++++++++++++++++++++++++++++++

.. panel-default::
	:title: Longhorn 中的 Wobbly 效果

	.. youtubeku:: X0idaN0MY1U XOTEzMzY5NjQ0

上面說到， Windows 系列中到 XP 爲止都還沒有使用混成器繪製窗口。
看着 Mac OS X 上有了美輪美奐的動畫效果， Windows 這邊自然不甘示弱。
於是同樣在 2003 年展示的 Project Longhorn 中就演示了 wobbly 效果的窗口，
並且跳票推遲多年之後的 Windows Vista 中實現了完整的混成器 
`Desktop Window Manager (DWM) <http://en.wikipedia.org/wiki/Desktop_Window_Manager>`_
。整個 DWM 的架構和 Mac OS X 上看到的很像：

.. ditaa::

	
	/--------------\
	| Windows cGRE |
	| Presentation |----------------------------------\
	| Foundation   |         DirectX 9                |
	\--------------/                                  |
	                                  Canonical       v       Desktop
	/--------\          +----------+   Display   +---------+  Window    +--------+
	|  GDI+  |  render  : Internal |   Driver    | DirectX |  Manager   |  WDDM  |
	| Window |--------->|   WMF    |------------>| Surface |----------->| Screen |
	|cGRE    |          |cPNK   {d}|             |cYEL  {d}|            |cBLU    |
	\--------/          +----------+             +---------+            +--------+
	                                                  ^
	/---------\                                       |
	| DirectX |                                       |
	| Window  |---------------------------------------/
	|cGRE     |              DirectX                   
	\---------/                                        

和 Mac OS X 的情況類似， Windows Vista 之後的應用程序有兩套主要的繪圖庫，一套是從早期
Win32API 就沿用至今的 GDI（以及GDI+），另一套是隨着 Longhorn 計劃開發出的 WPF 。
WPF 的所有用戶界面控件都繪製在 DirectX 貼圖上，所以使用了 WPF 的程序也可以看作是
DirectX 程序。而對老舊的 GDI 程序而言，它們並不是直接繪製到 DirectX 貼圖的。首先每一個
GDI 的繪圖操作都對應一條
`Windows Metafile (WMF) <http://en.wikipedia.org/wiki/Windows_Metafile>`_
記錄，所以 WMF 就可以看作是 Mac OS X 的 Quartz 內部用的 PDF 或者 NeXTSTEP 內部用的
DPS，它們都是矢量圖描述。隨後，這些 WMF 繪圖操作被通過一個
Canonical Display Driver (cdd.dll) 的內部組建轉換到 DirectX 平面，並且保存起來交給
DWM。最後， DWM 拿到來自 CDD 或者 DirectX 的平面，把它們混合起來繪製在屏幕上。

值得注意的細節是，WPF 底層的繪圖庫幾乎肯定有 C/C++ 綁定對應， Windows 自帶的不少應用程序
和 Office 2007 用了 Ribbon 之後的版本都採用這套繪圖引擎，不過微軟沒有公開這套繪圖庫的
C/C++ 實現的底層細節，而只能通過 .Net 框架的 WPF 訪問它。這一點和 OS X 上只能通過 
Objective-C 下的 Cocoa API 調用 Quartz 的情況類似。

另外需要注意的細節是 DirectX 的單窗口限制在 Windows Vista 之後被放開了，或者嚴格的說是
基於 WDDM 規範下的顯卡驅動支持了多個 DirectX 繪圖平面。
在早期的 Windows 包括 XP 上，整個桌面上同一時刻只能有一個程序的窗口處於 DirectX 的
**直接繪製** 模式，而別的窗口如果想用 DirectX 的話，要麼必須改用軟件渲染要麼就不能工作。
這種現象可以通過打開多個播放器或者窗口化的遊戲界面觀察到。
而在 WDDM 規範的 Vista 中，所有窗口最終都繪製到 DirectX 平面上，換句話說每個窗口都是
DirectX 窗口。又或者我們可以認爲，整個界面上只有一個真正的窗口也就是 DWM 繪製的全屏窗口，
只有 DWM 處於 DirectX 的直接渲染模式下，而別的窗口都輸出到 DirectX 平面裏（可能通過了硬件加速）。

由於 DWM 實現了混成器，使得 Vista 和隨後的 Windows 7 有了
`Aero Glass <http://en.wikipedia.org/wiki/Windows_Aero>`_ 的界面風格，
有了 Flip 3D 、Aero Peek 等等的這些輔助功能和動畫效果。
這套渲染方式延續到 Windows 8 之後，雖然 Windows 8 還提出了 Modern UI 
不過傳統桌面上的渲染仍舊是依靠混成器來做的。


X 中的混成器與 Composite 擴展
--------------------------------------

上面簡單介紹了 Mac OS X 和 Windows 系統中的混成器的發展史和工作原理，
話題回到我們的正題 Linux 系統上，來說說目前 X 中混成器是如何工作的。
首先，沒有混成器的時候 X 是這樣畫圖的：

.. ditaa::
	
	/--------\        +----------+           /------\    /--------\ 
	| GTK    | Cairo  | Internal | xlib/xcb  :      |    |        |  
	| Window |------->|   XPM    |---------------------->|        |
	|cGRE    |        |cPNK   {d}|           |      |    |        |             
	\--------/        +----------+           |      |    |        |             
	                                         :      :    |        | 
	/--------\        +----------+           | Xorg |    |        |  
	| QT     | QPaint | Internal | xlib/xcb  |      |    |        | 
	| Window |------->|   XPM    |---------------------->| Screen |
	|cGRE    |        |cPNK   {d}|           |      |    |        |
	\--------/        +----------+           |      |    |        |
	                                         :      :    |        |
	/----------\                             |      |    |        |
	| Xlib/XCB |          xlib/xcb           |      |    |        |
	| Window   |---------------------------------------->|        |
	|cGRE      |                             :      |    | cBLU   |
	\----------/                             \------/    \--------/	


	  
X 的應用程序沒有統一的繪圖 API ，GTK+ 在 3.0 之後統一用 Cairo 繪圖，
GTK 的 2.0 和之前的版本中也有很大一部分的繪圖是用 Cairo 進行，
其餘則通過 xlib 或者 xcb 調用 X 核心協議提供的繪圖原語繪圖。
QT 的情況也是類似，基本上用 QPaint 子系統繪製成位圖然後交給 X 的顯示服務器。
顯示服務器拿到這些繪製請求之後，再在屏幕上的相應位置繪製整個屏幕。
當然還有很多老舊的不用 GTK 或者 QT 的程序，他們則直接調用 X 核心協議提供的繪圖原語。

2004年發佈的 X11R6.8 版本的 Xorg 引入了
`Composite 擴展 <http://freedesktop.org/wiki/Software/CompositeExt/>`_
，這個擴展允許某個 X 程序做這幾件事情：

#. 將一個窗口樹中的所有窗口渲染重定向到 :ruby:`內部存儲|off-screen storage` 
   。這通過 :code:`RedirectSubwindows` 調用實現。重定向的時候可以指定讓 X
   自動更新窗口的內容到屏幕上或者不更新（由混成器手動更新）。
#. 取得某個窗口的內部存儲，通過 :code:`NameWindowPixmap` 實現。
#. 創建一個特殊的用於繪圖的窗口，對這個窗口上的繪製將覆蓋在屏幕的最上面，
   通過 :code:`CompositeGetOverlayWindow` 實現。
#. 取得某個窗口的邊界區域（不一定是矩形），通過 :code:`CreateRegionFromBorderClip`
   實現。

這樣的話，一個 X 程序就可以調用這些 API 實現混成器。開啓了混成的 X 是這樣繪圖的：

.. ditaa::
	
	/--------\        +----------+               /--------------\
	| GTK    | Cairo  | Internal | xlib/xcb      |  +---------+ |
	| Window |------->|   XPM    |----------------->| XPM {d} | |
	|cGRE    |        |cPNK   {d}|           /------|cYEL     | |
	\--------/        +----------+           |   |  +---------+ |
	                                         |   :              :
	/--------\        +----------+           |   |              |
	| QT     | QPaint | Internal | xlib/xcb  |   |  +---------+ |
	| Window |------->|   XPM    |----------------->| XPM {d} | |
	|cGRE    |        |cPNK   {d}|           | /----|cYEL     | |
	\--------/        +----------+           | | |  +---------+ |
	                                         | | :              |
	+-------------+    NameWindowPixmap      | | |     Xorg     |
	| Compositor  |<-------------------------/ | |    Server    |   /--------\
	| Overlay     |<---------------------------/ |              |   |        |
	| Window      |------------------------------------------------>| Screen |
	|cGRE         |<---------------------------\ |  XRender/    |   |cBLU    |
	+-------------+                            | |  OpenGL/EGL  |   \--------/
	                                           | :              :   
	/----------\                               | |  +---------+ |
	| Xlib/XCB |          xlib/xcb             \----| XPM {d} | |
	| Window   |----------------------------------->|cYEL     | |
	|cGRE      |                                 |  +---------+ |
	\----------/                                 \--------------/

整個 X 的混成器模型與 Mac OS X 的混成器模型相比，有如下幾點顯著的區別：

#. 混成的部分是交由外部的程序完成的，對混成的繪製方式和繪製普通窗口一樣。
   出於效率考慮，絕大多數 X 上的混成器額外使用了 XRender 擴展或者
   OpenGL/EGL 來加速繪製貼圖。
#. :code:`RedirectSubwindows` 調用針對的是一個窗口樹，換句話說是一個窗口
   及其全部子窗口，不同於 Mac OS X 中混成器能拿到全部窗口的輸出。
   另外一個限制是，爲了讓窗口有輸出，窗口必須顯示在當前桌面上，不能處於最小化
   狀態或者顯示在別的虛擬桌面，用 X 的術語說就是窗口必須處於 :ruby:`被映射|mapped`
   的狀態。因此直接用上述方法不能得到沒有顯示的窗口的輸出，比如不能對最小化的窗口
   直接實現 Windows 7 中的 Aero Peak 之類的效果。

以及，混成器用來繪製的 OverlayWindow 有個極其特殊的地方：它不是由混成器創建的，
而是由 X 創建並返回給混成器的，從而它 **沒有消息隊列，不能獲得任何鍵盤或者鼠標輸入**
。對 OverlayWindow 的點擊會透過 OverlayWindow 直接作用到底下的窗口上。
這帶來以下問題：

#. 窗口管理器或者混成器無法接受來自 OverlayWindow 的事件。如果想要實現類似 Exposé
   那樣的效果，即允許通過鼠標點擊選擇窗口，通常的做法是再在 OverlayWindow
   下面覆蓋一層置頂的普通窗口，由它接收鼠標鍵盤事件。
#. 如果要直接和窗口的內容交互，換句話說如果想要讓一般的窗口正常地接收鼠標鍵盤事件，
   那麼 **混成器繪製的窗口位置和大小必須嚴格地和底下普通窗口的位置和大小保持一致** 。
   再換句話說，雖然 Composite 允許我們重定向窗口內容的輸出，但是它不允許我們重定向
   鼠標鍵盤事件。這個的直接結果是，任何處於縮放狀態的窗口都不能獲得焦點和事件，
   反之要獲得焦點和事件，那麼窗口本身不能被縮放。


Wayland 與 Xorg 的區別 
--------------------------------------------------------------------

w
