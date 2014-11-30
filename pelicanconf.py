#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'farseerfc'
SITENAME = "Farseerfc's Blog"
SITEURL = ''

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'zh'

DATE_FORMATS = {
    'en': ((u'en_US', 'utf8'), u'%a, %d %b %Y',),
    'zh': ((u'zh_HK', 'utf8'), u'%Y年%m月%d日(週%a)',),
    'zhs': ((u'zh_CN', 'utf8'), u'%Y年%m月%d日(周%a)',),
    'jp': ((u'ja_JP', 'utf8'), u'%Y年%m月%d日(%a)',),
}


DISQUS_SITENAME = 'farseerfcgithub'
GOOGLE_ANALYTICS = 'UA-29540705-1'

TAG_FEED_ATOM = 'feeds/tag-%s.atom.xml'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          )

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/farseerfc'),
          ('github', 'https://github.com/farseerfc'),
          ('facebook', 'http://www.facebook.com/farseerfc'),
          ('weibo', 'http://weibo.com/farseerfc'),
          )


TWITTER_USERNAME = 'farseerfc'

GOOGLE_CUSTOM_SEARCH_SIDEBAR = "001578481551708017171:axpo6yvtdyg"
GOOGLE_CUSTOM_SEARCH_NAVBAR = "001578481551708017171:hxkva69brmg"


DEFAULT_PAGINATION = 4


STATIC_PATHS = ['static']


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = "../pelican-bootstrap3"

# Theme options
DOCUTIL_CSS = True
PYGMENTS_STYLE = 'monokai'
GITHUB_USER = 'farseerfc'
GITHUB_SHOW_USER_LINK = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
CC_LICENSE = "CC-BY-NC-SA"
DISPLAY_TAGS_INLINE = True