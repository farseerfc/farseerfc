尝试一下 Pelican
====================

:slug: try-pelican
:lang: zhs
:date: 2012-02-24 17:33
:tags: python, pelican

似乎一夜之间所有的
`极客们 <http://blog.yxwang.me/2011/11/migrated-to-octopress/>`_
`都 <http://xoyo.name/2012/02/migrate-to-octopress/>`_
`有了 <http://blog.xdite.net/posts/2011/10/07/what-is-octopress/>`_
`自己 <http://www.yangzhiping.com/tech/octopress.html>`_
的 `Github主页 <http://pages.github.com/#user__organization_pages>`_
和 Octopress_ 博客。就像所有人在他们的博客中指出的，静态博客的确比传统的WordPress方式具有更多优势。 自从看到这些
我就一直在想着自己搭一个 Octopress_ 。

.. _Octopress: http://octopress.org/

.. _Pelican: http://pelican.notmyidea.org/en/latest/

但是似乎 Octopress_ 不适合我
++++++++++++++++++++++++++++++++++++

一上手就被 `Octopress的搭建步骤 <http://octopress.org/docs/setup/>`_ 烦到了。 RVM_ 是什么？ rbenv_ 又是什么？
看来 Ruby 社区的快节奏发展已经超过了我的想象，他们似乎需要一套发行版管理器来调和不同版本之间的 Ruby 的兼容性问题。
虽然同样的兼容性问题在 Python 社区也有 [#]_ ，不过总觉得 Python 至少还没到需要一个发行版管理器的程度 [#]_ 。

真正的问题是我手上还没有一个可以让我随便玩的 Linux 环境（真的想要……）。 而无论是 RVM_ 还是 rbenv_ 似乎都只支持 Unix/Linux/MacOSX 。 身为极客就注定不能用 Windows 么？（或许是的……）。

剩下的问题就是 Ruby 和 Python 两大阵营的对立问题了。我不熟悉 Markdown_ ， 相对来说比较喜欢 ReST_ 。 似乎无论哪边都要
依赖 Pygments_ 作为代码着色器，那么其实 Rubyist 也至少需要安装 Python 。 我倾向于不依赖任何 Ruby 组件，最好没有 C 扩展
的纯 Python 实现。

于是我开始在 Github 上找 Python 的静态博客引擎。 Flask_ 的作者 mitsuhiko_ 写的 rstblog_ 看起来不错，不过似乎没有多少人在用。 Hyde_ 似乎很完善，不过默认的标记语言是 MarkDown ， 又依赖于几个 Ruby 组建，而且官方网站的设计实在太前卫。 最终我看到了 Pelican_ 。

.. [#] 比如 Python 2.x 与 3.x 之间看似难以跨越的鸿沟，以及 PyPy_ 、 CPython_ 、 Stackless_ 、 Cython_ 等各个实现之间的微妙差别。

.. [#] 是的，我们有 easy_install_ ，我们有 pip_ ， 不过这些都是包管理器，都是装好特定的Python实现之后的事情。 Python实现本身还不需要包管理器来管理。 Python 的版本问题基本上也只需要 2to3.py_ 和 3to2.py_ 这样的轻量级转换器就可以了，你不需要为了安装多个软件而在硬盘里留下多个不同版本的 Python 。 如果为了引用的稳定性，你可以用 virtualenv_ ，不过这又是另一回事情了。

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

那么就 Pelican_ 吧
++++++++++++++++++++++

对我而言， Pelican_ 相比于 Octopress_ 有几个好处：

 #. 纯 Python 实现。 这意味着我可以换用任何 Python 解释器而不必担心兼容性问题。比如我就换成了 PyPy_。
 #. 多语言支持。因为 Pelican_ 的作者似乎是个法国人。不过这个似乎大部分人不需要…… 我是想尽量把一篇博客写成三种语言作为锻炼吧。
 #. ReST_ 。这样我就可以用 Leo_ 的 @auto-rst 直接写 ReST了。简单方便快捷有效。
 
不过似乎 Pelican_ 的关注度不如 Octopress_ 那么高，现在一些部分还有细微的问题：

 #. pelican-import 从 WordPress 导入的时候对中文、日文的支持似乎很成问题。
 #. 日期格式、时区、字符集、和多语言功能的结合度还不够。  **我在尝试改善它。**
 #. 模板还不够丰富。
 #. 插件也不够多……

希望这么优秀的工具能够受到更多关注，以上这些问题都是增加关注度之后很快就能解决的问题。
 
.. _Leo: http://webpages.charter.net/edreamleo/front.html

我的设置 settings.py
++++++++++++++++++++++++

安装 Pelican_ 很容易，一句话就够了：

.. code-block:: console

    $ pip install pelican

然后把文章写成ReST的格式，放在`pages`文件夹里面。(重新)生成只要：


.. code-block:: console

    $ pelican -s settings.py
    
上传到 Github:

.. code-block:: console

    $ git commit -am "Commit message"
    $ git push

就这么简单。附上我的配置文件：

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

