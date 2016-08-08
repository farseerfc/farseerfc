爲什麼 Linus Torvalds 不願意將 Linux 變成 GPLv3 授權？
====================================================================

:date: 2016-08-08 16:15
:slug: why-linus-torvalds-undermine-gplv3
:lang: zh
:tags: Linux, zhihu, GPLv3, licenses, Linus Torvalds, GPL, FSF, EFF
:issueid: 63

從 `知乎 <https://www.zhihu.com/question/48884264/answer/113454129>`_ 轉載


和上篇文章一樣，這篇也是來自一個知乎上我回答的問題。

原問題：为什么 Linus Torvalds 不愿意将 Linux 变成 GPLv3 授权？

我的回答：

	這裏有段 Linus Torvalds 在 DebConf 14 上的 Q&A:
	https://youtu.be/1Mg5_gxNXTo?t=47m20s

	其中關於 GPLv3 和協議的那一段在47:20開始到57:00左右。
	裏面 Linus 對自己的觀點澄清得很清楚了。
	看u2b或者聽英語有困難的請留評論，我抽空可以試着翻譯一下。


.. panel-default::
	:title: DebConf 14: Q&A with Linus Torvalds

	.. youtubeku:: 1Mg5_gxNXTo XMTY3NjIzNDU0NA

然後接下來就是我承諾的翻譯了
------------------------------------------------------------


	Q: Do you agree that you undermine GPLv3? and ...

問：你是否同意說你貶低了 GPLv3 ? 以及……

	L: Yes

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
	been a completely new license.

L: 哦我討厭 GPLv3 ，我是在故意貶低它。實際上我覺得 GPLv3 的擴展非常可怕。
我能理解爲什麼人們想要做這個，但是我覺得它本應是一個全新的協議。

	Emm my argument for liking version 2, and I still think version 2 is a
	great license, was that, "I give you source code, you give me your
	changes back, we are even." Right? That's my take on GPL version 2, right,
	it's that simple.

嗯我喜歡版本 2 的那些理由，並且我仍然覺得版本 2 是一個非常棒的協議，
理由是：「我給你源代碼，你給我你對它的修改，我們就扯平了」
對吧？這是我用 GPL 版本 2 的理由，就是這麼簡單。

	And version 3 extended that in ways that I personally am really
	uncomfortable with, namely "I give you source code, that means that if
	you use that source code, you can't use it on your device unless you
	follow my rules." And to me that's, that's a violation of everything
	version 2 stood for. And I understand why the FSF did it because I know
	what the FSF wants.	But to me it's not the same license at all. 

然後版本 3 的擴展在某些方面讓我個人覺得非常不舒服，也就是說「我給你源代碼，
這意味着你必須服從我的一些規則，否則你不能把它用在你的設備上。」
對我來說，這是違反了版本 2 協議所追求的所有目的。然而我理解爲什麼 FSF 要這麼做，
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
因爲我早在大概 5 年前做了預防，之後也就再也沒有過關於內核的協議究竟是哪個
版本的討論。

	But I actually thought that version 3 is ... Uh, no ... I actually think
	version 3 is a **FINE** license, right. I'm a firm believer in,
	"If you write your code, it is your choice to pick a license."
	And version 3 is a fine license. Version 3 was not a good ... 
	"Here we give you version 2, and then we tried to sneak in these new rules,
	and tried to force everybody to upgrade." That was the part I disliked.
	And the FSF did some really sneaky stuff, downright immoral in my opinion.

不過事實上我覺得版本 3 是……呃不……我事實上覺得版本 3 是個 **不錯** 的協議，
對吧。我堅定地相信「如果是你寫的代碼，那麼你有權利決定它應該用什麼協議」。
並且版本 3 是個不錯的選擇。版本 3 不好的地方在……「我們給你了版本 2
，然後我們試圖偷偷混入這些新的規則，並且想逼着所有人都跟着升級」這是我不喜歡版本
3 的地方。並且 FSF 在其中做了很多見不得人的事情，我覺得做得很不道德。

	Q: So you are talking about `Tivoization <https://en.wikipedia.org/wiki/Tivoization>`_?

.. panel-default::
	:title: 譯註： 關於 `Tivoization <https://en.wikipedia.org/wiki/Tivoization>`_

	Tivoization 是 FSF 發明的一個詞，表示 TiVo 的做法。 TiVo
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
	particular statement from the FSF? (Please raise your hands)

L: 沒錯，Tivoization 的事情一直是我反對版本 3 的主要根據。並且，FSF
在這件事上表現得極不誠實。「嘿，其實我們允許你無效化 Tivoization 條款」，這樣他們試圖，
應該說他們是在明白着欺騙別人，並且說「嘿，這意味着你可以使用除去 Tivoization 部分的 GPLv3」。
這很……在場的諸位中有誰從 FSF 那兒聽過這個說法？（請舉手）

	Ok, maybe they only tried to convince me with that one.
	But they did try. And it was like, "I'm not stupid", right. Yes, you can
	... The GPLv3 allows you to say "Ok, Tivoization is not an issue for us".
	But it allows somebody else to take the project, and say "Hey, I ... The
	GPLv3 without Tivoization is compatible with the full GPLv3, so I will now
	make my own fork of this, and I will start doing drivers that use the full
	version of version 3" And where am I stuck then? I am stuck saying "Hey I
	give you the source code, and now I can't take it back your changes".
	That's completely against the whole point of the license in the first
	place.

好吧，或許他們只試過對我用這套說辭，但是他們真的試過。我的反應是「我可不傻」，對吧。是的，
的確你可以…… GPLv3 允許你說「好， Tivoization 的事情對我們來說不是問題」，
但是它同時又允許別人接過這個項目，並且說「嘿，我覺得……去掉了 Tivoization 的 GPLv3
是兼容完整的 GPLv3 的，所以我可以 fork 這個項目，然後我將在自己的 fork 上用完整的
GPLv3 寫驅動。」然後我就囧了。我的困境在於說「嘿，我給了你我的源代碼，現在我卻不能拿回你對它
的修改了」。這是徹底違背了我用這個協議最初的目的了。

	So the FSF was, I mean the kind of stuff that was going on behind the
	scenes, ah, made me once and for all to decide to never had any thing to
	do with the FSF again. So if you wanted to give money to an organization
	that does good? Give it to the EFF. The FSF is full of crazy bittered
	people. That's just mine opinion. Uh, actually I have ... Ah ...
	I overstated that a bit, right. The FSF has a lot of nice people in it,
	but some of them are bit too extreme.

所以 FSF 是，我是說那時他們暗地裏做的那些事情，讓我當下決定永遠不再和 FSF 有任何瓜葛。
所以如果你想捐錢給一個行善的組織，那就捐給 EFF 吧。FSF 充滿了瘋狂難處的人。這只是我的觀點。
呃其實我……嗯……我說得有點過分了。FSF 裏有很多不錯的人，不過其中有些人有點過激。

	Q: Well I wish the EFF care more about software freedom. But, uh,
	can you ... Do you think that Tivoization benefits me as a user somehow?

問: 嗯我也希望 EFF 能更多的關注於軟件的自由方面。但是你能……你覺得 Tivoization
這種行爲也能在某種方式上讓我作爲用戶獲益麼？

	L: No, no I don't. I mean that ... But that was never my argument. That
	was not why I selected the GPLv2. This is my whole point. It's not that
	I think Tivoization is necessarily something that you should strive for.
	But it is something that in my world view, it's your decision.
	If you make hardware that locks down the software, that's your decision
	as a hardware maker. That has no impact on my decision as a software maker
	to give you the software. Do you see where I am coming from? I don't like
	the locked down hardware, but at the same time that was never the social
	contract I intended with Linux. 

L: 不，我不覺得。我的意思是……這從來都不是我的論據，這不是我選擇了 GPLv2 的理由。
並不是說我覺得 Tivoization 是某種值得你去爭取的權利，而是說在我的世界觀中，這是你的決定。
如果你生產硬件去鎖住了其中的軟件，這是你作爲一個硬件提供者的決定。
這完全不影響我作爲一個軟件提供者給你軟件的決定。你能看出我的立場在哪兒了麼？
我不喜歡上鎖的硬件，但是同時這也從來不是我想要給 Linux 加上的的社會契約。

	To me, umm, I mean, people may or may not
	realize GPLv2 wasn't even the first license for Linux. 
	To me the important part was always "I give you software, you can do
	whatever you want with it. If you making improvements, you have to give
	them back." That was the first version of the license. It also had a
	completely broken clause which was completely insane and I was stupid.
	Hey it happened. My origin license says that you can't make money
	change hands. And that was a mistake. That was clearly just wrong and bad
	because it really didn't have anything to do with what I wanted. But I
	was young, I was poor, I didn't realize that the whole money thing wasn't
	the important part. And I have saw the errors in my ways, I saw the GPLv2
	and said "Hey, that's the perfect license". And I saw the GPLv3 and I said
	"No, that's overreaching a lot, that's not what I wanted". And so I made
	Linux GPLv2 only, right.

對我來說，呃我想說，大家可能知道或者不知道， GPLv2 並不是 Linux 的最初的協議。
對我來說重要的部分一直是「我給你軟件，你可以用它做任何你想要做的事情。如果你做了任何改進，
你需要把它交還給我。」這是協議最初的樣子。最早的協議還有一條完全錯誤的條款，寫得完全不合理，
那時我很傻。嘿我也傻過。我最初的協議說你不能用它賺錢。這是失策，這明顯是不對的不好的，
因爲它和我真正想要做的事情沒有任何關係。但是那時我很傻很天真，
我沒意識到錢的事情在其中完全不重要。然後我發現了其中的問題，我看到了 GPLv2 然後說「嘿，
這是個完美的協議」。然後我看到了 GPLv3 我說「不，這做得過分了，這不是我想要的」
所以我讓 Linux 成爲了僅限 GPLv2 ，對吧。

	Q: So do you think getting the patches back is as useful even if you can't
	modify the device that it is used on?

問: 所以你是否認爲，即使你不能修改跑着這個軟件的設備，拿回對軟件的修改也還是同樣重要的？

	L: Yeah, absolutely. And I mean TiVo itself is actually an example of this.
	Their patches were kind of crafty but I mean they were basically running
	on a, originally a fairly standard MIPS thing. And their patches were
	working around bugs in the chipsets they used. And they were valid patches.
	The fact that they then felt that their hardware had to be locked down
	someway. I didn't like it. But as I have mentioned, I felt that that was
	their decision.

L: 是的，當然。我想說 TiVo 它自己實際上就是一個例子。他們的修改有點複雜，但是我想說他們基本
是，一開始基本是運行在一套相當標準的 MIPS 設備上。然後他們的修改是想繞開他們用到的芯片上的
一些問題，並且這些是合格的修改。之後的事情是他們覺得他們需要鎖住他們的硬件，我不喜歡這個。
但是就像我已經說的，我覺得這是他們的決定。

	And they had real reasons for that. That's something people sometimes
	missed. There are sometimes reasons to do what TiVo did. Sometimes it's
	imposed on you by, wireless carriers. Sometimes it's imposed on you by
	Disney. Uh sometimes it's imposed on you by laws. The GPLv3 actually
	accepts the last one when it comes to things like medical equipment
	I think. But the point is that the whole Tivoization thing is, sometimes
	it's, there is a reason for it. And if you make ... I mean I am not a
	hardware designer. I think FPGA and stuff like that is really cool. 
	But I always ... I mean I really don't want to impose my world view on 
	anybody else. You don't have to use Linux. If you do use Linux, the only
	thing I asked for is source code back. And there is all these other
	verbiages in the GPLv2 about exact details, those aren't important.
	And that was always my standpoint.

並且他們有真正的理由去這麼做。這是有時人們忽視的地方。有時是真的有理由去做 TiVo
他們做的事情。有時強加給你這種限制的是，無線運營商。有時強加給你的是迪士尼。
有時強加給你限制的甚至是法律。 GPLv3 在醫療設備之類的場合其實允許最後一種情況，我記得。
我的觀點是，整個 Tivoization 的事情有時是有理由去這麼做的。如果你生產……
我是說我不是硬件設計者，我覺得 FPGA 之類的東西很酷，但是我……我的意思是我真的不想把我對世界的
看法強加給別人。你不是非得要用 Linux ，如果你想要用 Linux
，那麼我唯一要求你做的事情是把源代碼（變更）還給我。然後在 GPLv2
中還有很多繁文縟節規定了詳細的細節，這些都不重要。這是我一直以來的觀點。

	Q: Ok, well I will stop my non-point of making noise now.


.. panel-default::
	:title: 譯註： 關於 `ISC 協議 <https://zh.wikipedia.org/wiki/ISC%E8%A8%B1%E5%8F%AF%E8%AD%89>`_

	ISC 協議是一個開源軟件協議，和兩句的 BSD 協議功能相同。OpenBSD 項目選擇儘量用 ISC
	協議公開他們新寫的代碼。

問: 好吧那我就不浪費時間了。

	L: I mean don't get me ... I mean I like other licenses too. I have used
	like the four, emmm... Which BSD license is the acceptable one?
	One of the BSD license is actually really nice. And it's actually the...
	What? 

L: 我的意思是別誤解……我也喜歡別的協議。我用過……到底是哪個 BSD 協議是可以接受的？
有一個 BSD 協議實際上非常不錯。它實際上是……什麼？

	A: ISC

觀衆： ISC

	L: ISC? And I actually encourage people who don't care about the giving
	code back but care about the "Hey, I did something cool, please use it".
	I encourage people to use the BSD license for that. And I mean the BSD
	license is wonderful for that. It so happens that I thought that for my
	project the giving back is equally important so I, for me BSD is bad.
	But the point is **for me**. The GPLv3 maybe the perfect license for what
	you guys want to do. And that's fine. And then it's the license you should
	use. It's just that when somebody else wrote the code you don't get that
	choice.

L: ISC？並且事實上我在鼓勵那些不在意拿回修改但是在意「嘿，我做了一個很酷的東西，請用它」。
我鼓勵這些人去用 BSD 協議做這些事情。我想說 BSD 協議在這種場合是完美的。
只是碰巧我覺得對於我的項目，拿回修改也同樣重要，所以對我而言 BSD 不好。但是重點是
**對我而言** 。 GPLv3 可能對你們想要做的事情而言是完美的協議，這很好，並且這時你就應該去用
GPLv3 。只是當代碼是別人寫的時候，你沒有這個選擇權。