用 Travis-CI 生成 Github Pages 博客
====================================================

:slug: travis-push-to-github-pages-blog
:lang: zh
:date: 2015-02-19 22:45
:tags: pelican, github, pages, travis, travis-ci, ubuntu
:series: pelican

.. contents::

前言
----------------------------

上次介紹 `過這個博客改換了主題 <{filename}/tech/redesign-pelican-theme.zh.rst>`_ ，
本以爲這個話題可以告一段落了，沒想到還要繼續呢。

寄宿在 Github Pages 上的靜態博客通常有兩種方案，其一是使用 Jekyll_ 方式撰寫，這可以利用
Github Pages 原本就有的 
`Jekyll支持 <https://help.github.com/articles/using-jekyll-with-pages/>`_
生成靜態網站。另一種是在 **本地** 也就是自己的電腦上生成好，然後把生成的 HTML 網站 push
到 Github Pages ，這種情況下 Github Pages 就完全只是一個靜態頁面宿主環境。

.. _Jekyll: http://jekyllrb.com/

我用 Pelican_ 生成博客，當然就只能選擇後一種方式了。這帶來一些不便，比如本地配置 pelican
還是有一點點複雜的，所以不能隨便找臺電腦就開始寫博客。再比如 pelican 本身雖然是 python
寫的所以跨平臺，但是具體到博客的配置方面， Windows 環境和 Linux/OSX/Unix-like
環境下還是有
`些許出入 <http://pelican.readthedocs.org/en/latest/settings.html#date-format-and-locale>`_
的。還有在手機上就不能隨便寫一篇博客發表出來（不知道有沒有勇士嘗試過在
Android 的 SL4A_ 環境下的 python 中跑 pelican ，還要配合一個
`Android 上的 git 客戶端 <https://play.google.com/store/apps/details?id=com.romanenco.gitt>`_ ）。

.. _Pelican: http://getpelican.com/
.. _SL4A: https://code.google.com/p/android-scripting/
.. _Agit: https://play.google.com/store/apps/details?id=com.madgag.agit

當然並不是因此就束手無策了，感謝 Travis-CI_ 提供了免費的 
:ruby:`持续整合|Continuous integration` 虛擬機環境，
通過它全自動生成靜態博客成爲了可能。

.. _Travis-CI: https://travis-ci.org/

關於 Travis-CI
----------------------------

`持续整合 <http://zh.wikipedia.org/wiki/%E6%8C%81%E7%BA%8C%E6%95%B4%E5%90%88>`_
原本是 :ruby:`敏捷開發|Agile Development`
或者 :ruby:`極限編程|Extreme Programming` 中提到的概念，大意就是說在開發的過程中，
一旦有微小的變更，就全自動地 **持續** 合併到主線中， **整合** 變更的內容到發佈版本裏。
這裏的 **整合** 實際上可以理解爲 **全自動測試** 加上 **生成最終產品** 。
可以看到 **持續整合** 實際強調 **全自動** ，於是需要有一個服務器不斷地監聽主線開發的變更內容，
一旦有任何變更（可以理解爲 git commit ）就自動調用測試和部署腳本。

於是要用持續整合就需要一個整合服務器，幸而 Travis-CI 對 github 上的公開 repo
提供了免費的整合服務器虛擬機服務，和 github 的整合非常自然。所以我們就可以用它提供的虛擬機
爲博客生成靜態網站。

啓用 Travis-CI 自動編譯 
--------------------------------------------------------

.. panel-default::
  :title: **暫時** 測試的目的下的 :code:`.travis.yml` 

	.. code-block:: yaml

		language: python

		python:
		    - "2.7"

		before_install:
		    - sudo apt-add-repository ppa:chris-lea/node.js -y
		    - sudo apt-get update
		    - sudo apt-get install nodejs ditaa doxygen parallel

		install:
		    - sudo pip install pelican 
		    - sudo pip install jinja2
		    - sudo pip install babel
		    - sudo pip install beautifulsoup4
		    - sudo pip install markdown
		    - sudo npm install -g less
		    - wget "http://downloads.sourceforge.net/project/plantuml/plantuml.jar?r=&ts=1424308684&use_mirror=jaist" -O plantuml.jar
		    - sudo mkdir -p /opt/plantuml
		    - sudo cp plantuml.jar /opt/plantuml
		    - echo "#! /bin/sh" > plantuml
		    - echo 'exec java -jar /opt/plantuml/plantuml.jar "$@"' >> plantuml
		    - sudo install -m 755 -D plantuml /usr/bin/plantuml
		    - plantuml -version
		    - wget https://bintray.com/artifact/download/byvoid/opencc/opencc-1.0.2.tar.gz
		    - tar xf opencc-1.0.2.tar.gz
		    - cd opencc-1.0.2 && make && sudo make install && cd ..
		    - opencc --version
		    - sudo locale-gen zh_CN.UTF-8
		    - sudo locale-gen zh_HK.UTF-8
		    - sudo locale-gen en_US.UTF-8
		    - sudo locale-gen ja_JP.UTF-8
		    - locale -a
		    - pelican --version

		script:
		    - git clone https://github.com/farseerfc/pelican-plugins plugins
		    - git clone https://github.com/farseerfc/pelican-bootstrap3 theme
		    - mkdir output
		    - env SITEURL="farseerfc.me" make publish

這一步很簡單，訪問 https://travis-ci.org/ 並用你的 Github 賬戶登錄，
授權它訪問你的賬戶信息就可以了。然後在 https://travis-ci.org/repositories 裏開啓
需要編譯的 repo ，這樣 Travis-CI 就會監視對這個 repo 的所有 push 操作，並且對
每個 push 調用測試了。

然後在 repo 的根目錄放一個 :code:`.travis.yml` 文件描述編譯的步驟。
**暫時** 測試的目的下我寫的 :code:`.travis.yml` 大概是側邊那樣。

Travis-CI 提供的虛擬機是比較標準的 Ubuntu 12.04 LTS ，打上了最新的補丁，並且根據你指定的
語言選項會把響應的解釋器和編譯器升級到最新版（或者指定的版本）。這裏用 python 語言的配置。
這裏 before_install 和 install 的區別其實不大，任何一個失敗的話算作 build errored 而不是
build fail ，而如果在 script 裏失敗的話算作 build fail 。

這裏爲了編譯模板，我還需要比較新的 less.js ，所以添加了 ppa 裝了個 nodejs 。
還從源碼編譯安裝上了最新版的 opencc ，因爲 Ubuntu 源裏的 opencc 的版本比較老，
然後 doxygen 作爲 opencc 的編譯依賴也裝上了。
其它安裝的東西麼，除了 pelican 之外都是插件們需要的。以及我還需要生成 4 個語言的 locale
所以調用了 4 次 locale-gen 。

寫好 :code:`.travis.yml` 之後把它 push 到 github ，然後 travis 這邊就會自動 clone
下來開始編譯。 travis 上能看到編譯的完整過程和輸出，一切正常的話編譯結束之後
build 的狀態就會變成 passed ，比如我的這次的
https://travis-ci.org/farseerfc/farseerfc/builds/51344614 。

從 Travis-CI 推往 Github 
--------------------------------------------------------

上面的測試編譯通過了之後，下一步自然就是讓 travis-ci 編譯的結果自動推到 Github
發佈出來。要推往 Github 自然需要設置 github 用戶的身份，在本地設置的時候是把
本地的 ssh key 添加到 github 賬戶就可以了，在一切細節都公開了的 travis 上
當然不能放私有 key 。