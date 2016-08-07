为什么 Linus Torvalds 不愿意将 Linux 变成 GPLv3 授权？
====================================================================

:date: 2016-08-08 01:02
:slug: why-linus-torvalds-undermine-gplv3
:lang: zh
:tags: Linux, zhihu, GPLv3, licenses, Linus Torvalds

從 `知乎 <https://www.zhihu.com/question/48884264/answer/113454129>`_ 轉載


和上篇文章一樣，這篇也是來自一個知乎上我回答的問題。

原問題：为什么 Linus Torvalds 不愿意将 Linux 变成 GPLv3 授权？

我的回答：

	這裏有段 Linus Torvalds 在 DebConf 14 上的 Q&A:
	https://youtu.be/1Mg5_gxNXTo?t=47m20s

	其中關於 GPLv3 和協議的那一段在47:20開始到57:00左右。
	裏面 Linus 對自己的觀點澄清得很清楚了。
	看u2b或者聽英語有困難的請留評論，我抽空可以試着翻譯一下。


然後接下來就是我承諾的翻譯了
------------------------------------------------------------


	Q: Do you agree that you undermine GPLv3? and ...

問：你是否同意說你藐視了 GPLv3 ? 以及……

	L: Yeah

L: 是的

	Q: How can we get you to stop?

問：我們如何纔能讓你別這麼做？

	L: What?

L: 什麼？

	Q: How can we get you to stop?

問：我們如何纔能讓你別這麼做？

	L: Oh I hate GPLv3. I undermined it on purpose.
	I actually thought the GPLv3 extensions were horrible.
	I understand why people would want to do them but I think it should have
	been a completely new licenses.

L: 哦我討厭 GPLv3 ，我是在故意藐視它。我實際上覺得 GPLv3 的擴展非常可怕。
我能理解爲什麼人們想要做這個，但是我覺得它本應是一個全新的協議。

	Emm my argument for liking version 2, and I still think version 2 is a
	great license, was that, "I give you source code, you give me your
	changes back, we are even." Right? That's my take on GPL version 2, right,
	it's that simple.

嗯我喜歡版本2的那些理由，並且我仍然覺得版本 2 是一個非常棒的協議，
理由是：「我給你源代碼，你給我你對它的修改，我們就扯平了」
對吧？這是我用 GPL 版本 2 的理由，就是這麼簡單。

	And version 3 extended that in ways that I personally am really
	uncomfortable with, namely "I give you source code, that means that if
	you use that source code, you can't use that on your device unless you
	follow my rules." And to me that's, that's a violation of everything
	version 2 stood for. And I understand why the FSF did it because I know
	what the FSF wants.	But to me it's not the same license at all. 

然後版本3的擴展在某些方面讓我個人覺得非常不舒服，也就是說「我給你源代碼，
這意味着你必須服從我的一些規則，否則你不能把它用在你的設備上。」
對我來說，這是違反了版本2協議所追求的所有目的。然而我理解爲什麼 FSF 要這麼做，
因爲我知道 FSF 想要達成什麼，但是對我來說這完全是不同的協議了。

	So I was very upset and made it very clear, and this was months before
	version 3 was actually published. There was a discussion about this
	long before... There was an earlier version of version 3, years before
	actually, where I said "No, this is not gonna fly."
	And during that earlier discussion I had already added to the kernel that,
	"Hey, I don't have the version 2 or later". And there was no...
	And I was really happy then when version 3 came out, that I have done that
	something like 5 years before, because there was ever never any question
	about what the license for the kernel was.

所以我當時非常不安，並且表明了自己的觀點，並且這是在版本 3 發佈的數月之前。
在那很久之前曾經有過一場討論……在版本 3 之前有一個早期的版本，
事實上幾年之前，那時我就說過：「不，這不可能工作」。
並且在那個早期的討論階段我已經在內核裏寫好了「嘿，我可沒有寫過版本 2
或者更高版本」。所以之後也沒有過（爭議）……隨後版本 3 出來的時候我非常開心，
因爲我早就在大概 5 年前做了預防，之後也就再也沒有過關於內核的協議究竟是哪個
版本的討論。

	But I actually thought that version 3 is ... Uh, no ... I actually think
	version 3 is a **FINE** license, right. I'm a firm believer in,
	"If you write your code, it is your choice to pick a license."
	And version 3 is a fine license. Version 3 was not a good ... 
	"Here we give you version 2, and then we tried to sneak in these new rules,
	and tried to force everybody to upgrade." That was the part I disliked.
	And the FSF did some really sneaky stuff.
	Done right immoral in my opinion.

不過事實上我覺得版本 3 是……呃不……我事實上覺得版本 3 是個 **不錯** 的協議，
對吧。我堅定地相信「如果是你寫的代碼，那麼你有權利決定它應該用什麼協議」。
並且版本 3 是個不錯的選擇。版本 3 不好的地方在……「我們給你了版本 2
，然後我們試圖偷偷混入這些新的規則，並且想讓所有人都跟着升級」這是我不喜歡版本
3 的地方。並且 FSF 在其中做了很多見不得人的事情，我覺得做得很不地道。

	Q: So you are talking about `Tivoization <https://en.wikipedia.org/wiki/Tivoization>`_?

.. panel-default::
	:title: 關於 Tivoization

	譯註： Tivoization 是 FSF 發明的一個詞，表示 TiVo 的做法。 TiVo
	是一個生產類似電視機頂盒之類的設備的廠商，他們在他們的設備中用到了 Linux
	內核和很多別的開源組件，並且他們根據 GPLv2 協議開放了他們使用的組件的源代碼。
	然而他們在他們出售的設備中增加了數字簽名，驗證正在執行的系統和軟件是他們自己
	編制的軟件，從而限制了用戶修改運行軟件的自由。這種做法在 FSF 看來是鑽了 GPLv2
	的法律上的空子，所以 FSF 提出了 GPLv3 封堵這種做法。


問：所以你在說 `Tivoization <https://en.wikipedia.org/wiki/Tivoization>`_ 的事情麼？

	L: Ehmm, yeah the Tivoization is always my main, eh dislike of version 3.
	And, the FSF was being very dishonest thing. "Hey, we actually allow you
	to invalidate the Tivoization clause" and they tried to, they literally
	lied to people, and say "Hey, so that means that you can use GPLv3 without
	the Tivoization part", right. This is ... How many people heard this
	particular statement from the FSF? (Please rise your hands)

L: 沒錯，Tivoization 的事情一直是我的主要反對版本 3 的根據。並且，FSF
在這件事上表現得極不誠實。「嘿，其實我們允許你」