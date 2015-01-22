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
`折騰主題 <{filename}/python/try_pelican.zh.rst>`_ 到現在都快三年了，
而從上次 `寫了篇告白信 <{filename}/life/marry-me.zh.rst>`_ 到現在也有快兩年了。
這期間曾經把主題配色從 `Bootstrap 2 <http://getbootstrap.com/2.3.2/>`_ 默認的
白底黑字改成了黑底白字，也不過是用 drop-in 的配色方案而已，沒有本質上的改進。

洞中一日世上千載，兩年裏 Bootstrap 已經升上 `v3.3 <http://getbootstrap.com/>`_ ,
而 Pelican 則已經升到 `3.5 <https://github.com/getpelican/pelican/releases/tag/3.5.0>`_ 了。
早就眼饞 Bootstrap 和 Pelican 中的諸多新功能新設計，不過無奈於時間有限只能飽飽眼福。


.. PELICAN_END_SUMMARY

Bootstrap 3 的新設計
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 全新的mobile-first responsive設計。

原本Bootstrap 2雖然有responsive design的設計，
不過諸多細節不能符合我的需求，最終還是得手工 hack :code:`@media` 查詢去微調。
現在的mobile-first responsive grid system 則相對顯得科學很多了，也終於在手持
設備上看起來能舒服很多。諸位可以嘗試改變窗口寬度，或者在不同的手持設備上打開這個 
blog ，體驗一下這個頁面在不同顯示器大小中的效果。如果仍有問題歡迎
`發 Issue 給我 <https://github.com/farseerfc/pelican-bootstrap3/issues>`_  。

- 科學的 Navbar 。

比 Bootstrap 2 那個科學很多了。無論是 sticky 在上端還是跟着浮動，或者像這邊這樣
`自動隱藏 <http://www.virtuosoft.eu/code/bootstrap-autohidingnavbar/>`_
都很簡單。  

更多細節參考 `Bootstrap 3 主頁 <http://getbootstrap.com/>`_ 。


Pelican 3.5 的新功能
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Python 2 和 Python 3 統一代碼

再沒有惱人的 unicode 相關的問題了。這對 blog 系統來說相當重要啊。
而且還能方便切換 pypy 等不同的解釋器。

- 全新的插件系統：非常多好用的 `插件 <https://github.com/getpelican/pelican-plugins>`_ 等着你。

- 增強了導入系統：嗯總算可以導入我的中文的 wordpress 博客了。（雖然那邊長草更久了……）

- 頁面內鏈接：不用硬編碼手寫鏈接了，方便各種 plugin 和 theme 的實現。

更多細節參考 `Pelican 文檔 <http://pelican.readthedocs.org/en/latest/>`_ 。


.. PELICAN_BEGIN_SUMMARY

近日想寫的東西越積越多，終於下定決心重新設計了一遍 Pelican 的主題，加之一些精選的插件。
於是本博客就變成你們現在看到的樣子了。

.. PELICAN_END_SUMMARY

新的文件夾佈局 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. panel-default::
    :title: Pelican 的新文件夾佈局
    
    .. uml::

        salt
        {
        {T
        +.
        ++ cache                             Pelican 用的加速生成緩存
        ++ content                           文章
        +++ <categories>                     按分類存放    
        +++ images                           文章包含的靜態圖片
        +++ pages                            about 這樣的頁面
        +++ static                           個別文章包含的靜態資源
        ++ drafts                            未發佈的本地草稿箱
        ++ Makefile                          生成用的make
        ++ pelicanconf.py                    Pelican 的測試用配置 
        ++ publishconf.py                    Pelican 的生成用配置
        ++ plugins -> ../pelican-plugins
        ++ output -> ../farseerfc.github.io
        ++ theme -> ../pelican-bootstrap3
        }
        }

`之前的博客 <https://github.com/farseerfc/farseerfc.github.com>`_ 仍然留在 
github 上，其中的內容完全搬過來了。老 Pelican 博客的 Pelican 沒有很好的文件夾佈局，
導致生成的文章、使用的模板和撰寫的內容全都混在一起，非常難以管理，於是趁改版之際用了新的
文件夾佈局方式，並分爲 4 個 git repo 分別管理歷史。

首先是存放 `總的博客內容的 repo <https://github.com/farseerfc/farseerfc>`_ ，
其佈局是如圖那樣的。
這樣將生成的靜態網站和生成網站用的配置啦內容啦分開之後，頓時清晰了很多。

主題： Material Design 風格的 Bootstrap 3 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

上篇 `博文 <{filename}/python/summary-material-design-css-framework.zh.rst>`_ 
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

        @screen-xs:  320px;
        @screen-sm:  598px;
        @screen-md:  992px;
        @screen-lg: 1400px;

首先把 Bootstrap 3 默認適配的幾個響應式設備的大小改成了我需要的大小。
:code:`xs` 和 :code:`sm` 的大小分別按照我的手機屏幕 **豎屏** 和 **橫屏** 來算， 
:code:`lg` 的大小則按照常見的 MacBook Pro Retina 13' 配置下 1440 寬的屏幕來適配。
雖然很想再定義比 :code:`lg` 更大的寬度，比如目前 2560 寬的屏幕也不算少見了，但是貌似工作量
有點大比較難以下手。


然後把主題配色改成了現在這樣的淡紫色，配合我的頭像風格， 這個修改只需要一行：

.. code-block:: css

    @brand-primary:         darken(#6B5594, 6.5%);

接着刪掉了 :code:`.btn` 的 :code:`white-space: nowrap;` 讓按鈕的文字可以換行。

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