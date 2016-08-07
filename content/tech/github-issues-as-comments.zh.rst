啓用 GitHub Issue 作爲博客留言系統
====================================================

:slug: github-issues-as-comments
:lang: zh
:date: 2016-08-07 16:28
:tags: pelican, github, pages, issues
:series: pelican
:issueid: 52


從今天起本博客將啓用 GitHub Issue 作爲留言系統。
原本使用的 Disqus 將繼續保留一段時間，目前沒有關閉的計劃。

換用 GitHub Issue 是計劃了好久的事情了，最初重做這個主題的時候就有考慮過。
這個想法的契機是看到了這篇
`GitHub hosted comments for GitHub hosted blogs <http://ivanzuzak.info/2011/02/18/github-hosted-comments-for-github-hosted-blogs.html>`_
，然後立馬覺得這個想法很符合寄宿在 GitHub Pages 上的博客。
一個限制是要求評論者必須有 GitHub
賬戶，考慮到我的博客的受衆這個要求估計不算太過分。
使用 GitHub Issue 的好處麼，比如自帶的 GFMD
富文本格式，郵件通知，還有訂閱和取消訂閱通知，郵件回復，
這些方面都不比第三方留言系統遜色。

換用 GitHub Issue 另一方面原因是最近聽說 Disqus
被部分牆了，想必以後牆也會越來越高。之前曾經試過在這個博客換上多說，
然而效果我並不喜歡，多說喜歡侵入頁面加很多奇怪的東西，比如用戶的頭像通常是
http 的……也試過結合新浪微博的評論，而新浪微博越來越封閉，API 也越來越不靠譜。

使用 GitHub Issue 作爲評論的方式比較簡單，上面那篇博客裏面提到了，代碼量不比
加載 Disqus 多多少，而且沒有了 iframe 的困擾，唯一麻煩的地方就是要稍微設計一下佈局方式讓它融入
現有的頁面佈局。
`我參考上面的實現在這裏 <https://github.com/farseerfc/pelican-bootstrap3/blob/2ea6c9f3227275fe86ddaa75d8fc6496b3b03d8c/templates/includes/comments.html#L32>`_ 。
這個加載代碼使用兩個變量加載 Issue Comments ，一個是在 pelicanconf.py 裏的
:code:`GITHUB_REPO` ，可以指向任何 Repo ，我指向 farseerfc/farseerfc.github.io
的這個 GitHub Page repo ，另一個變量是每篇文章裏需要加上 :code:`issueid`
的元數據，關連文章到每個 Issue 上。

還有一個稍微麻煩的事情是現在每寫一篇文章之後都要新建一個 issue 了。
手動操作有點累人，於是我 `寫了個腳本 <https://github.com/farseerfc/farseerfc/blob/master/createissue.py>`_
自動搜索 pelican 的 content 文件夾裏面文章的 slug 並且對沒有 issueid 關連的
文章創建 issue 。

好啦新的留言系統的外觀樣式還在測試中，希望大家多留言幫我測試一下！

.. label-warning::

    **2016年8月7日19:30更新**

新增了對 GitHub Issue comments 裏面
`reactions <https://developer.github.com/v3/issues/comments/#reactions-summary>`_
的支持，套用 font-awesome 的圖標（似乎沒 GitHub 上的圖標好看）。這個還屬於 GitHub API
的實驗性功能，要加入 :code:`Accept: application/vnd.github.squirrel-girl-preview`
HTTP 頭纔能拿到。

.. label-warning::

    **2016年8月7日23:16更新**

感謝 @iovxw 的測試讓我發現 github 的高亮回復和郵件回復是需要特殊處理的。
高亮回復用上了 `這裏的 CSS <https://github.com/sindresorhus/github-markdown-css>`_
郵件引言的展開事件直接用 jQuery 做了：

.. code-block:: javascript

	  $(".email-hidden-toggle > a").on("click", function (e){
        e.preventDefault();
        $(".email-hidden-reply", this.parent).toggle();
      });


還得注意郵件的回復需要 CSS 裏面 :code:`white-space: pre-wrap` 。