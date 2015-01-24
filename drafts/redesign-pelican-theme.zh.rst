重新設計了 Pelican 的主題與插件
=======================================

:slug: redesign-pelican-theme
:lang: zh
:date: 2015-01-21 23:45
:tags: python, pelican
:series: pelican

.. contents::


前言
++++++++++++++++++++

.. PELICAN_BEGIN_SUMMARY

不知不覺間放任這邊長草很久了，從上次
`折騰主題 <{filename}/tech/try_pelican.zh.rst>`_ 到現在都快三年了，
而從上次 `寫了篇告白信 <{filename}/life/marry-me.zh.rst>`_ 到現在也有快兩年了。
這期間曾經把主題配色從 `Bootstrap 2 <http://getbootstrap.com/2.3.2/>`_ 默認的
白底黑字改成了讓眼睛更舒適的黑底白字，也不過是用 drop-in 的配色方案而已，沒有本質上的改進。

洞中一日世上千載，兩年裏 Bootstrap 已經升上 `v3.3 <http://getbootstrap.com/>`_ ,
而 Pelican 則已經升到 `3.5 <https://github.com/getpelican/pelican/releases/tag/3.5.0>`_ 了。
早就眼饞 Bootstrap 和 Pelican 中的諸多新功能新設計，不過無奈於時間有限只能飽飽眼福。


.. PELICAN_END_SUMMARY

.. panel-default::
  :title: 在邁阿密參加 `ICSR 2015 <http://icsr2015.ipd.kit.edu/>`_ 的時候
          拍到的街邊一家叫 Pelican 的旅館

  .. image:: {filename}/images/pelican.jpg
      :alt: Pelican Hotel


Bootstrap 3 的新設計
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 全新的 :ruby:`優先移動設備|mobile-first` :ruby:`響應式|responsive` 設計。
  原本Bootstrap 2雖然有響應式設計，
  不過諸多細節不能符合我的需求，最終還是得手工 hack :code:`@media` 查詢去微調。
  現在的 :ruby:`優先移動設備|mobile-first` :ruby:`響應式|responsive`
  :ruby:`柵格系統|grid system` 則相對顯得科學很多了，也終於能在手持
  設備上看起來能舒服很多。諸位可以嘗試改變窗口寬度，或者在不同的手持設備上打開這個 
  blog ，體驗一下這個頁面在不同顯示器大小中的效果。如果仍有問題歡迎
  `發 Issue 給我 <https://github.com/farseerfc/pelican-bootstrap3/issues>`_  。

- 科學的 :ruby:`導航欄|Navbar` 。
  比 Bootstrap 2 那個科學很多了。無論是 :ruby:`保持|sticky` 在上端還是跟着浮動，
  或者像這邊這樣 `自動隱藏 <http://www.virtuosoft.eu/code/bootstrap-autohidingnavbar/>`_ 都很簡單。  

更多細節參考 `Bootstrap 3 主頁 <http://getbootstrap.com/>`_ 。


Pelican 3.5 的新功能
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Python 2 和 Python 3 統一代碼：
  再沒有惱人的 unicode 相關的問題了。這對 blog 系統來說相當重要啊。
  而且還能方便切換 pypy 等不同的解釋器。

- 全新的插件系統：非常多功能強大的 `插件 <https://github.com/getpelican/pelican-plugins>`_ 等着你。

- 增強了導入系統：嗯總算可以導入我的中文的 wordpress 博客了。（雖然那邊長草更久了……）

- `站內鏈接 <http://pelican.readthedocs.org/en/latest/content.html#linking-to-internal-content>`_
  ：不用 :ruby:`硬編碼|hard code` 目標頁面的鏈接了，可以直接寫源文件的位置然後讓 pelican 
  處理，這樣能簡化各種 :ruby:`插件|plugin` 和 :ruby:`主題|theme` 的實現。

更多細節參考 `Pelican 文檔 <http://pelican.readthedocs.org/en/latest/>`_ 。


.. PELICAN_BEGIN_SUMMARY

近日想寫的東西越積越多，終於下定決心花了前前後後 **兩個月** 的時間重新設計了一遍 
Pelican 的主題，配合一些我覺得有用的插件。於是本博客就變成你們現在看到的樣子了。
（以及本篇博文也用了兩個月的時間寫完，其間還發了幾篇別的短文，算是恢復寫博客的嘗試吧。）

.. PELICAN_END_SUMMARY

新的文件夾佈局 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. panel-default::
    :title: Pelican 的新文件夾佈局
    
    .. raw:: html

        <pre>
        <span style="color:blue;font-weight:bold;">.</span>
        ├── <span style="color:blue;font-weight:bold;">cache</span>             生成頁面的 pickle 緩存.
        ├── <span style="color:blue;font-weight:bold;">content</span>           讀取的全部內容.
        │   ├── <span style="color:blue;font-weight:bold;">&lt;categories&gt;</span>      按分類存放的文章.
        │   ├── <span style="color:blue;font-weight:bold;">pages</span>             像 About 這樣的固定頁面.
        │   └── <span style="color:blue;font-weight:bold;">static</span>            文章內用到的靜態內容.
        ├── <span style="color:blue;font-weight:bold;">drafts</span>            文章的草稿箱.
        ├── <span style="color:green;font-weight:bold;">Makefile</span>          生成用的 makefile
        ├── <span style="color:green;font-weight:bold;">pelicanconf.py</span>    測試時用的快速 Pelican 配置.
        ├── <span style="color:green;font-weight:bold;">publishconf.py</span>    部署時用的耗時 Pelican 配置.
        ├── <span style="color:teal;font-weight:bold;">output</span>          -&gt; <span style="color:blue;font-weight:bold;">../farseerfc.github.io</span>
        ├── <span style="color:teal;font-weight:bold;">plugins</span>         -&gt; <span style="color:blue;font-weight:bold;">../pelican-plugins</span>
        └── <span style="color:teal;font-weight:bold;">theme</span>           -&gt; <span style="color:blue;font-weight:bold;">../pelican-bootstrap3</span>
        </pre>

`之前的博客 <https://github.com/farseerfc/farseerfc.github.com>`_ 仍然留在 
github 上，其中的內容完全搬過來了。開始寫老博客的時候 Pelican 版本較早，沒有形成好的
文件夾佈局，導致生成的文章、使用的模板和撰寫的內容全都混在一起，非常難以管理，
於是趁改版之際用了新的文件夾佈局方式，並分爲 4 個 git repo 分別管理歷史。

首先是存放 `總的博客內容的 repo <https://github.com/farseerfc/farseerfc>`_ ，
其佈局是如圖那樣的。這樣將生成的靜態網站和生成網站用的配置啦內容啦分開之後，頓時清晰了很多。

然後這個內容 repo 中的三個符號鏈接分別指向三個子 repo（沒用 :code:`git submodule` 
管理純粹是因爲偷懶）。 theme 指向 pelican-bootstrap3 ，是我修改過的 pelican 主題。 
plugins 指向 pelican-plugins，由於 plugins 的質量有些參差不齊，其中不少 plugin 
都按我的需要做了些許修改，一些是功能改進，另一些則是修bug（比如不少plugin只支持 python 2）。
最後 output 指向 farseerfc.github.io 也就是發佈的靜態網站啦。

接下來主要在 **主題** 和 **插件** 兩個方面介紹一下改版的細節。

主題： Material Design 風格的 Bootstrap 3 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

上篇 `博文 <{filename}/tech/summary-material-design-css-framework.zh.rst>`_ 
就總結了我爲了這個博客尋找了一堆 CSS 框架，並且最終決定用 
`bootstrap-material-design <http://fezvrasta.github.io/bootstrap-material-design/>`_
, `pelican-bootstrap3 <https://github.com/DandyDev/pelican-bootstrap3>`_
和 `Bootstrap 3 <http://getbootstrap.com/>`_ 這三個項目結合的方式實現這個模板的主題。
這三個項目都或多或少經過了我的修改，修改後的項目以 pelican-bootstrap3 爲基礎放在
`這裏 <https://github.com/farseerfc/pelican-bootstrap3>`_ ，包括 `Bootstrap3 樣式 <https://github.com/farseerfc/pelican-bootstrap3/tree/master/static/bootstrap>`_
和 `Material 樣式 <https://github.com/farseerfc/pelican-bootstrap3/tree/master/static/material>`_。

對 Bootstrap 3 的定製
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

由於架構完善，修改 Bootstrap 3 感覺非常簡單。另一方面我在 Web 前端技術上的技能點也不多，
所以修改的地方非常有限，只能按我自己的需求定製而已。

.. panel-default::
    :title: 修改了 Bootstrap 3 響應式設備的大小

    .. code-block:: css

        @screen-xs:     320px;
        @screen-sm:     598px; /*  768px; */
        @screen-md:     952px; /*  992px; */
        @screen-lg:    1350px; /* 1200px; */
        @screen-xl:    2030px; 
        @container-sm:  582px; /*  750px; */
        @container-md:  930px; /*  970px; */
        @container-lg: 1320px; /* 1170px; */
        @container-xl: 1990px;


首先把 Bootstrap 3 默認適配的幾個 `響應式設備的大小 <http://getbootstrap.com/css/#grid>`_ 
改成了我需要的大小。:code:`xs` 和 :code:`sm` 的大小分別按照我的手機屏幕 **豎屏** 和
**橫屏** 時候的瀏覽器頁面寬度來算， :code:`md` 是想兼容 Nexus 7 橫屏 960 的寬度以及
一個常見上網本 1024 的寬度。:code:`lg` 的大小則按照常見的筆記本 1366 寬的屏幕來適配。
這裏 Bootstrap 3 支持的設備大小的一個問題是，它最多考慮到 1200 像素寬的顯示器，而更大的
比如 1600、 2048 甚至 2560 寬的顯示器現在也並不少見，其結果就是頁面中左右兩側
有很大的空間被浪費掉了。作爲深受這一問題困擾的用戶之一，我用
`這裏介紹的方法 <http://stackoverflow.com/a/25644266>`_
給 bootstrap 增加了一類「:ruby:`比大更大|bigger than bigger`」的 :code:`xl` 響應式設備尺寸，寬度設爲支持 2048 
像素寬的顯示器。

然後把主題配色改成了現在這樣的淡紫色 :code:`@brand-primary: darken(#6B5594, 6.5%);`
，配合我的頭像風格， 這個修改只需要一行。
接着刪掉了 :code:`.btn` 的 :code:`white-space: nowrap;` 讓按鈕的文字可以換行，
這也只是一行修改。

接下來一個目標是讓主頁的文章列表像 Google+ 主頁那樣根據顯示器寬度自動分欄。
想要達到的效果是，根據上面定義的屏幕寬度尺寸：

- :code:`xs` 用單欄 :ruby:`流動|fluid` 佈局
- :code:`sm` 和 :code:`md` 用單欄列表加單欄側邊欄固定佈局
- :code:`lg` 用雙欄列表加單欄側邊欄固定佈局
- :code:`xl` 用三欄列表加雙欄側邊欄固定佈局

+---+---+----+------------+------------+
|          |Navbar|                    |
+===+===+====+============+============+
| 1 | 2 | 3  | |sidebar|  |  |sidebar| |
+---+---+----+            |            |
| 4 | 5 | 6  |            |            |
+---+---+----+------------+------------+
|          Footer                      |
+---+---+----+-------------------------+

.. |Navbar| replace:: 導航欄
.. |Footer| replace:: 底欄
.. |sidebar| replace:: 側邊欄

最後是最最重要的 **文章正文** 的樣式。這裏我想要達到的效果是，在大屏幕上用更大的字號，讓讀者
看起來更舒適，同時在小屏幕上用比較小的字號，最終保證基本上「一行」的文字數接近。這個修改
主要針對 :code:`.jumbotron`，
用了 `不太科學的方式 <https://github.com/farseerfc/pelican-bootstrap3/blob/master/static/bootstrap/jumbotron.less>`_ 代碼太長就不貼全了。


對 bootstrap-material-design 的定製
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

這裏定製的地方也不算太多。原樣式中一個不太科學的做法是所有 :code:`.btn` 都強制加上了陰影
效果，這在已經有陰影的環境裏用的話非常礙眼，像是 Win9x 風格的厚重的睫毛膏。既然可以單獨
給每個樣式加陰影，於是就把 :code:`.btn` 強制的陰影去掉了，只保留鼠標懸停之後強調的陰影。
其它定製的細節麼就是統一配色風格而已啦，這個不說太多。


將以上兩者整合在 pelican-bootstrap3 裏
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

雖說 pelican-bootstrap3 是我 fork 出來的，不過由於我修改的地方實在太多，代碼看來基本上
接近重寫了一份。好在之前有給 pelican 寫 bootstrap 2 主題的經驗，這次修改算得上駕輕就熟。


Test Math
+++++++++++++++++++

The area of a circle is :math:`A_\text{c} = (\pi/4) d^2`.

.. math::

  α_t(i) = P(O_1, O_2, … O_t, q_t = S_i λ)