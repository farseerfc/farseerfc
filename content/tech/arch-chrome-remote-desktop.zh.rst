archlinux 上用 chrome 實現 :del:`透明計算` 遠程登錄 
====================================================================

:slug: arch-chrome-remote-desktop
:lang: zh
:date: 2015-02-13 20:39
:tags: linux, archlinux, arch, chrome, remote, desktop
:issueid: 33

.. contents::

`透明計算 <http://news.sciencenet.cn/htmlnews/2015/1/311393.shtm>`_ 
具體是什麼，因爲他們沒有公開技術細節所以我並不知道，只是看
`公開出來的演示視頻 <http://v.qq.com/page/h/v/q/h0145ebh1vq.html>`_ 
，感覺似乎只要能從手機上遠程登錄系統桌面，就能算是透明計算了。
如果透明計算真是這個意思，那麼我似乎已經用着這個技術很多年了嘛。

Xorg 上常用的遠程桌面工具有很多，基於 VNC 協議的、基於NX的和基於 RDP 協議的都能找到，
直接 ssh X forwarding 效果也不錯。只是這些方案的一個 **不太易用** 的地方在於，需要
通過 ip 訪問到遠程的電腦，所以在跨越 NAT 之類的情況下不太容易使用。

於是今天介紹一個使用方便設置也簡單的方法： 通過 chrome-remote-desktop 在 archlinux 
上使用遠程桌面。這個方案的優勢在於，藉助 Google 的雲端服務器（內部貌似是XMPP協議下的握手）
方便地實現了 NAT 穿透，無論什麼網絡環境基本都能使用。當然，要支持遠程登錄，
位於遠端的登錄的計算機必須一直開着 Chrome Remote Desktop 的後臺服務。

.. panel-default:: 
	:title: Chrome Remote Desktop 插件

	.. image:: {filename}/images/chrome-remote-desktop-plugin.png
	  :alt: Chrome Remote Desktop 插件

Chrome Remote Desktop 的客戶端
------------------------------------------------

雖然可能有很多人不知道，不過 Chrome 內包括遠程桌面的功能很久了。只是這個功能的界面默認
沒有提供界面，要使用它需要安裝 Google 官方出品的 
`remote-desktop 插件 <https://chrome.google.com/webstore/detail/chrome-remote-desktop/gbchcmhmhahfdphkhkmpfmihenigjmpp>`_ 。
裝好之後遠程桌面的客戶端就準備好，可以用來遠程訪問別的計算機桌面了（無論是 Windows/OS X
還是 Linux 都支持）。並且不光可以自己遠程訪問自己賬戶的桌面，還可以遠程協助朋友的桌面。


Archlinux 上設置遠程登錄的服務器
------------------------------------------------

有了客戶端之後還要設置一下纔能讓桌面作爲遠程登錄的服務器。Windows 和 OS X 上 Chrome
會自動下載需要的安裝包，無腦下一步就能裝好了。Linux上由於發行版衆多，桌面配置各異，
所以需要一點手動配置。官方的設置步驟記載在 `這裏 <https://support.google.com/chrome/answer/1649523>`_
其中給出了 debian 用的二進制包和 Ubuntu 12.10 上的設置方式，以下設置是參考官方步驟。

首先要安裝 chrome-remote-desktop 這個包，這個包實際上對應了 Windows/OS X 上用安裝程序
安裝的 Remote Desktop Host Controller。 archlinux 上開啓了
`[archlinuxcn] <https://github.com/archlinuxcn/repo>`_
倉庫的話，可以直接安裝打好的包。或者可以從
`AUR <https://aur.archlinux.org/packages/chrome-remote-desktop/>`_ 裝。

.. raw:: html

	<pre>$ pacman -Ss chrome-remote-desktop<br/><span style="color:purple;font-weight:bold;">archlinuxcn/</span><span style="font-weight:bold;">chrome-remote-desktop </span><span style="color:green;font-weight:bold;">40.0.2214.44-1</span><br/>Allows you to securely access your computer over the Internet through Chrome.</pre>

裝好之後從會說這麼一段話：

	groupadd：无效的组 ID “chrome-remote-desktop”

	Please create ~/.config/chrome-remote-desktop folder manually, if it doesn't exist, or else you can't use CRD.
	The needed files are created by the Chrome app, inside the chrome-remote-desktop folder, after Enabling Remote Connections.
	To {enable,start} the service use systemctl --user {enable,start} chrome-remote-desktop

	You may need to create a ~/.chrome-remote-desktop-session file with commands to start your session

	Go to https://support.google.com/chrome/answer/1649523 for more information.

那句報錯是 AUR 裏打的包還沒跟上上游 Google 的更改導致的錯誤，
首先我們需要把遠程登錄的用戶添加入 chrome-remote-desktop 這個用戶組裏。
新版本的 chrome remote desktop 提供了一個命令做這個事情，所以執行以下命令就可以了：

.. code-block:: console

	$ /opt/google/chrome-remote-desktop/chrome-remote-desktop --add-user

然後我們需要手動創建 :code:`~/.config/chrome-remote-desktop` 這個文件夾，內容是空的
就好了，隨後 chrome 會往這裏面放 :code:`host#.json` 文件用於身份驗證。

.. code-block:: console

	$ mkdir ~/.config/chrome-remote-desktop

然後我們要創建一個 shell 腳本 :code:`~/.chrome-remote-desktop-session` ，這是遠程
登錄時的 .xinitrc ，內容麼就是啓動你想在遠程登錄時用的桌面環境。
這裏可以指定一個和你正在登錄的 WM/DE 不同的桌面，比如我啓動 xfce4：

.. code-block:: console

	$ cat ~/.chrome-remote-desktop-session
	#!/bin/bash
	startxfce4
	$ chmod 755 .chrome-remote-desktop-session


接下來需要從 Chrome 的插件裏啓用遠程桌面。打開 Chrome 的 Remote Desktop 插件，這時
應該可以看到一個「啓用遠程鏈接」的按鈕。

.. figure:: {filename}/images/chrome-remote-desktop-enable-button.png
  :alt: Chrome Remote Desktop 插件中「啓用遠程鏈接」的按鈕

  Chrome Remote Desktop 插件中「啓用遠程鏈接」的按鈕

.. alert-warning::
	
	在撰寫本文的時候， Archlinux 官方源裏的 chromium 的版本和 aur/google-chrome 
	的版本尚且還是 40.0.2214.111 ，而 Chrome Web Store 中提供的 Chrome Remote 
	Desktop 的插件的版本是 41.0.2272.41 。雖然通常並不要求兩者版本一致，不過貌似最近
	Chrome 內部的 Remoting 功能更改了 API 導致可能出問題。如果你找不到
	「啓用遠程鏈接」的按鈕，請嘗試一下新版本的 Chrome 比如 google-chrome-dev 。
	在這一步啓用之後，老版本的 chrome 應該也就能使用遠程桌面了。

.. alert-warning::
	
	在32位的 Linux 版本上，最近更新的 Chrome Remote Desktop 插件可能無法正確識別 Host
	的版本，具體 `參考這個 bug <https://code.google.com/p/chromium/issues/detail?id=332930>`_ 。


點擊「啓用遠程鏈接」，設定一個 PIN 密碼（不需要很複雜，這裏首先有 Google 帳號驗證保證只有
你纔能訪問），然後就能看到這套電腦的 hostname 出現在「我的電腦」列表裏。

.. figure:: {filename}/images/chrome-remote-desktop-after-enabled.png
  :alt: 啓用遠程鏈接之後的樣子

  啓用遠程鏈接之後的樣子


同時，啓用了遠程鏈接之後，可以在剛剛創建的 ~/.config/chrome-remote-desktop 
文件夾中找到記錄了驗證信息的文件。

.. code-block:: console

	$ ls .config/chrome-remote-desktop 
	chrome-profile  host#8cfe7ecfd6bb17955c1ea22f77d0d800.json  pulseaudio#8cfe7ecfd6

然後就可以啓動對應的 systemd 用戶服務了，如果想自動啓動服務要記得 :code:`systemctl --user enable` ：

.. code-block:: console

	$ systemctl --user start chrome-remote-desktop.service

如果上面的設置一切正常，就可以看到 chrome-remote-desktop 啓動了另外一個 Xorg 執行你
剛剛指定的桌面環境：

.. figure:: {filename}/images/chrome-remote-desktop-htop.png
  :alt: htop 中看到的 chrome-remote-desktop 啓動的另外一個 Xorg

  htop 中看到的 chrome-remote-desktop 啓動的另外一個 Xorg

然後就可以試着通過 Remote Desktop 插件登錄到這個新開的 Xorg 了：

.. figure:: {filename}/images/chrome-remote-desktop-xfce4.png
  :alt: 「遠程」登錄到新的 XFCE4

  「遠程」登錄到新的 XFCE4


Linux 版本的 Chrome遠程桌面 和 Windows/ OS X 上的區別 
------------------------------------------------------------------


通過上面的設置步驟也可以看出，Linux版本的遠程桌面會在後臺開一個獨立的 X 會話，而不能
復用現在已有的 X 會話。對遠程登錄的用法而言這還能接受，對遠程協助的功能而言有點問題，
因爲正在使用的人不能觀察協助者做了什麼，協助者也不能繼續請求協助的人的操作。

當然目前 Chrome 遠程桌面的 Linux Host Controller 還只是 beta 版本，官方只測試支持 
Ubuntu 12.04 和 12.10 （14.04之後似乎有 
`Bug <https://code.google.com/p/chromium/issues/detail?id=366432>`_
），所以不能要求太多。希望以後能改善吧。


Bonus： 手機遠程登錄
----------------------------------------

.. panel-default:: 
	:title: 手機上的 Chrome 遠程桌面 App

	.. image:: {filename}/images/chrome-remote-desktop-android.png
	  :alt: 手機上的 Chrome 遠程桌面 App

通過上面的設置就可以從任何一個 Chrome 遠程桌面客戶端登錄剛剛設置的這臺電腦了。
因爲 Chrome 在三大桌面系統 Windows / OS X / Linux 上都有，所以應該能覆蓋大多數桌面
系統了。

除了桌面的 Chrome 之外還有一個客戶端是 Android 上的
`Chrome 遠程桌面 App <https://play.google.com/store/apps/details?id=com.google.chromeremotedesktop>`_ 經過上面的設置之後，從這個 App 也能看到並登錄： 

.. figure:: {filename}/images/chrome-remote-desktop-android-logined.png
  :alt: 手機遠程登錄

  手機遠程登錄

好啦，開始享受國家自然科學一等獎的透明計算技術吧！