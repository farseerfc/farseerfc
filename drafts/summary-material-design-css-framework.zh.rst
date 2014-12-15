總結一下 Material Design 的 CSS 框架
=======================================

:slug: summarize-material-design-css-framework
:lang: zh
:date: 2014-12-16 00:08
:tags: css, material, paper
:series: pelican


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

並且對於我這個 Web 開發的半吊子來說，Polymer 只是提供了一組設計組建，沒有完善的響應式(responsive)佈局支持，也沒有
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


Materialize
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. panel-default::
  :title: Materialize

  .. image:: https://raw.githubusercontent.com/Dogfalo/materialize/master/images/materialize.gif
      :alt: Materialize logo

`Materialize <http://materializecss.com/>`_ 這是一批(自稱?)熟悉 Android 上 Material Design 的設計師
們新近出爐的框架，試圖提供一個接近 Bootstrap 的方案。最早是在 `Reddit <http://www.reddit.com/r/web_design/comments/2lt4qy/what_do_you_think_of_materialize_a_responsive/>`_ 上看到對它的討論的，立刻覺得這個想法不錯。

體驗一下官網的設計就可以看出，他們的動畫效果非常接近 Polymer 的感覺， 響應式設計的佈局也還不錯。