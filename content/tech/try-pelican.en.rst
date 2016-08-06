Give a try to Pelican
=====================

:slug: try-pelican
:lang: en
:date: 2012-02-24 17:33
:tags: python, pelican
:series: pelican
:issueid: 5

It seems in one night
`all <http://blog.yxwang.me/2011/11/migrated-to-octopress/>`_
`geeks <http://xoyo.name/2012/02/migrate-to-octopress/>`_
have
`their <http://blog.xdite.net/posts/2011/10/07/what-is-octopress/>`_
`own <http://www.yangzhiping.com/tech/octopress.html>`_
`Github User Page <http://pages.github.com/#user__organization_pages>`_
and Octopress_ Blog.
Like everyone posted in their blogs, Static Blog is indeed more convenient than traditional 
Blog systems such as WordPress. I have been wanting my own Octopress_ since then.

.. _Octopress: http://octopress.org/

.. _Pelican: http://pelican.notmyidea.org/en/latest/

But it seems that Octopress_ isn't for me
+++++++++++++++++++++++++++++++++++++++++

At first I was confused  by `Setup Steps of Octopress <http://octopress.org/docs/setup/>`_ .  What is this RVM_ thing? 
And what is that rbenv_ thing? It seems  the high pace of Ruby community has beyond my imagination to a degree that 
they need a version manager to ensure the compatibility of different versions of Ruby. Althrough the same compatibility  
issue also troubles Python community [#]_ , but at least Python don't need a version manager (yet) to control this mass [#]_ .

Real problem for me is that I haven't yet a Linux box that I can play around freely. (I really want one ... ) Both RVM_ and 
rbenv_ needs to run on Unix/Linux/MacOSX. One can not be a geek if he use Windows ? (Maybe it's true...)

Remaining problem is the battle between Ruby and Python campaign.  I haven't tried Markdown_ , and I rather like ReST_ . 
It seems that both sides depend on Pygments_ as code block highlighter so  Rubyists need Python environment anyway. 
I simply don't want to depend on any Ruby component. It is better when it is in pure Python, no C extensions so that I can 
debug into it and make minor modifications.

So I started searching for Static Blog Engine in Python on Github. The author of the great framework Flask_ , mitsuhiko_ , 
wrote a rstblog_ , but it's not well developed. Hyde_ seems to be complete enough, but it use MarkDown_ as its default markup 
language, and the design of its homepage is too fashion to be used as blog. Finally I found Pelican_ .

.. [#] Such as the difference between Python 2.x and 3.x , and also difference in C-API of implementations of PyPy_ , CPython_ , Stackless_ , Cython_ .

.. [#] Yes, we have easy_install_ and pip_ , but all these are package manager, running in a perticular Python implementation. Python implementation itself don't need a manager. Version issue of Python largely have been solved by lightweight converters such as 2to3.py_ and 3to2.py_ , you don't need to store multiple implementations of Python in your disk for different packages. Yes you can use  virtualenv_ if you need to preserve stablility but this is another story.

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

Let it be Pelican_
++++++++++++++++++

For my own use, Pelican_ offers me some advantages over Octopress_:

 #. Implemented in **pure Python**. This means that I can use different implementation of Python other than CPython easily. I use PyPy_ myself.
 #. Translation of multi-languages. The original author of Pelican_ is a France. This is unnecessory for most people, but I will post my blog mainly in three languages: English, Japanese and Chinese.
 #. ReST_ . So that I can use the @auto-rst feature of Leo_ . And also I don't need to switch between my blog and documentation of my projects.

But it seems that Pelican_ was less contributed than Octopress_ . Some minor issues remains in latest version:

 #. Support of pelican-import from WordPress for Chinese and Japanese articles are buggy.
 #. Datetime format, timezone, and locale support for multi-language blogs are not so natural. **I will work on this in these days**
 #. There are not so many templates compared to Octopress_ .
 #. And less plugins .

I hope more people from Python community can contribute to this excellent project, then all these issues will be fixed soon.
 
.. _Leo: http://webpages.charter.net/edreamleo/front.html

My settings
+++++++++++

To install Pelican_ is simple:

.. code-block:: console

    $ pip install pelican

Write posts in ReST_ , with ``rst`` extensions, and put them in ``pages`` folder. (Re)Build all pages is simply:

.. code-block:: console

    $ pelican -s settings.py
    
Push to Github:

.. code-block:: console

    $ git commit -am "Commit message"
    $ git push

And following is my ``settings.py``:

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

