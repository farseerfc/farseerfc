PacVis: visualize pacman local database
===============================================

:slug: pacvis
:lang: en
:date: 2016-07-31 03:52
:tags: python, pacvis, pacman, arch, linux, pacgraph

.. contents::

.. panel-default::
  :title: PacVis

  .. image:: {filename}/images/pacvis-first.png
      :alt: Demo of PacVis

Motivation for PacVis
----------------------------------------

I must admit that I love Arch Linux, largely because Arch Linux can let me feel
like I really **own** the whole system. In my Arch Linux system, I know clearly
every package that I have installed and why I installed it. I can find which
package brings in a give file. A Debian/Fedora/openSUSE user with experience
could do this with their favorite package manager too, but they must overcome
a much higher complexity with their distro's fine-grinding packaging strategy.
Usually they have 3 times to 10 times more packages than Arch Linux on a
similar setup. And with regard to packing, they must work with much more
details than Arch's simple PKGBUILD based system.

Every user who successfully installed Arch Linux should have known that, after
the initial installation, you will only get a minimum setup. The most important
thing in the installation guide on ArchWiki is a command
:code:`pactrap /mnt base` , which will use :code:`/mnt` as the filesystem root
and call :code:`pacman -S base` inside that root to install the whole base
group. And that's basically all you will get after the install. The initial
system has nearly nothing. Everything you need will be installed afterwards,
manually by using :code:`pacman`. It is nothing unnecessary, only for **your** need. 

But after using the system for a long time, there are unavoidably some packages
inside the system which are installed and used for awhile and abandoned.
They are like the old furnitures inside your house, taking space and covered by
ash. We have :code:`pacman -Qtd` to help you find all packages that are 
**installed as dependency for other packages once but not needed for now**
, but for those manually installed packages, we have no good tool but manually
checking them one by one.

So I was looking for a tool to help me understand the relations in my system.
In particular, I want a tool to help me do these things:

#. Find the packages that I installed manually but not needed now
#. Find those large and space-consuming packages
#. Understand th relationship between packages


.. figure:: {filename}/images/Android-System-Architecture.jpg
  :alt: Android System Architecture

  `Android System Architecture <https://en.wikipedia.org/wiki/Android_(operating_system)>`_

About the last thing "relations between packages", I once saw the diagram of
`macOS Architecture <https://en.wikipedia.org/wiki/Architecture_of_OS_X>`_
and Android System Architecture, and I was impressed by the layered hierarchy
in these diagrams. I was wondering since then that *is it possible to draw a
similar layered architecture diagram for modern Linux desktop* ?
Or will it be much different? I can find hierarchy diagram for Linux kernel or
Xorg graphic stack on Wikipedia or other sites, but I don't know such a diagram
for the whole distribution. And further I thought, can I draw such diagram from
the dependency relationships between packages automatically?


PacVis的老前輩們
----------------------------------------

在開始寫 PacVis 之前，我試過一些類似的工具，他們都或多或少能解決一部分我的需要，
又在某些方面有所不足。這些工具成爲了 PacVis 的雛形，啓發了 PacVis
應該做成什麼樣子。

pactree
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pactree 曾經是一個
`獨立的項目 <https://bbs.archlinux.org/viewtopic.php?id=51795>`_ ，現在則是
`pacman 的一部分 <https://www.archlinux.org/pacman/pactree.8.html>`_ 了。
從手冊頁可以看出， pactree 的輸出是由某個包開始的依賴樹。
加上 :code:`--graph` 參數之後 pactree 還能輸出
`dot <http://www.graphviz.org/>`_ 格式的矢量圖描述，然後可以用 dot 畫出依賴圖：

.. panel-default::
  :title: :code:`pactree pacvis-git -d3 --graph | dot -Tpng >pacvis-pactree.png`

  .. image:: {filename}/images/pacvis-pactree.png
      :alt: pactree --graph

.. code-block:: console

   $ pactree pacvis-git -d3
   pacvis-git
   ├─python-tornado
   │ └─python
   │   ├─expat
   │   ├─bzip2
   │   ├─gdbm
   │   ├─openssl
   │   ├─libffi
   │   └─zlib
   ├─pyalpm
   │ ├─python
   │ └─pacman
   │   ├─bash
   │   ├─glibc
   │   ├─libarchive
   │   ├─curl
   │   ├─gpgme
   │   ├─pacman-mirrorlist
   │   └─archlinux-keyring
   └─python-setuptools
     └─python-packaging
       ├─python-pyparsing
       └─python-six
    $ pactree pacvis-git -d3 --graph | dot -Tpng >pacvis-pactree.png

從畫出的圖可以看出，因爲有共用的依賴，所以從一個包開始的依賴關係已經不再是一棵
`圖論意義上的樹(Tree) <https://zh.wikipedia.org/wiki/%E6%A8%B9%E7%8B%80%E7%B5%90%E6%A7%8B>`_
了。最初嘗試做 PacVis 的早期實現的時候，就是試圖用 bash/python 腳本解析 pactree 和
pacman 的輸出，在 pactree 的基礎上把整個系統中所有安裝的包全都包含到一張圖裏。
當然後來畫出的結果並不那麼理想，首先由於圖非常巨大，導致 dot
的自動佈局要耗費數小時，最後畫出的圖也過於巨大基本上沒法看。

然而不得不說沒有 pactree 就不會有 PacVis ，甚至 pacman 被分離出 alpm
庫也和 pactree 用 C 重寫的過程有很大關係，而 PacVis 用來查詢 pacman 數據庫的庫
pyalpm 正是 alpm 的 Python 綁定。因爲 pactree 的需要而增加出的 alpm 庫奠定了 PacVis
實現的基石。

pacgraph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. panel-default::
  :title: pacgraph 的輸出

  .. image:: {filename}/images/pacvis-pacgraph.png
      :alt: pacgraph


`pacgraph <http://kmkeen.com/pacgraph/index.html>`_ 是一位 Arch Linux 的
Trusted User `keenerd <http://kmkeen.com/>`_ 寫的程序，和
PacVis 一樣也是用 Python 實現的。
比起 pactree ， pacgraph 明顯更接近我的需求，它默認繪製整個系統的所有安裝包，
並且用聰明的佈局算法解決了 dot 佈局的性能問題。

pacgraph 的輸出是一個富有藝術感的依賴圖，圖中用不同的字體大小表示出了每個包佔用
的磁盤空間。通過觀察 pacgraph 的輸出，我們可以清楚地把握系統全局的樣貌，
比如一眼看出這是個桌面系統還是個服務器系統，並且可以很容易地發現那些佔用磁盤空間
巨大的包，考慮清理這些包以節約空間。

更棒的是 pacgraph 還提供了一個交互性的 GUI 叫做 pacgraph-tk ，顯然通過 tk 實現。
用這個 GUI 可以縮放觀察整幅圖的細節，或者選中某個包觀察它和別的包的依賴關係。

pacgraph 還支持通過參數指定只繪製個別包的依賴關係，就像 pactree 那樣。

不過 pacgraph 也不是完全滿足我的需要。如我前面說過，我希望繪製出的圖能反應
**這個發行版的架構面貌** ，而 pacgraph 似乎並不區別「該包依賴的包」和「依賴該包的包」
這兩種截然相反的依賴關係。換句話說 pacgraph 畫出的是一張無向圖，
而我更想要一張有向圖，或者說是 **有層次結構的依賴關係圖** 。

於是就有了 PacVis
----------------------------------------

.. panel-default::
  :title: PacVis 剛打開的樣子

  .. image:: {filename}/images/pacvis-second.png
      :alt: PacVis on startup

總結了老前輩們的優勢與不足，我便開始利用空餘時間做我心目中的 PacVis 。
前後斷斷續續寫了兩個月，又分爲兩個階段，第一階段做了基本的功能和雛形，
第二階段套用上 https://getmdl.io/ 的模板，總算有了能拿得出手給別人看的樣子。

於是乎前兩天在 AUR 上給 pacvis 打了個
`pacvis-git <https://aur.archlinux.org/packages/pacvis-git/>`_
包，現在想在本地跑 pacvis 應該很方便了，用任何你熟悉的 aurhelper
就可以安裝，也可以直接從 aur 下載 PKGBUILD 打包：

.. code-block:: console

  ~$ git clone aur@aur.archlinux.org:pacvis-git.git
  ~$ cd pacvis-git
  ~/pacvis-git$ makepkg -si
  ~/pacvis-git$ pacvis
  Start PacVis at http://localhost:8888/

按照提示說的，接下來打開瀏覽器訪問 http://localhost:8888/ 就能看到 PacVis
的樣子了。僅僅作爲嘗試也可以直接打開跑在我的服務器上的 demo:
https://pacvis.farseerfc.me/ ，這個作爲最小安裝的服務器載入速度大概比普通的桌面系統快一點。


PacVis 的圖例和用法
----------------------------------------


操作上 PacVis 仿照地圖程序比如 Google Maps 的用法，可以用滾輪或者觸摸屏的手勢
縮放、拖拽，右上角有個側邊欄，不需要的話可以點叉隱藏掉，右下角有縮放的按鈕和
回到全局視圖的按鈕，用起來應該還算直觀。

.. figure:: {filename}/images/pacvis-pacvis-git.png
  :alt: PacVis showing pacvis-git

  pacvis-git 包的依賴

先解釋圖形本身，整張圖由很多小圓圈的節點，以及節點之間的箭頭組成。
一個圓圈就代表一個軟件包，而一條箭頭代表一個依賴關係。縮放到細節的話，
能看到每個小圓圈的下方標註了這個軟件包的名字，鼠標懸浮在圓圈上也會顯示響應信息。
還可以點開軟件包，在右側的邊欄裏會有更詳細的信息。

比如圖例中顯示了 pacvis-git 自己的依賴，它依賴 pyalpm, python-tornado 和
python-setuptools ，其中 pyalpm 又依賴 pacman 。圖中用
:html:`<span class="label label-primary">紫色</span>` 表示手動安裝的包，
:html:`<span class="label label-warning">橙色</span>` 表示被作爲依賴安裝的包，
箭頭的顏色也隨着包的顏色改變。

值得注意的是圖中大多數箭頭都是由下往上指的，這是因爲 PacVis 按照包的依賴關係做
了拓撲排序，並且給每個包賦予了一個拓撲層級。比如 pacvis-git 位於 39
層，那麼它依賴的 pyalpm 就位於 38 層，而 pyalpm 依賴的 pacman 就位於 37
層。根據層級關係排列包是 PacVis 於 pacgraph 之間最大的不同之處。

除了手動縮放， PacVis 還提供了搜索框，根據包名快速定位你感興趣的包。
以及在右側邊欄中的 Dep 和 Req-By 等頁中，包的依賴關係也是做成了按鈕的形式，
可以由此探索包和包之間的關聯。

最後稍微解釋一下兩個和實現相關的參數：

.. label-info:: Max Level

這是限制 PacVis 載入的最大拓撲層。系統包非常多的時候 PacVis
的佈局算法會顯得很慢，限制層數有助於加快載入，特別是在調試 PacVis 的時候比較有用。

.. label-info:: Max Required-By

這是限制 PacVis 繪製的最大被依賴關係。稍微把玩一下 PacVis 就會發現系統內絕大多數
的包都直接依賴了 glibc 或者 gcc-libs 等個別的幾個包，而要繪製這些依賴的話會導致
渲染出的圖中有大量長直的依賴線，不便觀察。於是可以通過限制這個值，使得 PacVis
不繪製被依賴太多的包的依賴關係，有助於讓渲染出的圖更易觀察。

從 PacVis 能瞭解到的一些事實
----------------------------------------


.. panel-default::
  :title: 一個 KDE 桌面的 PacVis 結果全圖， `放大（17M） <{filename}/images/pacvis-16384.png>`_

  .. image:: {filename}/images/pacvis-4096-anno.png
    :alt: A normal KDE desktop in PacVis

稍微玩一下 PacVis 就能發現不少有趣現象，上述「絕大多數包依賴 glibc 」就是一例。
除此之外還有不少值得玩味的地方。


依賴層次
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

系統中安裝的包被明顯地分成了這樣幾個層次：

* glibc 等 C 庫
* Bash/Perl/Python 等腳本語言
* coreutils/gcc/binutils 等核心工具
* pacman / systemd 等較大的系統工具
* gtk{2,3}/qt{4,5} 等 GUI toolkit
* chromium 等 GUI 應用
* Plasma/Gnome 等桌面環境

大體上符合直觀的感受，不過細節上有很多有意思的地方，比如 zsh 因爲 gdbm
間接依賴了 bash，這也說明我們不可能在系統中用 zsh 完全替代掉 bash。
再比如 python （在 Arch Linux 中是 python3）和 python2 和 pypy
幾乎在同一個拓撲層級。


.. figure:: {filename}/images/pacvis-zsh-bash.png
  :alt: zsh depends on bash because of gdbm
  :width: 45%

  zsh 因爲 gdbm 間接依賴了 bash

不過偶爾顯示的依賴層級不太符合直觀，比如 qt5-base < qt4 < gtk2 < gtk3 。
qt5 因爲被拆成了數個包所以比 qt4 更低級這可以理解，而 gtk 系比 qt
系更高級這一點是很多人（包括我）沒有預料到的吧。


循環依賴
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

有些包的依賴關係形成了循環依賴，一個例子是 freetype2 和 harfbuzz，freetype2
是繪製字體的庫，harfbuzz 是解析 OpenType 字形的庫，兩者對對方互相依賴。
另一個例子是 KDE 的 kio 和 kinit，前者提供類似 FUSE 的資源訪問抽象層，
後者初始化 KDE 桌面環境。


.. figure:: {filename}/images/pacvis-freetype2-harfbuzz.png
  :alt: freetype2 harfbuzz
  :width: 45%

  freetype2 和 harfbuzz 之間的循環依賴

因爲這些循環依賴的存在，使得 PacVis 在實現時不能直接拓撲排序，我採用環探測
算法找出有向圖中所有的環，並且打破這些環，然後再使用拓撲排序。
因此我在圖中用紅色的箭頭表示這些會導致環的依賴關係。


有些包沒有依賴關係
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: {filename}/images/pacvis-level0.png
  :alt: PacVis Level 0
  :width: 45%

  man-pages 和 licenses 沒有依賴關係

有些包既不被別的包依賴，也不依賴別的包，而是孤立在整張圖中，比如
man-pages 和 licenses 。這些包在圖中位於最頂端，拓撲層級是 0 ，我用
:html:`<span class="label label-info">藍色</span>` 正方形特別繪製它們。



只看依賴關係的話 Linux 內核完全不重要
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

所有用戶空間的程序都依賴着 glibc ，而 glibc 則從定義良好的 syscall 調用內核。
因此理所當然地，如果只看用戶空間的話， glibc 和別的 GNU 組建是整個 GNU/Linux
發行版的中心，而 Linux 則是位於依賴層次中很深的位置，甚至在我的 demo 服務器上
Linux 位於整個圖中的最底端，因爲它的安裝腳本依賴 mkinitcpio
而後者依賴了系統中的衆多組件。

PacVis 的未來
----------------------------------------

目前的 PacVis 基本上是我最初開始做的時候設想的樣子，隨着開發逐漸又增加了不少功能。
一些是迫於佈局算法的性能而增加的（比如限制層數）。

今後準備再加入以下這些特性：

#. 更合理的 optdeps 處理。目前只是把 optdeps 關係在圖上畫出來了。
#. 更合理的 **依賴關係抉擇** 。有時候包的依賴關係並不是直接根據包名，而是
   :code:`provides` 由一個包提供另一個包的依賴。目前 PacVis 用 alpm
   提供的方式抉擇這種依賴，於是這種關係並沒有記錄在圖上。
#. 目前的層級關係沒有考慮包所在的倉庫 (code/extra/community/...) 或者包所屬的組。
   加入這些關係能更清晰地表達依賴層次。
#. 目前沒有辦法只顯示一部分包的關係。以後準備加入像 pactree/pacgraph 一樣顯示部分包。

如果你希望 PacVis 出現某些有趣的用法和功能，也請給我提 issue 。
