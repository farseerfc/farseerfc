我看 Linux 發行版：碎片化？這是自由
===========================================

:id: how-i-view-linux-distributions-fragmentation-freedom
:translation_id: how-i-view-linux-distributions-fragmentation-freedom
:lang: zh
:date: 2016-08-26 22:45
:tags: linux, distributions, freedom
:status: draft

.. contents::

從不少 Linux 用戶，尤其是 Ubuntu 用戶口中，我聽到過 **「碎片化」**
這個詞，用來描述 Linux 發行版衆多的現象和（他們覺得）所導致的問題。 **碎片化**
對大家而言應該並不陌生，經常用來形容 Android 系統的現狀，表示廠商衆多的
Android 手機出現的諸多兼容性問題。大概由於 Android 系統也同樣用 Linux
內核並且開源，從而有不少人覺得 Android 上的碎片化現象是因爲 Linux 和開源的問題，
並且 GNU/Linux 的諸多發行版們也有同樣的問題，甚至百度百科也這麼說 [#]_ :

    ……而由于 Android **完全免费以及完全开源**
    的性质，最终导致 Android 设备的软件兼容性变差，间接加大了软件开发的难度
    (主要难度是让软件在更多的设备上运行)，最终会导致一个结果：由于开发难度高，
    开发成本增大，软件开发商和软件开发者们会放弃开发……

.. [#] `百度百科-安卓碎片化 <http://baike.baidu.com/view/9632689.htm#1>`_

但是 **本質上** ，Android 上出現的 **碎片化問題是 Linux 和開源所導致的麼** ，
**GNU/Linux 諸多發行版的現象也是同樣的問題麼** ？我想在這篇文章中聊聊這個。
考慮到 Android 用戶明顯比 GNU/Linux 發行版用戶要多，各大媒體也覆蓋得更廣，
本文不想再複述 Android 上的碎片化問題是什麼，而想關注於
**GNU/Linux 發行版的衆多的現象該如何看待**。
此外本文也不想討論 GNU/Linux 和 Linux 這兩個稱呼的區別，下面爲了方便就直接稱呼爲
Linux 發行版了，大家請默認我在說的都是 GNU/Linux 發行版（或者可能不用 Linux
內核而用別的內核的 GNU 系統比如 Debian 的 kfreebsd 和 Hurd
分支這樣的自由軟件發行版）。
同樣我也無意討論 Android 到底是不是 Linux 發行版的問題，以及 Android
到底算不算開源軟件平臺的問題，大家應該能從上下文中看出我想說什麼 😂 。

Linux 發行版衆多，該選擇的是社區
------------------------------------------------

Linux 確有很多發行版， 寫這篇的時候
`DistroWatch 上列出 895 個之多 <https://distrowatch.com/search.php?status=All>`_
，必然還有很多是他們沒能跟蹤到的。單看數字的確是有很多，但是考慮到大部分發行版
其實是別的發行版的衍生，看獨立活躍的發行版就
`只有 65 個了 <https://distrowatch.com/search.php?ostype=All&category=All&origin=All&basedon=Independent&notbasedon=None&desktop=All&architecture=All&package=All&rolling=All&isosize=All&netinstall=All&status=Active>`_
，其中還包括 FreeBSD 和 ReactOS 這些不知是否該被列入發行版的行列。

.. panel-warning::
   :title: 這些「經驗」不是我的觀點

   不要根據這些片面之詞選擇你的第一個發行版

「這麼多發行版之間的區別是什麼呢？」這或許是每個 Linux 剛入門的新人都想問的問題。
有這麼多發行版，要用一個的話必然想問他們之間的區別何在，該如何選擇。
於是會有諸多老手們會開始給新手介紹 *「經驗」*：

:Ubuntu: 對新手友好，社區龐大，軟件豐富，界面美觀易用……
:Debian: 穩定，安心，是每個 Linux 用戶折騰久了之後的最終歸宿……
:RedHat: 穩定，安全，企業級……
:CentOS: 我就是 RedHat……
:Mint: 我比 Ubuntu 更友好，用戶更多，排名更高……
:Arch Linux: 更新快，但是不穩定，而且安裝麻煩，需要「折騰」……
:Gentoo: 不自己編譯就不舒服……

.. panel-default::
   :title: Linux 發行版雷達圖，`來自這裏 <http://tuxradar.com/content/best-distro-2011>`_

   .. image:: {static}/images/distro_stats_lg.png
      :alt: Linux 發行版雷達圖

這些經驗試圖從穩定性、易用性等各方面對這些發行版下個定論，就好像 RPG
遊戲一開始創建角色的界面，每個角色的區別就是力量、敏捷、智力等或高或低的數值，
甚至還真的有人給發行版們畫出了雷達圖比較各項屬性在數值上的優劣。
就好像如果新人選擇了那個攻高血厚的發行版就能輕易上陣，
而如果想領略遊戲的精髓和趣味，務必打穿一週目之後去選那個一開始
看起來攻低血薄超高難度的 Arch Linux 或者全數值爲 0 的噩夢難度的 Gentoo 。
這些經驗或許是反映了高手們的個人感受，或許是來自前人代代相傳的耳濡目染。
我以前也經常這樣向詢問我的人們介紹發行版們的優劣，或者反駁別人這樣的介紹中
不符合我的感受的部分。這樣的數值評價通常適用於產品的宣傳，
每個發行版的自豪的用戶們都像是傳銷組織培訓出來的傳銷員，
努力向新手兜售自己所用發行版的優勢，抨擊別的發行版的不足。
而從剛入門的新人的角度來看，這些宣傳員們的互相抨擊只會讓他們更加困惑，
使他們覺得整個 Linux 用戶羣就像一個教派衆多的邪教組織，肆意發展新的信徒。

而這種對發行版的評價偏偏忽略了衡量一個 **發行版最重要的部分，也就是人**
。 **Linux 發行版並不是一個產品** （就算是 Red Hat 這樣的商業發行版，
其出售的產品也不是軟件本身），而是由 **一羣人組成的社區**
，其餘的都是這羣人產生的結果：

:軟件包的多寡: 是這個社區 **打包** 工作的結果
:軟件包的穩定性: 是這個社區 **測試** 工作的結果
:文檔的優劣: 是這個社區 **文檔編撰** 工作的結果
:安裝的難易: 是這個社區 **安裝嚮導** 工作的結果

那些通常認爲的衡量發行版優劣的指標，大多數都是對社區的間接評價，
還有少數只是人云亦云的謠傳。比如 **硬件支持** 這個指標，大家都是用同樣的內核樹，
同樣的內核版本硬件支持方面理應是一樣的，區別只在於有些發行版有提供工具自動偵測加載驅動，
另一些發行版可能需要用戶手動安裝。如果說有些商業發行版比如 RedHat 和 SUSE 有硬件廠商
（亦或發行版的內核組）直接提供的二進制驅動支持這還稍顯可信
（而這種情況通常發生在預期使用 Linux 的服務器上），而說 Ubuntu
因爲在安裝嚮導裏加入了對顯卡閉源驅動的自動檢測和支持就說它的硬件支持遠好於別的
發行版，這完全就是混淆視聽了。

因爲對 Linux 發行版而言最重要的是社區，所以 **如何選擇 Linux 發行版**
這個問題歸根結底其實是 **如何選擇 Linux 社區** 的問題。這本應該是一個顯而易見
衆所周知的事情，但是大部分人（包括我以前）在給人們推薦發行版的時候都忽略了
這一點。或許這是因爲我們日常評價別的「商品」的時候習慣了用這種性能指標衡量，
從而我們也遵循着慣性用同樣的性能指標去衡量我們的 Linux 發行版。
然而用性能指標評價 Linux 發行版是個嚴重的錯誤，甚至連
`Windows <https://youtu.be/Bs7a2DrWTmk?list=PLWs4_NfqMtoyppPlVydopdpz_FnnK4tuY>`_
和 `macOS <https://youtu.be/DZSBWbnmGrE>`_
的廣告都知道，宣傳的時候不應該聚焦在功能指標上，
而更應該着重於傳達「我們的用戶是怎樣的人」。

.. panel-default::
   :title: 我眼中的各 Linux 發行版用戶，`來自知乎提問 <https://www.zhihu.com/question/22605825>`_

   .. image:: {static}/images/how-i-view-linux-users.jpg
      :alt: 我眼中的各 Linux 發行版用戶

我們傾向於用這些指標評價 Linux 發行版的另一個原因，或許是因爲很多 Linux
用戶們覺得，「選擇 Linux 發行版」和「我是怎樣的人」並沒有直接關係，
而這又是一個嚴重的錯誤。閉上眼睛想想各個 Linux 發行版，大概你腦中很快會浮現出各種
Linux 發行版用戶的樣子，網上也流傳着各種版本的「我眼中的各 Linux 發行版用戶」的圖。
不少 Linux 用戶或許覺得，他們在同時使用着數個不同的發行版，是跨發行版用戶，
從而他們是怎樣的人不能決定他們對發行版的選擇。但是時間長了， Linux
用戶就會發現他們常用的發行版中更喜歡某個發行版的做事方式。
由於日常系統上切換發行版的成本相對很低，從而自然而然得，「我喜歡怎樣的做事方式」
就會漸漸影響到「選擇怎樣的 Linux 發行版」。

各個 Linux 發行版有其關於「Linux 應該如何」的 **理念** ，這樣的理念下聚集了持有同樣
理念的一羣人，這羣人在這 **同樣的理念下共同努力** 形成穩定的社區，開發更多社區項目
達成和完善發行版的理念，而社區運作的結果，就是這種理念在這個發行版中被加強，
形成良性循環，吸引更多持有同樣理念的人前來逗留。

我想了很久該如何描述這一現象，後來我發現，現代社會有一個詞完全符合這樣的描述，也就是
**「政治」** ： 一個 Linux 發行版代表了一個 **政治理念** 。
這句話最近被我在很多不同的地方重複過很多次，因爲我覺得它非常重要，
請允許我再重複一次：

**一個 Linux 發行版代表了一個政治理念。**

好像還不夠強調，那麼再強調一次：

一個 Linux 發行版代表了一個政治理念
------------------------------------------------

或許很多人會反感在 **「技術」** 領域談到 **「政治」** 這個詞，尤其是在中國大陸的政治環境中
成長起來的技術者們眼中，「政治」這個詞或多或少帶有某種「非我族類」的貶義。
但是請不要害怕「政治」這個詞，尤其讓我們來看看這個詞本來的意思：

  `Politics <https://en.wikipedia.org/wiki/Politics>`_ is the process of making decisions applying to all members of a group.

  `政治 <https://zh.wikipedia.org/wiki/%E6%94%BF%E6%B2%BB>`_ 是各種團體進行集體決策的一個過程……

**「集體決策」** 非常適合於用來描述 Linux 發行版是什麼。一個 Linux
發行版就是 **一羣 Linux 用戶共同做出的集體決策** 。衆所周知， Linux
發行版本質就是一堆軟件包，而要讓這些軟件包集合在一起協同工作，必須做一些決策。
這些決策包括並不限於：

#. 我們該用什麼包管理器和包格式？
#. 我們該用什麼 init 系統？
#. 我們該如何配置我們的系統？
#. 我們該支持幾種體系架構？
#. 我們該以何種態度對待私有閉源軟件？
#. 我們該用何種桌面環境？是我們強制一種還是允許用戶選擇一種？

這些決策涉及發行版的方方面面，並且這些決策並沒有一個標準答案，對每一個決策做出的
回答都會影響到整個發行版的使用體驗。在理想情況下，一個發行版應該兼顧用戶的所有
需求，提供最優的方案，而現實是發行版們的精力有限，努力的方向只能朝着一個方向。
從而所有這些決策都需要有個具體的答案，整個發行版社區朝着這些答案的方向努力。
**一個發行版，就像現實社會中的一個政黨** ，其販賣的是決策的指導方針，
宣傳的是選擇這個羣體之後享受的好處。
當新的疑問凸顯出來需要決策的時候，通常上游發行版都有一個明確的 **政治理念**
指導人們做出合適的選擇，而這就是該發行版的「原則」：

:Arch Linux: `簡潔(Simplicity)、現代(Modernity)、實用(Pragmatism)、用戶中心(User centrality)、可定製(Versatility) <https://wiki.archlinux.org/index.php/Arch_Linux>`_
:Gentoo: `社區驅動(Community)、高效(Efficiency)、靈活(Flexibility)、可伸縮(Scalability)、安全(Security) <https://wiki.gentoo.org/wiki/Benefits_of_Gentoo>`_
:Fedora: `自由(Freedom)、友愛(Friends)、功能(Features)、領先（First） <https://fedoraproject.org/wiki/Foundations>`_
:Debian: `理念與社區(Philosophy and Community)、實用與可用性(Utility and usability)、實現品質(Quality of implementation)、功能與軟件選擇(Feature set and Selection of Software)、內核與用戶空間(Kernels and User Land)、維護與管理(Maintenance and administration)、可移植性與硬件支持(Portability and Hardware Support)、源碼構建(Source Builds)、安全性和可靠性(Security and Reliability)、可擴展性與性能(Scalability and Performance) <https://wiki.debian.org/WhyDebian>`_

乍看起來每個發行版在說的貌似都差不多，都是些廣告用語，就像單從詞義理解的話美國民主黨和共和黨聽起來也是差不多的意思，
但是當你細看這些原則的細節，就能看出每個發行版在上述關鍵問題上所做的抉擇。

具體理念如何影響抉擇，抉擇如何塑造社區，社區又如何提供發行版的……

就從以我比較熟悉的 Arch Linux 舉例說說
-----------------------------------------------------------------------------------------------------

比如說 Arch Linux 崇尚簡潔，這可不是一句空頭支票， Arch Linux 崇尚不多做無謂的事情。