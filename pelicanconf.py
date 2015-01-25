#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from hashlib import md5
from os import getenv

AUTHOR = 'farseerfc'
SITENAME = "Farseerfc的小窩"
SITEURL = '//' + getenv("SITEURL", default='localhost:8000')

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'zh'
LOCALE = 'zh_HK.utf8'

DATE_FORMATS = {
    'en': ((u'en_US', 'utf8'), u'%a, %d %b %Y',),
    'zh': ((u'zh_HK', 'utf8'), u'%Y年%m月%d日(週%a)',),
    'zhs': ((u'zh_CN', 'utf8'), u'%Y年%m月%d日(周%a)',),
    'jp': ((u'ja_JP', 'utf8'), u'%Y年%m月%d日(%a)',),
}


DISQUS_SITENAME = 'farseerfcgithub'
DISQUS_DISPLAY_COUNTS = True
GOOGLE_ANALYTICS = 'UA-29540705-1'


TAG_FEED_ATOM = None
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

LINKS = (('lilydjwg',
          'http://lilydjwg.is-programmer.com/',
          'https://upload.wikimedia.org/wikipedia/commons/0/03/Vulpes_vulpes_laying_in_snow.jpg',
          '依雲（aka. 百合仙子）'),
         ('felixonmars',
          'http://blog.felixc.at/',
          'https://www.gravatar.com/avatar/48b2061f9e9a00023417bc1174532e81',
          '火星貓大大'),
         ('phoenixlzx',
          'http://blog.phoenixlzx.com/',
          'https://www.gravatar.com/avatar/' +
          md5(b"i@phoenixlzx.com").hexdigest(),
          '鳳凰菊苣'
          ),
         ('fixme',
          'https://fbq.github.io/',
          'https://avatars3.githubusercontent.com/u/673448',
          '水源技站'
          ),
         ('quininer',
          'http://quininer.github.io/',
          'https://www.gravatar.com/avatar/' +
          md5(b"quininer@live.com").hexdigest(),
          '純JavaScript的帥氣博客'
          ),
         ('acgtyrant',
          'http://acgtyrant.com/',
          'https://www.gravatar.com/avatar/' +
          md5(b"acgtyrant@gmail.com").hexdigest(),
          '御宅暴君，維護這個人和Arch兩個博客'
          ),
         ('飲水思源',
          'http://bbs.sjtu.edu.cn/',
          'https://bbs.sjtu.edu.cn/favicon.ico',
          '上海交通大學飲水思源BBS站'
          ),
         )

TWITTER_USERNAME = 'farseerfc'

DEFAULT_PAGINATION = 6

STATIC_PATHS = ['static', 'images', 'uml', 'images/favicon.ico']
EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'}
}

PLUGIN_PATHS = ['../pelican-plugins']
THEME = "../pelican-bootstrap3"


I18N_SUBSITES = {
    'jp': dict(
        LOCALE='ja_JP.utf8',
        SITENAME="Farseerfcの居場所"
    ),
    'en': dict(
        LOCALE='en_US.utf8',
        SITENAME="Farseerfc's Blog"
    ),
    'zhs': dict(
        LOCALE='zh_CN.utf8',
        SITENAME="Farseerfc的小窝"
    ),
}
I18N_UNTRANSLATED_ARTICLES = "remove"

PLUGINS = ["i18n_subsites",
           "plantuml",
           "youku",
           "youtube",
           'tipue_search',
           'neighbors',
           'series',
           'bootstrapify',
           'twitter_bootstrap_rst_directives',
           "render_math",
           'extract_toc',
           'summary']

USE_LESS = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Theme options

JINJA_EXTENSIONS = ['jinja2.ext.i18n']

DOCUTIL_CSS = True
TYPOGRIFY = False
PYGMENTS_STYLE = 'monokai'
GITHUB_USER = 'farseerfc'
GITHUB_SHOW_USER_LINK = True
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
CC_LICENSE = "CC-BY-NC-SA"
DISPLAY_TAGS_INLINE = True
OUTPUT_SOURCES = True
OUTPUT_SOURCES_EXTENSION = '.rst'

DIRECT_TEMPLATES = (('search', 'index', 'categories', 'authors', 'archives',
                     'tags'))

TWITTER_USERNAME = 'farseerfc'
TWITTER_WIDGET_ID = "538997172142759936"

AVATAR = 'images/avatar.jpg'
ABOUT_PAGE = "pages/about.html"
ABOUT_ME = """<h3 style="text-align:center">
<a href="https://twitter.com/farseerfc"                  target="_blank">
<i class="fa fa-twitter" style="text-align:center"></i></a>
<a href="https://github.com/farseerfc"                   target="_blank">
<i class="fa fa-github" style="text-align:center"></i></a>
<a href="http://weibo.com/farseerfc"                     target="_blank">
<i class="fa fa-weibo" style="text-align:center"></i></a>
<a href="http://www.facebook.com/farseerfc"              target="_blank">
<i class="fa fa-facebook" style="text-align:center"></i></a>
<a href="https://plus.google.com/u/0/+JiachenYang/posts" target="_blank">
<i class="fa fa-google-plus" style="text-align:center"></i></a>
<a href="mailto:farseerfc@gmail.com" target="_blank">
<i class="mdi-communication-email" style="text-align:center"></i></a>
</h3>
"""
