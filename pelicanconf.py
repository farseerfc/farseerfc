#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
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
    'jp': ((u'ja_JP', 'utf8'), u'%Y年%m月%d日(%a曜日)',),
}


DISQUS_SITENAME = 'farseerfcgithub'
DISQUS_DISPLAY_COUNTS = True
GOOGLE_ANALYTICS = 'UA-29540705-1'


TAG_FEED_ATOM = None
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

DEFAULT_PAGINATION = 12

STATIC_PATHS = ['static',
                'images',
                'uml',
                'images/favicon.ico',
                'static/CNAME']

EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
    'static/CNAME': {'path': 'CNAME'},
    'static/robots.txt': {'path': 'robots.txt'},
    'static/manifest.json': {'path': 'manifest.json'},
    'static/browserconfig.xml': {'path': 'browserconfig.xml'},
    'static/keybase.txt': {'path': 'keybase.txt'},
    'static/cinderella-avatar.html.redirect': {'path': 'cinderella-avatar.html'},
    'static/hoshiiroyozora.html.redirect': {'path': 'hoshiiroyozora.html'},
    'static/iwakutsuki-no-ensho.html.redirect': {'path': 'iwakutsuki-no-ensho.html'},
    'static/kachoufuugetsu.html.redirect': {'path': 'kachoufuugetsu.html'},
    'static/karakurenawi-no-kage.html.redirect': {'path': 'karakurenawi-no-kage.html'},
    'static/miserable-no-shizuku.html.redirect': {'path': 'miserable-no-shizuku.html'},
    'static/opposite-world.html.redirect': {'path': 'opposite-world.html'},
    'static/sakuya-oyafukou-na-ningen-no-ohanashi.html.redirect': {'path': 'sakuya-oyafukou-na-ningen-no-ohanashi.html'},
    'static/suika.html.redirect': {'path': 'suika.html'},
    'static/takenohana.html.redirect': {'path': 'takenohana.html'},
    'static/tsukimizakura.html.redirect': {'path': 'tsukimizakura.html'},
    'static/ukiyomichi.html.redirect': {'path': 'ukiyomichi.html'},
    'static/warabeasobi.html.redirect': {'path': 'warabeasobi.html'},
    'static/yozakuranikimiwokakushite.html.redirect': {'path': 'yozakuranikimiwokakushite.html'},
    'static/zankyohanariyamazu.html.redirect': {'path': 'zankyohanariyamazu.html'},
}

PAGE_URL = "{id}.html"
PAGE_SAVE_AS = "{id}.html"
PAGE_LANG_URL = '{lang}/{id}.html'
PAGE_LANG_SAVE_AS = '{lang}/{id}.html'
ARTICLE_URL = '{id}.html'
ARTICLE_SAVE_AS = '{id}.html'
ARTICLE_LANG_URL = '{lang}/{id}.html'
ARTICLE_LANG_SAVE_AS = '{lang}/{id}.html'


PLUGIN_PATHS = ['plugins']
THEME = "theme"

SLUGIFY_SOURCE='basename'
# FILENAME_METADATA = r'(?P<slug>[^.]*)\.(?P<lang>[^.]*)'

I18N_SUBSITES = {
    'jp': dict(
        LOCALE='ja_JP.utf8',
        SITENAME="Farseerfcの巣",
        STATIC_PATHS=STATIC_PATHS
    ),
    'en': dict(
        LOCALE='en_US.utf8',
        SITENAME="Farseerfc's Nest",
        STATIC_PATHS=STATIC_PATHS
    ),
    'zhs': dict(
        LOCALE='zh_CN.utf8',
        SITENAME="Farseerfc的小窝",
        STATIC_PATHS=STATIC_PATHS
    ),
}
I18N_UNTRANSLATED_ARTICLES = "remove"
I18N_TEMPLATES_LANG="en"

MARKDOWN = {'extension_configs': {
    'admonition': {},
    'toc': {},
    'codehilite': {'css_class': 'highlight', 'linenums': False },
    'extra': {}
    }}

PLUGINS = ["i18n_subsites",
           "better_codeblock_line_numbering",
           "plantuml",
           "youku",
           "youtube",
           'tipue_search',
        #    'neighbors',
           'series',
           'bootstrapify',
           'twitter_bootstrap_rst_directives',
           "render_math",
           'extract_toc',
           'tag_cloud',
           'sitemap',
           'summary']

SITEMAP = {
    'format': 'xml',
}

USE_LESS = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
CHECK_MODIFIED_METHOD = "md5"
LOAD_CONTENT_CACHE = True
CACHE_CONTENT = True

# Theme options

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

DOCUTILS_SETTINGS = {'table_style': 'borderless'}

DOCUTIL_CSS = True
TYPOGRIFY = False
PYGMENTS_STYLE = 'monokai'
GITHUB_USER = 'farseerfc'
GITHUB_SHOW_USER_LINK = True
GITHUB_REPO = 'farseerfc/farseerfc.github.io'
OTHER_BLOG = 'https://sak.uy/'
OTHER_BLOG_TITLE = 'Sakuya的音樂盒'
DISPLAY_BREADCRUMBS = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
CC_LICENSE = "CC-BY-NC-SA"
DISPLAY_TAGS_INLINE = True
OUTPUT_SOURCES = True
OUTPUT_SOURCES_EXTENSION = '.rst'

# WEIBO_WIDGET = True
# WEIBO_APPKEY = "NANnN"
# WEIBO_APPKEYN = "498769639"

DIRECT_TEMPLATES = (('search', 'index', 'categories', 'authors', 'archives',
                     'tags'))

# TWITTER_USERNAME = 'farseerfc'
# TWITTER_WIDGET_ID = "538997172142759936"

AVATAR = 'images/avatar.jpg'
ABOUT_PAGE = "about.html"
ABOUT_ME = """<h3 style="text-align:center">
<a href="https://sak.uy/"                  target="_blank">
<i class="fa fa-music" style="text-align:center"></i></a>
<a href="https://twitter.com/farseerfc"                  target="_blank">
<i class="fa fa-twitter" style="text-align:center"></i></a>
<a href="https://github.com/farseerfc"                   target="_blank">
<i class="fa fa-github" style="text-align:center"></i></a>
<a href="http://www.facebook.com/farseerfc"              target="_blank">
<i class="fa fa-facebook" style="text-align:center"></i></a>
<a href="https://plus.google.com/u/0/+JiachenYang/posts" target="_blank">
<i class="fa fa-google-plus" style="text-align:center"></i></a>
<a href="mailto:farseerfc@gmail.com" target="_blank">
<i class="mdi-communication-email" style="text-align:center"></i></a>
</h3>
"""

# SIDEBAR_PROMOTION = """<a href="https://www.vultr.com/?ref=6924747-3B">
# <img src="https://www.vultr.com/media/banner_4.png" width="160" height="600">
# </a>"""
