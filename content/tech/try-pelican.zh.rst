嘗試一下 Pelican
====================

:slug: try-pelican
:lang: zh
:date: 2012-02-24 17:33
:tags: python, pelican
:series: pelican
:issueid: 5

似乎一夜之間所有的
`極客們 <http://blog.yxwang.me/2011/11/migrated-to-octopress/>`_
`都 <http://xoyo.name/2012/02/migrate-to-octopress/>`_
`有了 <http://blog.xdite.net/posts/2011/10/07/what-is-octopress/>`_
`自己 <http://www.yangzhiping.com/tech/octopress.html>`_
的 `Github主頁 <http://pages.github.com/#user__organization_pages>`_
和 Octopress_ 博客。就像所有人在他們的博客中指出的，靜態博客的確比傳統的WordPress方式具有更多優勢。 自從看到這些
我就一直在想着自己搭一個 Octopress_ 。

.. _Octopress: http://octopress.org/

.. _Pelican: http://pelican.notmyidea.org/en/latest/

但是似乎 Octopress_ 不適合我
++++++++++++++++++++++++++++++++++++

一上手就被 `Octopress的搭建步驟 <http://octopress.org/docs/setup/>`_ 煩到了。 RVM_ 是什麼？ rbenv_ 又是什麼？
看來 Ruby 社區的快節奏發展已經超過了我的想象，他們似乎需要一套發行版管理器來調和不同版本之間的 Ruby 的兼容性問題。
雖然同樣的兼容性問題在 Python 社區也有 [#]_ ，不過總覺得 Python 至少還沒到需要一個發行版管理器的程度 [#]_ 。

真正的問題是我手上還沒有一個可以讓我隨便玩的 Linux 環境（真的想要……）。 而無論是 RVM_ 還是 rbenv_ 似乎都只支持 Unix/Linux/MacOSX 。 身爲極客就註定不能用 Windows 麼？（或許是的……）。

剩下的問題就是 Ruby 和 Python 兩大陣營的對立問題了。我不熟悉 Markdown_ ， 相對來說比較喜歡 ReST_ 。 似乎無論哪邊都要
依賴 Pygments_ 作爲代碼着色器，那麼其實 Rubyist 也至少需要安裝 Python 。 我傾向於不依賴任何 Ruby 組件，最好沒有 C 擴展
的純 Python 實現。

於是我開始在 Github 上找 Python 的靜態博客引擎。 Flask_ 的作者 mitsuhiko_ 寫的 rstblog_ 看起來不錯，不過似乎沒有多少人在用。 Hyde_ 似乎很完善，不過默認的標記語言是 MarkDown ， 又依賴於幾個 Ruby 組建，而且官方網站的設計實在太前衛。 最終我看到了 Pelican_ 。

.. [#] 比如 Python 2.x 與 3.x 之間看似難以跨越的鴻溝，以及 PyPy_ 、 CPython_ 、 Stackless_ 、 Cython_ 等各個實現之間的微妙差別。

.. [#] 是的，我們有 easy_install_ ，我們有 pip_ ， 不過這些都是包管理器，都是裝好特定的Python實現之後的事情。 Python實現本身還不需要包管理器來管理。 Python 的版本問題基本上也只需要 2to3.py_ 和 3to2.py_ 這樣的輕量級轉換器就可以了，你不需要爲了安裝多個軟件而在硬盤裏留下多個不同版本的 Python 。 如果爲了引用的穩定性，你可以用 virtualenv_ ，不過這又是另一回事情了。

.. _RVM: http://beginrescueend.com/

.. _rbenv: https://github.com/sstephenson/rbenv

.. _PyPy: http://pypy.org/

.. _CPython: http://python.org/

.. _Stackless: http://www.stackless.com/

.. _Cython: http://cython.org/

.. _easy_install: http://packages.python.org/distribute/easy_install.html

.. _pip: http://www.pip-installer.org/en/latest/index.html

.. _2to3.py: http://docs.python.org/release/3.0.1/library/2to3.html

.. _3to2.py: http://www.startcodon.com/wordpress/?cat=8

.. _virtualenv: http://pypi.python.org/pypi/virtualenv

.. _Markdown: http://daringfireball.net/projects/markdown/

.. _ReST: http://docutils.sourceforge.net/rst.html

.. _Pygments: http://pygments.org/

.. _Flask: http://flask.pocoo.org/

.. _mitsuhiko: https://github.com/mitsuhiko

.. _rstblog: https://github.com/mitsuhiko/rstblog

.. _Hyde: http://ringce.com/hyde

那麼就 Pelican_ 吧
++++++++++++++++++++++

對我而言， Pelican_ 相比於 Octopress_ 有幾個好處：

 #. 純 Python 實現。 這意味着我可以換用任何 Python 解釋器而不必擔心兼容性問題。比如我就換成了 PyPy_。
 #. 多語言支持。因爲 Pelican_ 的作者似乎是個法國人。不過這個似乎大部分人不需要…… 我是想儘量把一篇博客寫成三種語言作爲鍛鍊吧。
 #. ReST_ 。這樣我就可以用 Leo_ 的 @auto-rst 直接寫 ReST了。簡單方便快捷有效。
 
不過似乎 Pelican_ 的關注度不如 Octopress_ 那麼高，現在一些部分還有細微的問題：

 #. pelican-import 從 WordPress 導入的時候對中文、日文的支持似乎很成問題。
 #. 日期格式、時區、字符集、和多語言功能的結合度還不夠。  **我在嘗試改善它。**
 #. 模板還不夠豐富。
 #. 插件也不夠多……

希望這麼優秀的工具能夠受到更多關注，以上這些問題都是增加關注度之後很快就能解決的問題。
 
.. _Leo: http://webpages.charter.net/edreamleo/front.html

我的設置 settings.py
++++++++++++++++++++++++

安裝 Pelican_ 很容易，一句話就夠了：

.. code-block:: console

    $ pip install pelican

然後把文章寫成ReST的格式，放在`pages`文件夾裏面。(重新)生成只要：


.. code-block:: console

    $ pelican -s settings.py
    
上傳到 Github:

.. code-block:: console

    $ git commit -am "Commit message"
    $ git push

就這麼簡單。附上我的配置文件：

.. code-block:: python
    
    # -*- coding: utf-8 -*-
    
    TIMEZONE = 'Asia/Tokyo'
    
    DATE_FORMATS = {
        'en':('usa','%a, %d %b %Y'),
        'zh':('chs','%Y-%m-%d, %a'),
        'jp':('jpn','%Y/%m/%d (%a)'),
    }
    # windows locale: http://msdn.microsoft.com/en-us/library/cdax410z%28VS.71%29.aspx
    LOCALE = ['usa', 'chs', 'jpn',        # windows
              'en_US', 'zh_CN', 'ja_JP']  # Unix/Linux
    DEFAULT_LANG = 'zh'
    
    SITENAME = 'Farseerfc Blog'
    AUTHOR = 'Jiachen Yang'
    
    DISQUS_SITENAME = 'farseerfcgithub'
    GITHUB_URL = 'https://github.com/farseerfc'
    SITEURL = 'http://farseerfc.github.com'
    TAG_FEED  = 'feeds/%s.atom.xml'
    
    SOCIAL = (('twitter', 'http://twitter.com/farseerfc'),
              ('github', 'https://github.com/farseerfc'),
              ('facebook', 'http://www.facebook.com/farseerfc'),
              ('weibo', 'http://weibo.com/farseerfc'),
              ('renren', 'http://www.renren.com/farseer'),
              )
              
    
    TWITTER_USERNAME = 'farseerfc'
    
    THEME='notmyidea'
    CSS_FILE = "wide.css"
    
    DEFAULT_CATEGORY ='Others'
    OUTPUT_PATH = '.'
    PATH = 'posts'

