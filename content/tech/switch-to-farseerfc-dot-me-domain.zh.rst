換到 farseerfc.me 域名
=======================================

:slug: switch-to-farseerfc-dot-me-domain
:lang: zh
:date: 2015-01-26 23:32
:tags: pelican, domain, cloudflare, github
:series: pelican
:issueid: 48


上個月就在 :ruby:`狗爹|godaddy` 上買了個自己的域名 :code:`farseerfc.me` 準備用在這個
博客上，當時試着轉到過這個域名，發現 :ruby:`自定義域名|custom domain` 
只支持 http 不支持 https ，想着還要買自己的證書，於是就扔在了一旁。不用自定義域名的話，
放在 github.io 上是可以用 HTTPS 的。
今天在 :irc:`archlinux-cn` 上受大牛 :fref:`quininer` 和 :fref:`lilydjwg` 點播，
發現 cloudflare 有提供
`免費的支持 SSL 的 CDN 服務 <https://blog.cloudflare.com/introducing-universal-ssl/>`_
趕快去申請了一個，感覺非常讚，於是就換過來了。

設置的方法按照 `這篇博文 <https://me.net.nz/blog/github-pages-secure-with-cloudflare/>`_
說的一步步做下來，如它所述，用 CloudFlare 的優點如下：

#. CDN 加速
#. SSL (HTTPS) 加密
#. 支持 SPDY 協議
#. 支持 IPv6 

.. label-warning::

    **2015年12月29日更新**

現在不光支持 SPDY 而且支持 HTTP/2 了。

然後 **免費賬戶** 的一些缺點有：

#. CloudFlare 和 github.io 之間的數據不是加密的，因爲 github
   :ruby:`自定義域名|custom domain` 還不支持使用自己的證書。這也是一開始我沒用
   自定義域名的原因嘛，這沒有辦法……
#. CloudFlare 給免費賬戶簽名的 SSL 證書比較新，不支持一些老的設備和瀏覽器，比如不支持
   老的 XP 系統的 IE 或者 2.x 的 Android。這種情況下沒辦法只能用沒有加密的 HTTP 了。
#. 不支持 `HSTS 頭 <https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security>`_
   ，所以不能從服務器這邊強制瀏覽器用 HTTPS。當然可以放個 javascript 跳轉，
   也可以用 `HTTPSEverywhere <https://www.eff.org/https-everywhere>`_ 這種方案。

.. label-warning::

    **2015年12月29日更新**

如評論中 `提到的 <http://farseerfc.me/switch-to-farseerfc-dot-me-domain.html#comment-2015037231>`_
現在支持 HSTS 了。

設置步驟 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

基本按照默認的選項下一步就可以了。

#. 和那個博主一樣我把 :ruby:`安全級別|Security profile` 降到了 Low ，即使是可疑流量也
   不會要求輸入 CAPTCHA 。
#. 把 SSL 方式開在 Flexible SSL，訪客到 CloudFlare 是加密的，而 CloudFlare 到 
   github.io 是不加密的。
#. 把 CDN 開到了 CDT+Full Optimization ，可以對訪問加速。由於是完全靜態的博客，沒有
   動態變化的內容，所以應該比較安全。
#. 服務器設置的一步需要將 :ruby:`域名解析服務器|DNS nameservers` 從狗爹的服務器改到
   CloudFlare 的，如下圖：

.. figure:: {filename}/images/godaddy.png
    :alt: 更改狗爹的域名服務器

    更改狗爹的域名服務器

申請好之後就由 CloudFlare 接管域名解析了，接下來在 CloudFlare 的 DNS 設置添加一條
`A 類規則指向 github pages 的 IP <https://help.github.com/articles/tips-for-configuring-an-a-record-with-your-dns-provider/>`_ 。

.. figure:: {filename}/images/cloudflaredns.png
    :alt: 更改CloudFlare的DNS規則

    更改CloudFlare的DNS規則

等一切都反映到 DNS 服務器上就設置完成了，接下來給 
`farseerfc.github.io push 一個 CNAME 文件 <https://help.github.com/articles/adding-a-cname-file-to-your-repository/>`_
寫上我的域名就可以了。我用 Makefile 配合我的 pelican 配置做這個：

.. code-block:: Makefile

    publish: rmdrafts cc clean theme
      [ ! -d $(OUTPUTDIR) ] || find $(OUTPUTDIR) -mindepth 1 -not -wholename "*/.git*" -delete
      rm -rf cache
      echo $(SITEURL) > content/static/CNAME
      $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
      $(MAKE) rsthtml

    github:
      (cd $(OUTPUTDIR) && git checkout master)
      env SITEURL="farseerfc.me" $(MAKE) publish
      (cd $(OUTPUTDIR) && git add . && git commit -m "update" && git push)

.. code-block:: python

    SITEURL = '//' + getenv("SITEURL", default='localhost:8000')
    STATIC_PATHS = ['static', 'images', 'uml', 'images/favicon.ico', 'static/CNAME']
    EXTRA_PATH_METADATA = {
        'images/favicon.ico': {'path': 'favicon.ico'},
        'static/CNAME': {'path': 'CNAME'}
    }

然後把生成的靜態網站 push 到 github 之後可以從項目設置裏看到域名的變化：

.. figure:: {filename}/images/githubdomain.png
    :alt: Github 配置好自定義域名之後的變化

    Github 配置好自定義域名之後的變化

最後把Disqus的評論也遷移到新的域名，disqus有方便的遷移嚮導，一直下一步就可以了。

這樣就一切都設置妥當了。

致謝
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

最後要感謝提供消息的 :fref:`quininer` 和 :fref:`lilydjwg` ，感謝撰寫設置步驟的
*Jonathan J Hunt* ， 感謝 CloudFlare 提供免費 SSL CDN 服務，感謝 Github 提供
方便免費的 Pages 託管。
