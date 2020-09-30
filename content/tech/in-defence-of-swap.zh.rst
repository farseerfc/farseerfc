【譯】替 swap 辯護：常見的誤解
====================================================================

:slug: in-defence-of-swap
:translation_id: in-defence-of-swap
:lang: zh
:date: 2020-09-30 13:45
:tags: swap, mm, memory management, translate, swappiness
:issueid: 97

這篇翻譯自 Chris Down 的博文
`In defence of swap: common misconceptions <https://chrisdown.name/2018/01/02/in-defence-of-swap.html>`_
。 `原文的協議 <https://github.com/cdown/chrisdown.name/blob/master/LICENSE>`_
是 `CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>`_
，本文翻譯同樣也使用 `CC BY-SA 4.0`_ 。其中加入了一些我自己的理解作爲旁註，所有譯註都在側邊欄中。

翻譯這篇文章是因爲經常看到朋友們（包括有經驗的程序員和 Linux 管理員）對 swap 和 swappiness
有諸多誤解，而這篇文章正好澄清了這些誤解，也講清楚了 Linux 中這兩者的本質。值得一提的是本文討論的
swap 針對 Linux 內核，在別的系統包括 macOS/WinNT 或者 Unix 系統中的交換文件可能有不同一樣的行爲，
需要不同的調優方式。比如在 `FreeBSD handbook <https://www.freebsd.org/doc/handbook/bsdinstall-partitioning.html#configtuning-initial>`_
中明確建議了 swap 分區通常應該是兩倍物理內存大小，這一點建議對 FreeBSD 系內核的內存管理可能非常合理，
而不一定適合 Linux 內核，FreeBSD 和 Linux 有不同的內存管理方式尤其是 swap 和 page cache 和
buffer cache 的處理方式有諸多不同。

經常有朋友看到系統卡頓之後看系統內存使用狀況觀察到大量 swap 佔用，於是覺得卡頓是來源於 swap
。就像文中所述，相關不蘊含因果，產生內存顛簸之後的確會造成大量 swap 佔用，也會造成系統卡頓，
但是 swap 不是導致卡頓的原因，關掉 swap 或者調低 swappiness 並不能阻止卡頓，只會將 swap
造成的 I/O 轉化爲加載文件緩存造成的 I/O 。

以下是原文翻譯：

.. contents:: 目录

------------

這篇文章也有 `日文 <https://chrisdown.name/ja/2018/01/02/in-defence-of-swap.html>`_
和 `俄文 <https://softdroid.net/v-zashchitu-svopa-rasprostranennye-zabluzhdeniya>`_
翻譯。

.. translate-collapse::

   tl;dr:

   #. Having swap is a reasonably important part of a well functioning system.
      Without it, sane memory management becomes harder to achieve.
   #. Swap is not generally about getting emergency memory, it's about making
      memory reclamation egalitarian and efficient. In fact, using it as
      "emergency memory" is generally actively harmful.
   #. Disabling swap does not prevent disk I/O from becoming a problem
      under memory contention, it simply shifts the disk I/O thrashing from
      anonymous pages to file pages. Not only may this be less efficient,
      as we have a smaller pool of pages to select from for reclaim, but it
      may also contribute to getting into this high contention state in
      the first place.
   #. The swapper on kernels before 4.0 has a lot of pitfalls,
      and has contributed to a lot of people's negative perceptions about
      swap due to its overeagerness to swap out pages. On kernels >4.0,
      the situation is significantly better.
   #. On SSDs, swapping out anonymous pages and reclaiming file pages are
      essentially equivalent in terms of performance/latency.
      On older spinning disks, swap reads are slower due to random reads,
      so a lower :code:`vm.swappiness` setting makes sense there
      (read on for more about :code:`vm.swappiness`).
   #. Disabling swap doesn't prevent pathological behaviour at near-OOM,
      although it's true that having swap may prolong it. Whether the
      system global OOM killer is invoked with or without swap, or was invoked
      sooner or later, the result is the same: you are left with a system in an
      unpredictable state. Having no swap doesn't avoid this.
   #. You can achieve better swap behaviour under memory pressure and prevent
      thrashing using :code:`memory.low` and friends in cgroup v2.


太長不看：

#. 對維持系統的正常功能而言，有 swap 是相對挺重要的一部分。沒有它的話會更難做到合理的內存管理。
#. swap 的目的通常並不是用作緊急內存，它的目的在於讓內存回收能更平等和高效。
   事實上把它當作「緊急內存」來用的想法通常是有害的。
#. 禁用 swap 在內存壓力下並不能避免磁盤I/O造成的性能問題，這麼做只是讓磁盤I/O顛簸的範圍從
   匿名頁面轉化到文件頁面。這不僅更低效，因爲系統能回收的頁面的選擇範圍更有限了，
   而且這種做法還可能是加重了內存壓力的原因之一。
#. 內核 4.0 版本之前的交換進程（swapper）有一些問題，導致很多人對 swap 有負面印象，
   因爲它太急於（overeagerness）把頁面交換出去。在 4.0 之後的內核上這種情況已經改善了很多。
#. 在 SSD 上，交換出匿名頁面的開銷和回收文件頁面的開銷基本上在性能/延遲方面沒有區別。
   在老式的磁盤上，讀取交換文件因爲屬於隨機訪問讀取所以會更慢，於是設置較低的 :code:`vm.swappiness`
   可能比較合理（繼續讀下面關於 :code:`vm.swappiness` 的描述）。
#. 禁用 swap 並不能避免在接近 OOM 狀態下最終表現出的症狀，儘管的確有 swap
   的情況下這種症狀持續的時間可能會延長。在系統調用 OOM 殺手的時候無論有沒有啓用 swap
   ，或者更早/更晚開始調用 OOM 殺手，結果都是一樣的：整個系統留在了一種不可預知的狀態下。
   有 swap 也不能避免這一點。
#. 可以用 cgroup v2 的 :code:`memory.low` 相關機制來改善內存壓力下 swap 的行爲並且
   避免發生顛簸。

------------


.. translate-collapse::

   As part of my work improving kernel memory management and cgroup v2,
   I've been talking to a lot of engineers about attitudes towards memory
   management, especially around application behaviour under pressure and
   operating system heuristics used under the hood for memory management.

我的工作的一部分是改善內核中內存管理和 cgroup v2 相關，所以我和很多工程師討論過看待內存管理的態度，
尤其是在壓力下應用程序的行爲和操作系統在底層內存管理中用的基於經驗的啓發式決策邏輯。


.. translate-collapse::

   A repeated topic in these discussions has been swap. 
   Swap is a hotly contested and poorly understood topic, 
   even by those who have been working with Linux for many years. 
   Many see it as useless or actively harmful: a relic of a time where
   memory was scarce, and disks were a necessary evil to provide much-needed
   space for paging. This is a statement that I still see being batted
   around with relative frequency in recent years, and I've had many
   discussions with colleagues, friends, and industry peers to help them
   understand why swap is still a useful concept on modern computers with
   significantly more physical memory available than in the past.

在這種討論中經常重複的話題是交換區（swap）。交換區的話題是非常有爭議而且很少被理解的話題，甚至包括那些在
Linux 上工作過多年的人也是如此。很多人覺得它沒什麼用甚至是有害的：它是歷史遺蹟，從內存緊缺而
磁盤讀寫是必要之惡的時代遺留到現在，爲計算機提供在當年很必要的頁面交換功能作爲內存空間。
最近幾年我還經常能以一定頻度看到這種論調，然後我和很多同事、朋友、業界同行們討論過很多次，
幫他們理解爲什麼在現代計算機系統中交換區仍是有用的概念，即便現在的電腦中物理內存已經遠多於過去。

.. translate-collapse::

   There's also a lot of misunderstanding about the purpose of swap –
   many people just see it as a kind of "slow extra memory" for use in emergencies,
   but don't understand how it can contribute during normal load to the healthy
   operation of an operating system as a whole.

圍繞交換區的目的還有很多誤解——很多人覺得它只是某種爲了應對緊急情況的「慢速額外內存」，
但是沒能理解在整個操作系統健康運作的時候它也能改善普通負載的性能。

.. translate-collapse::

   Many of us have heard most of the usual tropes about memory:
   " `Linux uses too much memory <https://www.linuxatemyram.com/>`_ ",
   " `swap should be double your physical memory size <https://superuser.com/a/111510>`_
   ", and the like. While these are either trivial to dispel,
   or discussion around them has become more nuanced in recent years,
   the myth of "useless" swap is much more grounded in heuristics and
   arcana rather than something that can be explained by simple analogy,
   and requires somewhat more understanding of memory management to reason about.

我們很多人也聽說過描述內存時所用的常見說法： 「 `Linux 用了太多內存 <https://www.linuxatemyram.com/>`_
」，「 `swap 應該設爲物理內存的兩倍大小 <https://superuser.com/a/111510>`_ 」，或者類似的說法。
雖然這些誤解要麼很容易化解，或者關於他們的討論在最近幾年已經逐漸變得瑣碎，但是關於「無用」交換區
的傳言有更深的經驗傳承的根基，而不是一兩個類比就能解釋清楚的，並且要探討這個先得對內存管理有
一些基礎認知。

.. translate-collapse::

   This post is mostly aimed at those who administrate Linux systems and
   are interested in hearing the counterpoints to running with
   undersized/no swap or running with vm.swappiness set to 0.

本文主要目標是針對那些管理 Linux 系統並且有興趣理解「讓系統運行於低/無交換區狀態」或者「把
:code:`vm.swappiness` 設爲 0 」這些做法的反論。

背景
----------------------------------------

.. translate-collapse::

   It's hard to talk about why having swap and swapping out pages are good
   things in normal operation without a shared understanding of some of
   the basic underlying mechanisms at play in Linux memory management,
   so let's make sure we're on the same page.

如果沒有基本理解 Linux 內存管理的底層機制是如何運作的，就很難討論爲什麼需要交換區以及交換出頁面
對正常運行的系統爲什麼是件好事，所以我們先確保大家有討論的基礎。

內存的類型
++++++++++++++++++++++++++++++++++++++++++++++++


.. translate-collapse::

   There are many different types of memory in Linux, and each type has its
   own properties. Understanding the nuances of these is key to understanding
   why swap is important.

Linux 中內存分爲好幾種類型，每種都有各自的屬性。想理解爲什麼交換區很重要的關鍵一點在於理解這些的細微區別。

.. translate-collapse::

   For example, there are **pages ("blocks" of memory, typically 4k)**
   responsible for holding the code for each process being run on your computer.
   There are also pages responsible for caching data and metadata related to
   files accessed by those programs in order to speed up future access.
   These are part of the **page cache** , and I will refer to them as file memory.

比如說，有種 **頁面（「整塊」的內存，通常 4K）** 是用來存放電腦裏每個程序運行時各自的代碼的。
也有頁面用來保存這些程序所需要讀取的文件數據和元數據的緩存，以便加速隨後的文件讀寫。
這些內存頁面構成 **頁面緩存（page cache）**，後文中我稱他們爲文件內存。

.. translate-collapse::

   There are also pages which are responsible for the memory allocations
   made inside that code, for example, when new memory that has been allocated
   with :code:`malloc` is written to, or when using :code:`mmap`'s
   :code:`MAP_ANONYMOUS` flag. These are "anonymous" pages –
   so called because they are not backed by anything –
   and I will refer to them as anon memory.

還有一些頁面是在代碼執行過程中做的內存分配得到的，比如說，當代碼調用 :code:`malloc`
能分配到新內存區，或者使用 :code:`mmap` 的 :code:`MAP_ANONYMOUS` 標誌分配的內存。
這些是「匿名(anonymous)」頁面——之所以這麼稱呼它們是因爲他們沒有任何東西作後備——
後文中我稱他們爲匿名內存。


.. translate-collapse::

   There are other types of memory too –
   shared memory, slab memory, kernel stack memory, buffers, and the like –
   but anonymous memory and file memory are the most well known and
   easy to understand ones, so I will use these in my examples,
   although they apply equally to these types too.

還有其它類型的內存——共享內存、slab內存、內核棧內存、文件緩衝區（buffers），這種的——
但是匿名內存和文件內存是最知名也最好理解的，所以後面的例子裏我會用這兩個說明，
雖然後面的說明也同樣適用於別的這些內存類型。

可回收/不可回收內存
++++++++++++++++++++++++++++++++++++++++++++++++

.. translate-collapse::

   One of the most fundamental questions when thinking about a particular type
   of memory is whether it is able to be reclaimed or not.
   "Reclaim" here means that the system can, without losing data,
   purge pages of that type from physical memory.

考慮某種內存的類型時，一個非常基礎的問題是這種內存是否能被回收。
「回收（Reclaim）」在這裏是指系統可以，在不丟失數據的前提下，從物理內存中釋放這種內存的頁面。


.. translate-collapse::

   For some page types, this is typically fairly trivial. For example,
   in the case of clean (unmodified) page cache memory,
   we're simply caching something that we have on disk for performance,
   so we can drop the page without having to do any special operations.

對一些內存類型而言，是否可回收通常可以直接判斷。比如對於那些乾淨（未修改）的頁面緩存內存，
我們只是爲了性能在用它們緩存一些磁盤上現有的數據，所以我們可以直接扔掉這些頁面，
不需要做什麼特殊的操作。


.. translate-collapse::

   For some page types, this is possible, but not trivial. For example,
   in the case of dirty (modified) page cache memory, we can't just drop the page,
   because the disk doesn't have our modifications yet.
   As such we either need to deny reclamation or first get our changes back to
   disk before we can drop this memory.

對有些內存類型而言，回收是可能的，但是不是那麼直接。比如對髒（修改過）的頁面緩存內存，
我們不能直接扔掉這些頁面，因爲磁盤上還沒有寫入我們所做的修改。這種情況下，我們可以選擇拒絕回收，
或者選擇先等待我們的變更寫入磁盤之後才能扔掉這些內存。

.. translate-collapse::

   For some page types, this is not possible. For example,
   in the case of the anonymous pages mentioned previously,
   they only exist in memory and in no other backing store,
   so they have to be kept there.

對還有些內存類型而言，是不能回收的。比如前面提到的匿名頁面，它們只存在於內存中，沒有任何後備存儲，
所以它們必須留在內存裏。

說到交換區的本質
----------------------------------------


.. translate-collapse::

   If you look for descriptions of the purpose of swap on Linux,
   you'll inevitably find many people talking about it as if it is merely
   an extension of the physical RAM for use in emergencies. For example,
   here is a random post I got as one of the top results from typing
   "what is swap" in Google:

      Swap is essentially emergency memory; a space set aside for times
      when your system temporarily needs more physical memory than you
      have available in RAM. It's considered "bad" in the sense that
      it's slow and inefficient, and if your system constantly needs
      to use swap then it obviously doesn't have enough memory. […]
      If you have enough RAM to handle all of your needs, and don't
      expect to ever max it out, then you should be perfectly safe
      running without a swap space.

如果你去搜 Linux 上交換區的目的的描述，肯定會找到很多人說交換區只是在緊急時用來擴展物理內存的機制。
比如下面這段是我在 google 中輸入「什麼是 swap」 從前排結果中隨機找到的一篇：

   交換區本質上是緊急內存；是爲了應對你的系統臨時所需內存多餘你現有物理內存時，專門分出一塊額外空間。
   大家覺得交換區「不好」是因爲它又慢又低效，並且如果你的系統一直需要使用交換區那說明它明顯沒有足夠的內存。
   ［……］如果你有足夠內存覆蓋所有你需要的情況，而且你覺得肯定不會用滿內存，那麼完全可以不用交換區
   安全地運行系統。

.. translate-collapse::

   To be clear, I don't blame the poster of this comment at all for the content
   of their post – this is accepted as "common knowledge" by a lot of
   Linux sysadmins and is probably one of the most likely things that you will
   hear from one if you ask them to talk about swap. It is unfortunately also,
   however, a misunderstanding of the purpose and use of swap, especially on
   modern systems.

事先說明，我不想因爲這些文章的內容責怪這些文章的作者——這些內容被很多 Linux 系統管理員認爲是「常識」，
並且很可能你問他們什麼是交換區的時候他們會給你這樣的回答。但是也很不幸的是，
這種認識是使用交換區的目的的一種普遍誤解，尤其在現代系統上。

.. translate-collapse::

   Above, I talked about reclamation for anonymous pages being "not possible",
   as anonymous pages by their nature have no backing store to fall back to
   when being purged from memory – as such, their reclamation would result in
   complete data loss for those pages. What if we could create such a
   store for these pages, though?


前文中我說過回收匿名頁面的內存是「不可能的」，因爲匿名內存的特點，把它們從內存中清除掉之後，
沒有別的存儲區域能作爲他們的備份——因此，要回收它們會造成數據丟失。但是，如果我們爲這種內存頁面創建
一種後備存儲呢？

.. translate-collapse::

   Well, this is precisely what swap is for. Swap is a storage area for these
   seemingly "unreclaimable" pages that allows us to page them out to
   a storage device on demand. This means that they can now be considered as
   equally eligible for reclaim as their more trivially reclaimable friends,
   like clean file pages, allowing more efficient use of available physical memory.

嗯，這正是交換區存在的意義。交換區是一塊存儲空間，用來讓這些看起來「不可回收」的內存頁面在需要的時候
可以交換到存儲設備上。這意味着有了交換區之後，這些匿名頁面也和別的那些可回收內存一樣，
可以作爲內存回收的候選，就像乾淨文件頁面，從而允許更有效地使用物理內存。

.. translate-collapse::

   **Swap is primarily a mechanism for equality of reclamation,**
   **not for emergency "extra memory". Swap is not what makes your application**
   **slow – entering overall memory contention is what makes your application slow.**

**交換區主要是爲了平等的回收機制，而不是爲了緊急情況的「額外內存」。使用交換區不會讓你的程序變慢——**
**進入內存競爭的狀態才是讓程序變慢的元兇。**

.. translate-collapse::

  So in what situations under this "equality of reclamation"
  scenario would we legitimately choose to reclaim anonymous pages?
  Here are, abstractly, some not uncommon scenarios:

那麼在這種「平等的可回收機遇」的情況下，讓我們選擇回收匿名頁面的行爲在何種場景中更合理呢？
抽象地說，比如在下述不算罕見的場景中：

.. translate-collapse::

   #. During initialisation, a long-running program may allocate and
      use many pages. These pages may also be used as part of shutdown/cleanup,
      but are not needed once the program is "started" (in an
      application-specific sense). This is fairly common for daemons which
      have significant dependencies to initialise.
   #. During the program's normal operation, we may allocate memory which is
      only used rarely. It may make more sense for overall system performance
      to require a **major fault** to page these in from disk on demand,
      instead using the memory for something else that's more important.

#. 程序初始化的時候，那些長期運行的程序可能要分配和使用很多頁面。這些頁面可能在最後的關閉/清理的
   時候還需要使用，但是在程序「啓動」之後（以具體的程序相關的方式）持續運行的時候不需要訪問。
   對後臺服務程序來說，很多後臺程序要初始化不少依賴庫，這種情況很常見。
#. 在程序的正常運行過程中，我們可能分配一些很少使用的內存。對整體系統性能而言可能比起讓這些內存頁
   一直留在內存中，只有在用到的時候才按需把它們用 **缺頁異常（major fault）** 換入內存，
   可以空出更多內存留給更重要的東西。


.. panel-default::
    :title: `cgroupv2: Linux's new unified control group hierarchy (QCON London 2017) <https://www.youtube.com/watch?v=ikZ8_mRotT4>`_

    .. youtube:: ikZ8_mRotT4

考察有無交換區時會發生什麼
----------------------------------------

.. translate-collapse::

   Let's look at typical situations, and how they perform with and without
   swap present. I talk about metrics around "memory contention" in my 
   `talk on cgroup v2 <https://www.youtube.com/watch?v=ikZ8_mRotT4>`_ .

我們來看一些在常見場景中，有無交換區時分別會如何運行。
在我的 `關於 cgroup v2 的演講 <https://www.youtube.com/watch?v=ikZ8_mRotT4>`_
中探討過「內存競爭」的指標。

在無/低內存競爭的狀態下
++++++++++++++++++++++++++++++++++++++++++++++++

.. translate-collapse::

   - **With swap:** We can choose to swap out rarely-used anonymous memory that
     may only be used during a small part of the process lifecycle,
     allowing us to use this memory to improve cache hit rate,
     or do other optimisations.
   - **Without swap** We cannot swap out rarely-used anonymous memory,
     as it's locked in memory. While this may not immediately
     present as a problem, on some workloads this may represent
     a non-trivial drop in performance due to stale,
     anonymous pages taking space away from more important use.

- **有交换区:** 我們可以選擇換出那些只有在進程生存期內很小一部分時間會訪問的匿名內存，
  這允許我們空出更多內存空間用來提升緩存命中率，或者做別的優化。
- **無交換區:** 我們不能換出那些很少使用的匿名內存，因爲它們被鎖在了內存中。雖然這通常不會直接表現出問題，
  但是在一些工作條件下這可能造成卡頓導致不平凡的性能下降，因爲匿名內存佔着空間不能給
  更重要的需求使用。

.. panel-default::
    :title: 譯註：關於 **內存熱度** 和 **內存顛簸（thrash）**

    討論內核中內存管理的時候經常會說到內存頁的 **冷熱** 程度。這裏冷熱是指歷史上內存頁被訪問到的頻度，
    內存管理的經驗在說，歷史上在近期頻繁訪問的 **熱** 內存，在未來也可能被頻繁訪問，
    從而應該留在物理內存裏；反之歷史上不那麼頻繁訪問的 **冷** 內存，在未來也可能很少被用到，
    從而可以考慮交換到磁盤或者丟棄文件緩存。


    **顛簸（thrash）** 這個詞在文中出現多次但是似乎沒有詳細介紹，實際計算機科學專業的課程中應該有講過。
    一段時間內，讓程序繼續運行所需的熱內存總量被稱作程序的工作集（workset），估算工作集大小，
    換句話說判斷進程分配的內存頁中哪些屬於 **熱** 內存哪些屬於 **冷** 內存，是內核中
    內存管理的最重要的工作。當分配給程序的內存大於工作集的時候，程序可以不需要等待I/O全速運行；
    而當分配給程序的內存不足以放下整個工作集的時候，意味着程序每執行一小段就需要等待換頁或者等待
    磁盤緩存讀入所需內存頁，產生這種情況的時候，從用戶角度來看可以觀察到程序肉眼可見的「卡頓」。
    當系統中所有程序都內存不足的時候，整個系統都處於顛簸的狀態下，響應速度直接降至磁盤I/O的帶寬。
    如本文所說，禁用交換區並不能防止顛簸，只是從等待換頁變成了等待文件緩存，
    給程序分配超過工作集大小的內存才能防止顛簸。

在中/高內存競爭的狀態下
++++++++++++++++++++++++++++++++++++++++++++++++


.. translate-collapse::

   - **With swap:** All memory types have an equal possibility of being reclaimed. 
     This means we have more chance of being able to reclaim pages
     successfully – that is, we can reclaim pages that are not quickly
     faulted back in again (thrashing).
   - **Without swap** Anonymous pages are locked into memory as they have nowhere to go.
     The chance of successful long-term page reclamation is lower,
     as we have only some types of memory eligible to be reclaimed
     at all. The risk of page thrashing is higher. The casual
     reader might think that this would still be better as it might
     avoid having to do disk I/O, but this isn't true –
     we simply transfer the disk I/O of swapping to dropping
     hot page caches and dropping code segments we need soon.

- **有交换区:** 所有內存類型都有平等的被回收的可能性。這意味着我們回收頁面有更高的成功率——
  成功回收的意思是說被回收的那些頁面不會在近期內被缺頁異常換回內存中（顛簸）。
- **無交換區:** 匿名內存因爲無處可去所以被鎖在內存中。長期內存回收的成功率變低了，因爲我們成體上
  能回收的頁面總量少了。發生缺頁顛簸的危險性更高了。缺乏經驗的讀者可能覺得這某時也是好事，
  因爲這能避免進行磁盤I/O，但是實際上不是如此——我們只是把交換頁面造成的磁盤I/O變成了扔掉熱緩存頁
  和扔掉代碼段，這些頁面很可能馬上又要從文件中讀回來。

在臨時內存佔用高峰時
++++++++++++++++++++++++++++++++++++++++++++++++

.. translate-collapse::

   - **With swap:** We're more resilient to temporary spikes, but in cases of
     severe memory starvation, the period from memory thrashing beginning
     to the OOM killer may be prolonged. We have more visibility into the
     instigators of memory pressure and can act on them more reasonably,
     and can perform a controlled intervention.
   - **Without swap** The OOM killer is triggered more quickly as anonymous
     pages are locked into memory and cannot be reclaimed. We're more likely to
     thrash on memory, but the time between thrashing and OOMing is reduced.
     Depending on your application, this may be better or worse. For example,
     a queue-based application may desire this quick transfer from thrashing
     to killing. That said, this is still too late to be really useful –
     the OOM killer is only invoked at moments of severe starvation,
     and relying on this method for such behaviour would be better replaced
     with more opportunistic killing of processes as memory contention
     is reached in the first place.

- **有交换区:** 我們對內存使用激增的情況更有抵抗力，但是在嚴重的內存不足的情況下，
  從開始發生內存顛簸到 OOM 殺手開始工作的時間會被延長。內存壓力造成的問題更容易觀察到，
  從而可能更有效地應對，或者更有機會可控地干預。
- **無交換區:** 因爲匿名內存被鎖在內存中了不能被回收，所以 OOM 殺手會被更早觸發。
  發生內存顛簸的可能性更大，但是發生顛簸之後到 OOM 解決問題的時間間隔被縮短了。
  基於你的程序，這可能更好或是更糟。比如說，基於隊列的程序可能更希望這種從顛簸到殺進程的轉換更快發生。
  即便如此，發生 OOM 的時機通常還是太遲於是沒什麼幫助——只有在系統極度內存緊缺的情況下才會請出
  OOM 殺手，如果想依賴這種行爲模式，不如換成更早殺進程的方案，因爲在這之前已經發生內存競爭了。

好吧，所以我需要系統交換區，但是我該怎麼爲每個程序微調它的行爲？
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. translate-collapse::

   You didn't think you'd get through this entire post without me plugging cgroup v2, did you? ;-)

你肯定想到了我寫這篇文章一定會在哪兒插點 cgroup v2 的安利吧？ ;-)

.. translate-collapse::

   Obviously, it's hard for a generic heuristic algorithm to be right all the time,
   so it's important for you to be able to give guidance to the kernel.
   Historically the only tuning you could do was at the system level,
   using :code:`vm.swappiness` . This has two problems: :code:`vm.swappiness`
   is incredibly hard to reason about because it only feeds in as
   a small part of a larger heuristic system, and it also is system-wide
   instead of being granular to a smaller set of processes.

顯然，要設計一種對所有情況都有效的啓發算法會非常難，所以給內核提一些指引就很重要。
歷史上我們只能在整個系統層面做這方面微調，通過 :code:`vm.swappiness` 。這有兩方面問題：
:code:`vm.swappiness` 的行爲很難準確控制，因爲它只是傳遞給一個更大的啓發式算法中的一個小參數；
並且它是一個系統級別的設置，沒法針對一小部分進程微調。

.. translate-collapse::

   You can also use :code:`mlock` to lock pages into memory, but this requires
   either modifying program code, fun with :code:`LD_PRELOAD` , or doing
   horrible things with a debugger at runtime.
   In VM-based languages this also doesn't work very well, since you
   generally have no control over allocation and end up having to
   :code:`mlockall` , which has no precision towards the pages
   you actually care about.

你可以用 :code:`mlock` 把頁面鎖在內存裏，但是這要麼必須改程序代碼，或者折騰
:code:`LD_PRELOAD` ，或者在運行期用調試器做一些魔法操作。對基於虛擬機的語言來說這種方案也不能
很好工作，因爲通常你沒法控制內存分配，最後得用上 :code:`mlockall`
，而這個沒有辦法精確指定你實際上想鎖住的頁面。


.. translate-collapse::

   cgroup v2 has a tunable per-cgroup in the form of :code:`memory.low`
   , which allows us to tell the kernel to prefer other applications for
   reclaim below a certain threshold of memory used. This allows us to not
   prevent the kernel from swapping out parts of our application,
   but prefer to reclaim from other applications under memory contention.
   Under normal conditions, the kernel's swap logic is generally pretty good,
   and allowing it to swap out pages opportunistically generally increases
   system performance. Swap thrash under heavy memory contention is not ideal,
   but it's more a property of simply running out of memory entirely than
   a problem with the swapper. In these situations, you typically want to
   fail fast by self-killing non-critical processes when memory pressure
   starts to build up.

cgroup v2 提供了一套可以每個 cgroup 微調的 :code:`memory.low`
，允許我們告訴內核說當使用的內存低於一定閾值之後優先回收別的程序的內存。這可以讓我們不強硬禁止內核
換出程序的一部分內存，但是當發生內存競爭的時候讓內核優先回收別的程序的內存。在正常條件下，
內核的交換邏輯通常還是不錯的，允許它有條件地換出一部分頁面通常可以改善系統性能。在內存競爭的時候
發生交換顛簸雖然不理想，但是這更多地是單純因爲整體內存不夠了，而不是因爲交換進程（swapper）導致的問題。
在這種場景下，你通常希望在內存壓力開始積攢的時候通過自殺一些非關鍵的進程的方式來快速退出（fail fast）。

.. translate-collapse::

   You can not simply rely on the OOM killer for this. The OOM killer is
   only invoked in situations of dire failure when we've already entered
   a state where the system is severely unhealthy and may well have been
   so for a while. You need to opportunistically handle the situation yourself
   before ever thinking about the OOM killer.

你不能依賴 OOM 殺手達成這個。 OOM 殺手只有在非常急迫的情況下纔會出動，那時系統已經處於極度不健康的
狀態了，而且很可能在這種狀態下保持了一陣子了。需要在開始考慮 OOM 殺手之前，積極地自己處理這種情況。

.. translate-collapse::

   Determination of memory pressure is somewhat difficult using traditional
   Linux memory counters, though. We have some things which seem somewhat related,
   but are merely tangential – memory usage, page scans, etc – and from these
   metrics alone it's very hard to tell an efficient memory configuration
   from one that's trending towards memory contention. There is a group of us
   at Facebook, spearheaded by `Johannes <https://patchwork.kernel.org/project/LKML/list/?submitter=45>`_
   , working on developing new metrics that expose memory pressure more easily
   that should help with this in future. If you're interested in hearing more
   about this, 
   `I go into detail about one metric being considered in my talk on cgroup v2 <https://youtu.be/ikZ8_mRotT4?t=2145>`_.

不過，用傳統的 Linux 內存統計數據還是挺難判斷內存壓力的。我們有一些看起來相關的系統指標，但是都
只是支離破碎的——內存用量、頁面掃描，這些——單純從這些指標很難判斷系統是處於高效的內存利用率還是
在滑向內存競爭狀態。我們在 Facebook 有個團隊，由
`Johannes`_
牽頭，努力開發一些能評價內存壓力的新指標，希望能在今後改善目前的現狀。
如果你對這方面感興趣， `在我的 cgroup v2 的演講中介紹到一個被提議的指標 <https://youtu.be/ikZ8_mRotT4?t=2145>`_
。

調優
----------------------------------------

那麼，我需要多少交換空間？
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


.. translate-collapse::

   In general, the minimum amount of swap space required for optimal
   memory management depends on the number of anonymous pages pinned into
   memory that are rarely reaccessed by an application, and the value of
   reclaiming those anonymous pages. The latter is mostly a question of
   which pages are no longer purged to make way for these infrequently
   accessed anonymous pages.

通常而言，最優內存管理所需的最小交換空間取決於程序固定在內存中而又很少訪問到的匿名頁面的數量，
以及回收這些匿名頁面換來的價值。後者大體上來說是問哪些頁面不再會因爲要保留這些很少訪問的匿名頁面而
被回收掉騰出空間。

.. translate-collapse::

   If you have a bunch of disk space and a recent (4.0+) kernel,
   more swap is almost always better than less. In older kernels :code:`kswapd`,
   one of the kernel processes responsible for managing swap, was historically
   very overeager to swap out memory aggressively the more swap you had.
   In recent times, swapping behaviour when a large amount of swap space is
   available has been significantly improved. If you're running kernel 4.0+,
   having a larger swap on a modern kernel should not result in overzealous
   swapping. As such, if you have the space, having a swap size of a few GB
   keeps your options open on modern kernels.

如果你有足夠大的磁盤空間和比較新的內核版本（4.0+），越大的交換空間基本上總是越好的。
更老的內核上 :code:`kswapd` ， 內核中負責管理交換區的內核線程，在歷史上傾向於有越多交換空間就
急於交換越多內存出去。在最近一段時間，可用交換空間很大的時候的交換行爲已經改善了很多。
如果在運行 4.0+ 以後的內核，即便有很大的交換區在現代內核上也不會很激進地做交換。因此，
如果你有足夠的容量，現代內核上有個幾個 GB 的交換空間大小能讓你有更多選擇。

.. translate-collapse::

   If you're more constrained with disk space, then the answer really
   depends on the tradeoffs you have to make, and the nature of the environment.
   Ideally you should have enough swap to make your system operate optimally
   at normal and peak (memory) load. What I'd recommend is setting up a few
   testing systems with 2-3GB of swap or more, and monitoring what happens
   over the course of a week or so under varying (memory) load conditions.
   As long as you haven't encountered severe memory starvation during that week
   – in which case the test will not have been very useful – you will probably
   end up with some number of MB of swap occupied. As such, it's probably worth
   having at least that much swap available, in addition to a little buffer for
   changing workloads. :code:`atop` in logging mode can also show you which applications
   are having their pages swapped out in the :code:`SWAPSZ` column, so if you don't
   already use it on your servers to log historic server state you probably
   want to set it up on these test machines with logging mode as part of this
   experiment. This also tells you when your application started swapping out
   pages, which you can tie to log events or other key data.

如果你的磁盤空間有限，那麼答案更多取決於你願意做的取捨，以及運行的環境。理想上應該有足夠的交換空間
能高效應對正常負載和高峰（內存）負載。我建議先用 2-3GB 或者更多的交換空間搭個測試環境，
然後監視在不同（內存）負載條件下持續一週左右的情況。只要在那一週裏沒有發生過嚴重的內存不足——
發生了的話說明測試結果沒什麼用——在測試結束的時候大概會留有多少 MB 交換區佔用。
作爲結果說明你至少應該有那麼多可用的交換空間，再多加一些以應對負載變化。用日誌模式跑 :code:`atop`
可以在 :code:`SWAPSZ` 欄顯示程序的頁面被交換出去的情況，所以如果你還沒用它記錄服務器歷史日誌的話
，這次測試中可以試試在測試機上用它記錄日誌。這也會告訴你什麼時候你的程序開始換出頁面，你可以用這個
對照事件日誌或者別的關鍵數據。

.. translate-collapse::

   Another thing worth considering is the nature of the swap medium.
   Swap reads tend to be highly random, since we can't reliably predict
   which pages will be refaulted and when. On an SSD this doesn't matter much,
   but on spinning disks, random I/O is extremely expensive since it requires
   physical movement to achieve. On the other hand, refaulting of file pages
   is likely less random, since files related to the operation of a single
   application at runtime tend to be less fragmented. This might mean that on
   a spinning disk you may want to bias more towards reclaiming file pages
   instead of swapping out anonymous pages, but again, you need to test and
   evaluate how this balances out for your workload.

另一點值得考慮的是交換空間所在存儲設備的媒介。讀取交換區傾向於很隨機，因爲我們不能可靠預測什麼時候
什麼頁面會被再次訪問。在 SSD 上這不是什麼問題，但是在傳統磁盤上，隨機 I/O 操作會很昂貴，
因爲需要物理動作尋道。另一方面，重新加載文件緩存可能不那麼隨機，因爲單一程序在運行期的文件讀操作
一般不會太碎片化。這可能意味着在傳統磁盤上你想更多地回收文件頁面而不是換出匿名頁面，但仍就，
你需要做測試評估在你的工作負載下如何取得平衡。


.. panel-default::
   :title: 譯註：關於休眠到磁盤時的交換空間大小

   原文這裏建議交換空間至少是物理內存大小，我覺得實際上不需要。休眠到磁盤的時候內核會寫回並丟棄
   所有有文件作後備的可回收頁面，交換區只需要能放下那些沒有文件後備的頁面就可以了。
   如果去掉文件緩存頁面之後剩下的已用物理內存總量能完整放入交換區中，就可以正常休眠。
   對於桌面瀏覽器這種內存大戶，通常有很多緩存頁可以在休眠的時候丟棄。

.. translate-collapse::

   For laptop/desktop users who want to hibernate to swap, this also needs to
   be taken into account – in this case your swap file should be at least
   your physical RAM size.

對筆記本/桌面用戶如果想要休眠到交換區，這也需要考慮——這種情況下你的交換文件應該至少是物理內存大小。

我的 swappiness 應該如何設置？
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. translate-collapse::

   First, it's important to understand what :code:`vm.swappiness` does.
   :code:`vm.swappiness` is a sysctl that biases memory reclaim either towards
   reclamation of anonymous pages, or towards file pages. It does this using two
   different attributes: :code:`file_prio` (our willingness to reclaim file pages)
   and :code:`anon_prio` (our willingness to reclaim anonymous pages).
   :code:`vm.swappiness`plays into this, as it becomes the default value for
   :code:`anon_prio`, and it also is subtracted from the default value of 200
   for :code:`file_prio`, which means for a value of :code:`vm.swappiness = 50`,
   the outcome is that :code:`anon_prio` is 50, and :code:`file_prio` is 150
   (the exact numbers don't matter as much as their relative weight compared to the other).

首先很重要的一點是，要理解 :code:`vm.swappiness` 是做什麼的。
:code:`vm.swappiness` 是一個 sysctl 用來控制在內存回收的時候，是優先回收匿名頁面，
還是優先回收文件頁面。內存回收的時候用兩個屬性： :code:`file_prio` （回收文件頁面的傾向）
和 :code:`anon_prio` （回收匿名頁面的傾向）。 :code:`vm.swappiness` 控制這兩個值，
因爲它是 :code:`anon_prio` 的默認值，然後也是默認 200 減去它之後 :code:`file_prio` 的默認值。
意味着如果我們設置 :code:`vm.swappiness = 50` 那麼結果是 :code:`anon_prio` 是 50，
:code:`file_prio` 是 150 （這裏數值本身不是很重要，重要的是兩者之間的權重比）。



.. panel-default::
   :title: 譯註：關於 SSD 上的 swappiness

   原文這裏說 SSD 上 swap 和 drop page cache 差不多開銷所以 :code:`vm.swappiness = 100`
   。我覺得實際上要考慮 swap out 的時候會產生寫入操作，而 drop page cache 可能不需要寫入（
   要看頁面是否是髒頁）。如果負載本身對I/O帶寬比較敏感，稍微調低 swappiness 可能對性能更好，
   內核的默認值 60 是個不錯的默認值。以及桌面用戶可能對性能不那麼關心，反而更關心 SSD
   的寫入壽命，雖然說 SSD 寫入壽命一般也足夠桌面用戶，不過調低 swappiness
   可能也能減少一部分不必要的寫入（因爲寫回髒頁是必然會發生的，而寫 swap 可以避免）。
   當然太低的 swappiness 會對性能有負面影響（因爲太多匿名頁面留在物理內存裏而降低了緩存命中率）
   ，這裏的權衡也需要根據具體負載做測試。

   另外澄清一點誤解， swap 分區還是 swap 文件對系統運行時的性能而言沒有差別。或許有人會覺得
   swap 文件要經過文件系統所以會有性能損失，在譯文之前譯者說過 Linux 的內存管理子系統基本上獨立於文件系統。
   實際上 Linux 上的 swapon 在設置 swap 文件作爲交換空間的時候會讀取一次文件系統元數據，
   確定 swap 文件在磁盤上的地址範圍，隨後運行的過程中做交換就和文件系統無關了。關於 swap
   空間是否連續的影響，因爲 swap 讀寫基本是頁面單位的隨機讀寫，所以即便連續的 swap 空間（swap
   分區）也並不能改善 swap 的性能。希疏文件的地址範圍本身不連續，寫入希疏文件的空洞需要
   文件系統分配磁盤空間，所以在 Linux 上交換文件不能是希疏文件。只要不是希疏文件，
   連續的文件內地址範圍在磁盤上是否連續（是否有文件碎片）基本不影響能否 swapon 或者使用 swap 時的性能。

.. translate-collapse::

   This means that, in general, :code:`vm.swappiness` **is simply a ratio of how**
   **costly reclaiming and refaulting anonymous memory is compared to file memory**
   **for your hardware and workload**. The lower the value, the more you tell the
   kernel that infrequently accessed anonymous pages are expensive to swap out
   and in on your hardware. The higher the value, the more you tell the kernel
   that the cost of swapping anonymous pages and file pages is similar on your
   hardware. The memory management subsystem will still try to mostly decide
   whether it swaps file or anonymous pages based on how hot the memory is,
   but swappiness tips the cost calculation either more towards swapping or
   more towards dropping filesystem caches when it could go either way.
   On SSDs these are basically as expensive as each other, so setting
   :code:`vm.swappiness = 100` (full equality) may work well.
   On spinning disks, swapping may be significantly more expensive since
   swapping in generally requires random reads, so you may want to
   bias more towards a lower value.

這意味着，通常來說 :code:`vm.swappiness` **只是一個比例，用來衡量在你的硬件和工作負載下，**
**回收和換回匿名內存還是文件內存哪種更昂貴** 。設定的值越低，你就是在告訴內核說換出那些不常訪問的
匿名頁面在你的硬件上開銷越昂貴；設定的值越高，你就是在告訴內核說在你的硬件上交換匿名頁和
文件緩存的開銷越接近。內存管理子系統仍然還是會根據實際想要回收的內存的訪問熱度嘗試自己決定具體是
交換出文件還是匿名頁面，只不過 swappiness 會在兩種回收方式皆可的時候，在計算開銷權重的過程中左右
是該更多地做交換還是丟棄緩存。在 SSD 上這兩種方式基本上是同等開銷，所以設成
:code:`vm.swappiness = 100` （同等比重）可能工作得不錯。在傳統磁盤上，交換頁面可能會更昂貴，
因爲通常需要隨機讀取，所以你可能想要設低一些。

.. translate-collapse::

   The reality is that most people don't really have a feeling about which
   their hardware demands, so it's non-trivial to tune this value based on
   instinct alone – this is something that you need to test using different
   values. You can also spend time evaluating the memory composition of your
   system and core applications and their behaviour under mild memory reclamation.

現實是大部分人對他們的硬件需求沒有什麼感受，所以根據直覺調整這個值可能挺困難的 ——
你需要用不同的值做測試。你也可以花時間評估一下你的系統的內存分配情況和核心應用在大量回收內存的時候的行爲表現。

.. translate-collapse::

   When talking about :code:`vm.swappiness` , an extremely important change to
   consider from recent(ish) times is 
   `this change to vmscan by Satoru Moriya in 2012 <https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/patch/?id=fe35004fbf9eaf67482b074a2e032abb9c89b1dd>`_
   , which changes the way that :code:`vm.swappiness = 0` is handled
   quite significantly.

討論 :code:`vm.swappiness` 的時候，一個極爲重要需要考慮的修改是（相對）近期在
`2012 年左右 Satoru Moriya 對 vmscan 行爲的修改 <https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/patch/?id=fe35004fbf9eaf67482b074a2e032abb9c89b1dd>`_
，它顯著改變了代碼對 :code:`vm.swappiness = 0` 這個值的處理方式。

.. translate-collapse::

   Essentially, the patch makes it so that we are extremely biased against
   scanning (and thus reclaiming) any anonymous pages at all with
   :code:`vm.swappiness = 0` , unless we are already encountering severe
   memory contention. As mentioned previously in this post, that's generally
   not what you want, since this prevents equality of reclamation prior to
   extreme memory pressure occurring, which may actually lead to this
   extreme memory pressure in the first place. :code:`vm.swappiness = 1`
   is the lowest you can go without invoking the special casing for
   anonymous page scanning implemented in that patch.

基本上來說這個補丁讓我們在 :code:`vm.swappiness = 0` 的時候會極度避免掃描（進而回收）匿名頁面，
除非我們已經在經歷嚴重的內存搶佔。就如本文前面所屬，這種行爲基本上不會是你想要的，
因爲這種行爲會導致在發生內存搶佔之前無法保證內存回收的公平性，這甚至可能是最初導致發生內存搶佔的原因。
想要避免這個補丁中對掃描匿名頁面的特殊行爲的話， :code:`vm.swappiness = 1` 是你能設置的最低值。


.. translate-collapse::

   The kernel default here is :code:`vm.swappiness = 60`. This value is
   generally not too bad for most workloads, but it's hard to have a
   general default that suits all workloads. As such, a valuable extension
   to the tuning mentioned in the "how much swap do I need" section above
   would be to test these systems with differing values for :code:`vm.swappiness`
   , and monitor your application and system metrics under heavy (memory) load.
   Some time in the near future, once we have a decent implementation of
   `refault detection <https://youtu.be/ikZ8_mRotT4?t=2145>`_ in the kernel,
   you'll also be able to determine this somewhat workload-agnostically by
   looking at cgroup v2's page refaulting metrics.

內核在這裏設置的默認值是 :code:`vm.swappiness = 60` 。這個值對大部分工作負載來說都不會太壞，
但是很難有一個默認值能符合所有種類的工作負載。因此，對上面「 `那麼，我需要多少交換空間？`_
」那段討論的一點重要擴展可以說，在測試系統中可以嘗試使用不同的 :code:`vm.swappiness`
，然後監視你的程序和系統在重（內存）負載下的性能指標。在未來某天，如果我們在內核中有了合理的
`缺頁檢測 <https://youtu.be/ikZ8_mRotT4?t=2145>`_ ，你也將能通過 cgroup v2 的頁面缺頁
指標來以負載無關的方式決定這個。


.. panel-default::
    :title: `SREcon19 Asia/Pacific - Linux Memory Management at Scale: Under the Hood <https://www.youtube.com/watch?v=beefUhRH5lU>`_

    .. youtube:: beefUhRH5lU

2019年07月更新：內核 4.20+ 中的內存壓力指標
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. translate-collapse::

   The refault metrics mentioned as in development earlier are now in the
   kernel from 4.20 onwards and can be enabled with :code:`CONFIG_PSI=y`
   . See my talk at SREcon at around the 25:05 mark:

前文中提到的開發中的內存缺頁檢測指標已經進入 4.20+ 以上版本的內核，可以通過
:code:`CONFIG_PSI=y` 開啓。詳情參見我在 SREcon 大約 25:05 左右的討論。

結論
-----------------------------------------------

.. translate-collapse::

   - Swap is a useful tool to allow equality of reclamation of memory pages,
     but its purpose is frequently misunderstood, leading to its negative
     perception across the industry. If you use swap in the spirit intended,
     though – as a method of increasing equality of reclamation – you'll
     find that it's a useful tool instead of a hindrance.
   - Disabling swap does not prevent disk I/O from becoming a problem under
     memory contention, it simply shifts the disk I/O thrashing from anonymous
     pages to file pages. Not only may this be less efficient, as we have
     a smaller pool of pages to select from for reclaim, but it may also
     contribute to getting into this high contention state in the first place.
   - Swap can make a system slower to OOM kill, since it provides another,
     slower source of memory to thrash on in out of memory situations – the
     OOM killer is only used by the kernel as a last resort, after things have
     already become monumentally screwed. The solutions here depend on your system:

     - You can opportunistically change the system workload depending on
       cgroup-local or global memory pressure. This prevents getting into these
       situations in the first place, but solid memory pressure metrics are
       lacking throughout the history of Unix. Hopefully this should be
       better soon with the addition of refault detection.
     - You can bias reclaiming (and thus swapping) away from certain processes
       per-cgroup using memory.low, allowing you to protect critical daemons
       without disabling swap entirely.

- 交換區是允許公平地回收內存的有用工具，但是它的目的經常被人誤解，導致它在業內這種負面聲譽。如果
  你是按照原本的目的使用交換區的話——作爲增加內存回收公平性的方式——你會發現它是很有效的工具而不是阻礙。
- 禁用交換區並不能在內存競爭的時候防止磁盤I/O的問題，它只不過把匿名頁面的磁盤I/O變成了文件頁面的
  磁盤I/O。這不僅更低效，因爲我們回收內存的時候能選擇的頁面範圍更小了，而且它可能是導致高度內存競爭
  狀態的元兇。
- 有交換區會導致系統更慢地使用 OOM 殺手，因爲在缺少內存的情況下它提供了另一種更慢的內存，
  會持續地內存顛簸——內核調用 OOM 殺手只是最後手段，會晚於所有事情已經被搞得一團糟之後。
  解決方案取決於你的系統：

  - 你可以預先更具每個 cgroup 的或者系統全局的內存壓力改變系統負載。這能防止我們最初進入內存競爭
    的狀態，但是 Unix 的歷史中一直缺乏可靠的內存壓力檢測方式。希望不久之後在有了
    `缺頁檢測 <https://youtu.be/ikZ8_mRotT4?t=2145>`_ 這樣的性能指標之後能改善這一點。
  - 你可以使用 :code:`memory.low` 讓內核不傾向於回收（進而交換）特定一些 cgroup 中的進程，
    允許你在不禁用交換區的前提下保護關鍵後臺服務。

-------------------------

感謝在撰寫本文時 `Rahul <https://github.com/rahulg>`_ ，
`Tejun <https://github.com/htejun>`_ 和 
`Johannes <https://patchwork.kernel.org/project/LKML/list/?submitter=45>`_
提供的諸多建議和反饋。