重新設計了Pelican的主題
=======================================

:slug: redesign-pelican-theme
:lang: zh
:date: 2014-12-07 23:45
:tags: python, pelican
:status: draft

不知不覺間放任這邊長草很久了，從上次 `折騰主題 <{filename}try_pelican.zh.rst>`_ 到現在都快三年了，
而從上次 `寫了篇告白信 <{filename}/life/marry-me.zh.rst>`_ 到現在也有快兩年了。
這期間曾經把主題配色從 `Bootstrap 2 <http://getbootstrap.com/2.3.2/>`_ 默認的白底黑字改成了黑底白字，
也不過是用 drop-in 的配色方案而已。
而洞中一日世上千載，兩年裏 Bootstrap 已經升上 `v3.3 <http://getbootstrap.com/>`_ ,
而 Pelican 則已經升到 `3.5 <https://github.com/getpelican/pelican/releases/tag/3.5.0>`_ 了。
早就眼饞 Bootstrap 和 Pelican 中的諸多新功能新設計，不過無奈於時間有限只能飽飽眼福。

.. panel-default::
    :title: Bootstrap 3 的新設計

    - 全新的 mobile-first responsive 設計。

      原本 Bootstrap 2 雖然有 responsive design 的設計，
      不過諸多細節不能符合我的需求，最終還是得手工 hack :code:`@media screen` 查詢去微調。
      現在的 mobile-first responsive grid system 則相對顯得科學很多了，也終於在手持設備上看起來能舒服很多。
      諸位可以嘗試改變窗口寬度，體驗一下這個頁面在不同顯示器大小中的效果。如果仍有問題歡迎 
      `發 Issue 給我 <https://github.com/farseerfc/pelican-bootstrap3/issues>`_  呀。

    - 科學的 Navbar 。

      比 Bootstrap 2 那個科學很多了。
      無論是 sticky 在上端還是跟着浮動，或者像這邊這樣自動隱藏都很簡單。  

近日想寫的東西越積越多，終於下定決心重新設計了一遍 Pelican 的主題。於是本博客就變成你們現在看到的樣子了。