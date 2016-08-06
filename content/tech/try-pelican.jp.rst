Pelicanを試してみた
=========================

:slug: try-pelican
:lang: jp
:date: 2012-02-24 17:33
:tags: python, pelican
:series: pelican
:issueid: 5

一日の間に全ての
`ギーク <http://blog.yxwang.me/2011/11/migrated-to-octopress/>`_
`たち <http://xoyo.name/2012/02/migrate-to-octopress/>`_
`が <http://blog.xdite.net/posts/2011/10/07/what-is-octopress/>`_
`自分の <http://www.yangzhiping.com/tech/octopress.html>`_
`Githubユーザーページ <http://pages.github.com/#user__organization_pages>`_
と Octopress_ ブログを導入したような気がします。皆がブログに書いた通りに、静的ブログは確かに WordPress 
などの従来の動的ブログ・エンジンより便利だと思います。これらブログを見ると、私も自分の Octopress_ ブログを立ちましょう
とずっと思っています。

.. _Octopress: http://octopress.org/

.. _Pelican: http://pelican.notmyidea.org/en/latest/

ですが Octopress_ は私に向いてないかも
+++++++++++++++++++++++++++++++++++++++++++++++++++

初めのところに `Octopressの配置手順 <http://octopress.org/docs/setup/>`_ に迷わされた。 
RVM_ とはなに？ rbenv_ とは何のこと？見るところ Ruby コミュニティーの発展するハイペースは既に私の想像に超えましたみたい。
彼らは Ruby の各バージョン間に互換性を持つために、バージョン管理が必要らしいです。同様の互換性問題が Python コミュニティーにもある
ですが [#]_ 、 Python は今のところこのようなバージョン管理の必要がないと思います [#]_ 。

実際に迷惑したのは、私は今自由に持って遊べる Linux 環境が持っていないということ（ほしいなぁ……）。 ですが RVM_ それとも rbenv_ 両方も Unix/Linux/MacOSX しか実行できないらしいです。ギークとしたの皆は絶対に Windows つかっじゃいけないんですか？（本当かも……）。

残りは Ruby と Python の争いです。私は Markdown_ に詳しくない、比べると ReST_ のほうが私に向いています。それに、どっちでも Pygments_ を依存しシンタックス・ハイライトをしているから、 Rubyist 達も少なくとも Python を入れなきゃダメみたいです。 私の好みは一切の Ruby コンポーネントを頼らず、 C 拡張もない純粋な Python の実現がほしいです。

そこから Github に Python で実現した静的ブログ・エンジンを探し始めた。 Flask_ の作者である mitsuhiko_ 氏が書いた rstblog_ が素晴らしいが、あんまり他人に使われていないようです。 Hyde_ は多く使われているけれと、ホームページにブログの感じがみえないです。最後に Pelican_ を見かけました。

.. [#] 例えば Python 2.x と 3.x の間にあまりにも巨大なる差、それと PyPy_ 、 CPython_ 、 Stackless_ 、 Cython_ など各実現間に微妙な違いがあります。

.. [#] はい、こっちに easy_install_ とか pip_ があります、ですがそれらはパッケージ管理、特定なPython環境を入れた後の話です。Python自身はまだ管理する必要がないです。 Python のバージョン問題も 2to3.py_ とか 3to2.py_ のようなツールで変換すればいいです、違うソフトを実行するためたくさんの Python バージョンを残る必要はないです。もしバージョンの違いが気にするなら virtualenv_ を使うのも構わないが、それも別のことです。

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

それでは Pelican_ にしよう
++++++++++++++++++++++++++++++++++

私自身にとって、 Pelican_ は Octopress_ よりいいところ：

 #. 純粋な Python で実現した。ですから CPython_ のほかべつの実現を使うのも心配がない。例えばわたしは PyPy_　を使ています。
 #. 多言語。Pelican_ の原作者はフランス人らしいです。ほとんどの人はこれの必要がないと思うが……できるだけ、わたしは三つの言語で書く。
 #. ReST_ 。それなら Leo_ の ``@auto-rst`` を使って直接 ReST_ をかけます。

でも Pelican_ は Octopress_ のほど注目されていないから、一部問題があります。

 #. pelican-import は WordPress から導入する時、日本語や中国語は問題となります。
 #. 多言語の機能と日付、タイムゾーンなどにバグがある。  **私は改善しています。**
 #. テンプレートは少ない。
 #. プラグインも少ない……

こんなに優れたツールにもっと注目されてほしい。
 
.. _Leo: http://webpages.charter.net/edreamleo/front.html

配置
++++++

Pelican_ を入れるのは簡単：

.. code-block:: console

    $ pip install pelican

文章を ReST_ で書いて、 ``posts`` フォルダーに置きます。ページを生成する：

.. code-block:: console

    $ pelican -s settings.py
    
Github　に送る:

.. code-block:: console

    $ git commit -am "Commit message"
    $ git push

私の配置ファイル：

.. code-block:: python
    
    # -*- coding: utf-8 -*-
    
    TIMEZONE = 'Asia/Tokyo'
    
    DATE_FORMATS = {
        'en':('usa','%a, %d %b %Y'),
        'zh':('chs','%Y-%m-%d, %a'),
        'jp':('jpn','%Y年%m月%d日(%a)'),
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

