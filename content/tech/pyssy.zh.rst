Pyssy 項目
============

:slug: pyssy
:lang: zh
:date: 2012-04-02 12:42
:tags: python, sjtu, yssy
:issueid: 45

簡介
++++++

Pyssy 是用於 `上海交通大學 飲水思源站 <https://bbs.sjtu.edu.cn>`_ 的一系列 Python 腳本和工具。

Pyssy 被有意設計爲既可以託管寄宿在 SAE [#SAE]_ 上，也可以在單機上獨立使用。

項目地址： http://pyssy.sinaapp.com/

Github上的源代碼地址： https://github.com/yssy-d3/pyssy

.. [#SAE] `Sina App Engine <http://sae.sina.com.cn/>`_ ，新浪雲平臺，類似 `Google App Engine <https://appengine.google.com/>`_ 的東西。

依賴關係
++++++++++++

Pyssy 使用 `Flask <http://flask.pocoo.org/>`_ 作爲網頁服務器，
並且使用 Memcached 或者 Redis 作爲抓取 *水源Web* 的緩存。

SAE Python 環境下請開啓 Memcached 支持。

本地環境下請安裝 Redis-py 並運行 redis-server 服務器程序。

