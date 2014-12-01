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
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Blogroll
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
          'http://blog.phoenixlzx.com/static/img/avatar/avatar.jpg',
          '鳳凰菊苣'
          ),
         ('fixme',
          'https://fbq.github.io/',
          'https://avatars3.githubusercontent.com/u/673448',
          '水源技站'
          ),
         ('飲水思源',
          'http://bbs.sjtu.edu.cn/',
          'https://bbs.sjtu.edu.cn/favicon.ico',
          '上海交通大學飲水思源BBS站'
          ),
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

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['tipue_search']

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

DIRECT_TEMPLATES = (('search', 'index', 'categories', 'authors', 'archives',
                    'tags'))

# TWITTER_CARDS = True
# TWITTER_USERNAME = 'farseerfc'
# TWITTER_WIDGET_ID = "538997172142759936"
