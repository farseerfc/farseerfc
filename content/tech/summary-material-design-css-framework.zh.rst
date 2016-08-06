總結一下 Material Design 的 CSS 框架
=======================================

:slug: summarize-material-design-css-framework
:lang: zh
:date: 2015-01-16 03:27
:tags: css, material, paper
:series: pelican
:issueid: 47

.. PELICAN_BEGIN_SUMMARY

現在這裏的界面風格要從 Google 在 `I/O 2014 大會 <https://www.google.com/events/io>`_
上公佈Android L 也即 後來的 Lollipop 說起。 他們在談論界面設計的時候公佈了他們的
設計準則： `Material Design <http://www.google.com/design/spec/material-design/introduction.html>`_ (`中文非官方翻譯 <http://wcc723.gitbooks.io/google_design_translate/>`_ )。
當然這只是一些準則，總結並描述了之前在 Web 設計和移動端 App 界面設計方面的一些規範，
並且用材料的類比來形象化的比喻這個準則。關於 Material Design 的更多中文資料可
`參考這裏 <http://www.ui.cn/Material/>`_ 。

看到 Material Design 之後就覺得這個設計風格非常符合直覺，於是想在這邊也用上
Material Design。 但是我在 Web 前端科技樹上沒點多少技能點，所以想找找別人實現好的模板
或者框架直接套用上。在網絡上搜索數日找到了這幾個：


Polymer Paper Elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. PELICAN_END_SUMMARY

.. panel-default::
  :title: Polymer

  .. image:: https://www.polymer-project.org/images/logos/p-logo.svg
      :alt: Polymer logo

.. PELICAN_BEGIN_SUMMARY

Google 官方提供的參考實現應該是 `Polymer <https://www.polymer-project.org/>`_ 中的
`Paper Elements <https://www.polymer-project.org/docs/elements/paper-elements.html>`_ 。

.. PELICAN_END_SUMMARY

由於是 **官方參考實現** ，這個框架的確非常忠實地實現了 Material Design 的設計，但是同時
由於它基於 `HTML5 Web Components <http://webcomponents.org/>`_ 構建，相關技術我還
不太懂，瀏覽器兼容性和其餘 HTML 技術的兼容性也還不太完善的樣子……

並且對於我這個 Web 開發的半吊子來說，Polymer 只是提供了一組設計組建，沒有完善的 
**響應式** (responsive) 佈局支持，也沒有 Navbar 這種常見的框架組建，真的要用起來的話還
需要手工實現不少東西。於是口水了半天之後只好放棄……以後可能真的會換用這個，只是目前需要學
的東西太多了。


Angular Material Design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. panel-default::
  :title: AngularJS

  .. image:: https://angularjs.org/img/AngularJS-large.png
      :alt: AngularJS logo


`AngularJS <https://angularjs.org/>`_ 是 Google 對 Web Components 技術的另一個
嘗試。而這額 `Angular Material Design <https://material.angularjs.org/>`_ 項目
就是基於 AngularJS 構建的Material Design 庫啦，同樣是 Google 出品所以應該算得上半個
官方實現吧。 相比於 Polymer, AngularJS 算是實用了很多，提供了基於 
`CSS Flexbox <http://www.w3.org/TR/css3-flexbox/>`_ 的佈局。有人對這兩者的評價是，
如果說 Polymer 代表了 **未來趨勢** ，那麼 AngularJS 就是 **眼下可用** 的 Web
Components 實現了。

只不過同樣是因爲它是 Components 的框架，對 WebApp 的支持很豐富，大量採用 Ajax 等
JavaScript 技術， 對於我這個靜態博客來說仍然稍顯高級了……非常擔心還不支持 HTML5 的瀏覽器
比如 w3m 甚至 cURL 對它的支持程度。 於是最終也沒有使用它。


Materialize
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. panel-default::
  :title: Materialize

  .. image:: https://raw.githubusercontent.com/Dogfalo/materialize/master/images/materialize.gif
      :alt: Materialize logo

`Materialize <http://materializecss.com/>`_ 這是一批(自稱?)熟悉 Android 上
Material Design 的設計師們新近出爐的框架，試圖提供一個接近 Bootstrap 的方案。
最早是在 `Reddit <http://www.reddit.com/r/web_design/comments/2lt4qy/what_do_you_think_of_materialize_a_responsive/>`_ 上看到對它的討論的，立刻覺得這個想法不錯。

體驗一下官網的設計就可以看出，他們的動畫效果非常接近 Polymer 的感覺，響應式設計的佈局
也還不錯。 只是同樣體驗一下他們現在的官網就可以看出，他們目前的
`bug 還比較多 <https://github.com/Dogfalo/materialize/issues>`_ ，甚至一些 bug
在他們自己的主頁上也有顯現。 雖然不想給這個新出爐的項目潑涼水，不過看來要達到他們聲稱的接近
Bootstrap 的易用度還任重而道遠……


bootstrap-material-design + bootstrap3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

這是我最終選擇的方案。這個方案將三個項目組合在了一起，分別是 
`bootstrap-material-design <http://fezvrasta.github.io/bootstrap-material-design/>`_
, `pelican-bootstrap3 <https://github.com/DandyDev/pelican-bootstrap3>`_
和 `Bootstrap 3 <http://getbootstrap.com/>`_ 。
Bootstrap 3 想必不用再介紹了，很多網站都在使用這套框架，定製性很高。 
bootstrap-material-design 是在 Bootstrap 3 的基礎上套用 Material Design 風格
製作的一套 CSS 庫，當然也不是很完善並且在不斷改進中，一些細節其實並不是很符合我的要求。
最後 pelican-bootstrap3 是用 Bootstrap 3 做的 pelican 模板。
這三個項目或多或少都有點不合我的口味，於是嘛就把 pelican-bootstrap3 fork了一套放在
`這裏 <https://github.com/farseerfc/pelican-bootstrap3>`_ ，其中還包括我自己改
過的 `Bootstrap3 樣式 <https://github.com/farseerfc/pelican-bootstrap3/tree/master/static/bootstrap>`_
和 `Material 樣式 <https://github.com/farseerfc/pelican-bootstrap3/tree/master/static/material>`_
，需要的可以自取。

至於細節上我定製了哪些地方，敬請聽下回分解……