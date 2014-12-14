重新設計了Pelican的主題與插件
=======================================

:slug: redesign-pelican-theme
:lang: zh
:date: 2014-12-14 23:45
:tags: python, pelican
:series: pelican

.. contents::

.. PELICAN_BEGIN_SUMMARY

前言
++++++++++++++++++++


不知不覺間放任這邊長草很久了，從上次 `折騰主題 <{filename}/python/try_pelican.zh.rst>`_ 到現在都快三年了，
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
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

這個界面風格要從 Google 在 `I/O 2014 大會 <https://www.google.com/events/io>`_ 上公佈 
Android L 也即 後來的 Lollipop 說起。 他們在談論界面設計的時候公佈了他們的
設計準則： `Material Design <http://www.google.com/design/spec/material-design/introduction.html>`_ (`中文非官方翻譯 <http://wcc723.gitbooks.io/google_design_translate/>`_ )。
當然這只是一些準則，總結並描述了之前在 Web 設計和移動端 App 界面設計方面的一些規範，
並且用材料的類比來形象化的比喻這個準則。關於 Material Design 的更多中文資料可 `參考這裏 <http://www.ui.cn/Material/>`_ 。

看到 Material Design 之後就覺得這個設計風格非常符合直覺，於是想在這邊也用上 Material Design。
但是我在 Web 前端科技樹上沒點多少技能點，所以想找找別人實現好的模板或者框架直接套用上。
從而就找到了這幾個：


Polymer Paper Elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. panel-default:: 
  :title: Polymer

  .. image:: https://www.polymer-project.org/images/logos/p-logo.svg
      :alt: Polymer logo

Google 官方提供的參考實現應該是 `Polymer <https://www.polymer-project.org/>`_ 中的
`Paper Elements <https://www.polymer-project.org/docs/elements/paper-elements.html>`_ 。

由於是官方參考實現，這個框架的確非常忠實地實現了 Material Design 的設計，但是同時由於它
基於 `HTML5 Web Components <http://webcomponents.org/>`_ 構建，相關技術我還不太懂，瀏覽器兼容性和其餘 HTML 技術的兼容性也還不太完善的樣子…… 

並且對於我這個 Web 開發的半吊子來說，Polymer 只是提供了一組設計組建，沒有完善的 Responsive 佈局支持，也沒有
Navbar 這種常見的框架組建，真的要用起來的話還需要手工實現不少東西。
於是口水了半天之後只好放棄……以後可能真的會換用這個，只是目前需要學的東西太多了。


Angular Material Design 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. panel-default::
  :title: AngularJS

  .. image:: https://angularjs.org/img/AngularJS-large.png
      :alt: AngularJS logo


`AngularJS <https://angularjs.org/>`_ 是 Google 對 Web Components 技術的另一個嘗試。
而這額 `Angular Material Design <https://material.angularjs.org/>`_ 項目就是基於 AngularJS 構建的
Material Design 庫啦，同樣是 Google 出品所以應該算得上半個官方實現吧。
相比於 Polymer, AngularJS 算是實用了很多，提供了基於 `CSS Flexbox <http://www.w3.org/TR/css3-flexbox/>`_ 的
佈局。有人對這兩者的評價是， 如果說 Polymer 代表了未來趨勢，那麼 AngularJS 就是現階段可用的 Web Components 了。

只不過同樣是因爲它是 Components 的框架，對 WebApp 的支持很豐富，大量採用 Ajax 等 JavaScript 技術，
對於我這個靜態博客來說仍然稍顯高級了……非常擔心還不支持 HTML5 的瀏覽器比如 W3M 甚至 cURL 對它的支持程度。
於是最終也沒有使用它。
