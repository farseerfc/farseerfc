重新設計了Pelican的主題與插件
=======================================

:slug: redesign-pelican-theme
:lang: zh
:date: 2014-12-11 23:45
:tags: python, pelican
:series: pelican

.. contents::

.. PELICAN_BEGIN_SUMMARY

前言
++++++++++++++++++++


不知不覺間放任這邊長草很久了，從上次 `折騰主題 <{filename}/programming/try_pelican.zh.rst>`_ 到現在都快三年了，
而從上次 `寫了篇告白信 <{filename}/life/marry-me.zh.rst>`_ 到現在也有快兩年了。
這期間曾經把主題配色從 `Bootstrap 2 <http://getbootstrap.com/2.3.2/>`_ 默認的白底黑字改成了黑底白字，
也不過是用 drop-in 的配色方案而已，沒有本質上的改進。

洞中一日世上千載，兩年裏 Bootstrap 已經升上 `v3.3 <http://getbootstrap.com/>`_ ,
而 Pelican 則已經升到 `3.5 <https://github.com/getpelican/pelican/releases/tag/3.5.0>`_ 了。
早就眼饞 Bootstrap 和 Pelican 中的諸多新功能新設計，不過無奈於時間有限只能飽飽眼福。


.. PELICAN_END_SUMMARY


.. panel-default::
    :title: Bootstrap 3 的新設計

    - 全新的mobile-first responsive設計。

      原本Bootstrap 2雖然有responsive design的設計，
      不過諸多細節不能符合我的需求，最終還是得手工 hack :code:`@media screen` 查詢去微調。
      現在的mobile-first responsive grid system 則相對顯得科學很多了，也終於在手持設備上看起來能舒服很多。
      諸位可以嘗試改變窗口寬度，或者在不同的手持設備上打開這個 blog ，體驗一下這個頁面在不同顯示器大小中的效果。
      如果仍有問題歡迎 `發 Issue 給我 <https://github.com/farseerfc/pelican-bootstrap3/issues>`_  呀。

    - 科學的 Navbar 。

      比 Bootstrap 2 那個科學很多了。無論是 sticky 在上端還是跟着浮動，或者像這邊這樣
      `自動隱藏 <http://www.virtuosoft.eu/code/bootstrap-autohidingnavbar/>`_ 都很簡單。  

    更多細節參考 `Bootstrap 3 主頁 <http://getbootstrap.com/>`_ 。


.. panel-default::
    :title: Pelican 3.5 的新功能

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
接下來從主題和插件，也即外用與內體兩方面介紹一下這次改版的細節。

.. PELICAN_END_SUMMARY

外用：基於Material Design的主題
++++++++++++++++++++++++++++++++++++++++

這個界面風格要從 Google 在 `I/O 2014 大會 <https://www.google.com/events/io>`_ 
上公佈 Android L 也即 後來的 Lollipop 說起。 他們在談論界面設計的時候公佈了他們的
設計準則： `Material Design <http://www.google.com/design/>`_ 。
當然這只是一些準則，總結並描述了之前在 Web 設計和移動端 App 界面設計方面的一些規範，
並且用材料的類比來形象化的比喻這個準則。