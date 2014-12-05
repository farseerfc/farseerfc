Pyssy 项目
============

:slug: pyssy
:lang: zhs
:date: 2012-04-02 12:42
:tags: python, sjtu, yssy

简介
++++++

Pyssy 是用于 `上海交通大学 饮水思源站 <https://bbs.sjtu.edu.cn>`_ 的一系列 Python 脚本和工具。

Pyssy 被有意设计为既可以托管寄宿在 SAE [#SAE]_ 上，也可以在单机上独立使用。

项目地址： http://pyssy.sinaapp.com/

Github上的源代码地址： https://github.com/yssy-d3/pyssy

.. [#SAE] `Sina App Engine <http://sae.sina.com.cn/>`_ ，新浪云平台，类似 `Google App Engine <https://appengine.google.com/>`_ 的东西。

依赖关系
++++++++++++

Pyssy 使用 `Flask <http://flask.pocoo.org/>`_ 作为网页服务器，
并且使用 Memcached 或者 Redis 作为抓取 *水源Web* 的缓存。

SAE Python 环境下请开启 Memcached 支持。

本地环境下请安装 Redis-py 并运行 redis-server 服务器程序。

