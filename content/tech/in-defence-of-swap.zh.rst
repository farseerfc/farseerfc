【譯】替 swap 辯護：常見誤解
====================================================================

:slug: in-defence-of-swap
:translation_id: in-defence-of-swap
:lang: zh
:date: 2020-09-28 15:45
:tags: swap, mm, memory management, translate, swappiness
:issueid: 97
:status: draft

這篇翻譯自 Chris Down 的博客
`In defence of swap: common misconceptions <https://chrisdown.name/2018/01/02/in-defence-of-swap.html>`_
，下面是原文翻譯。


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

#. 對正常功能的系統而言，有 swap 是相對挺重要的一部分。沒有它的話很難做到合理的內存管理。
#. swap 的目的通常並不是用作緊急內存，它的目的在於讓內存回收能更平等高效。
   事實上把它當作「緊急內存」來用通常是有害的。
#. 禁用 swap 在內存壓力下並不能避免磁盤I/O造成的性能問題，這麼做只是讓磁盤I/O顛簸的範圍從
   匿名頁面轉化到文件頁面。這不僅更低效，因爲系統能回收的頁面的選擇範圍更有限了，
   而且這還可能是最初導致內存壓力的原因之一。
#. 內核 4.0 版本之前的交換進程（swapper）有一些問題，導致很多人對 swap 有負面印象，
   因爲它太急於（overeagerness）把頁面交換出去。在 4.0 之後的內核上這種情況已經改善了很多。
#. 在 SSD 上，交換出匿名頁面的開銷和回收文件頁面的開銷基本上在性能/延遲方面沒有區別。
   在磁盤上，讀取交換文件因爲屬於隨機訪問讀取所以會更慢，於是較低的 :code:`vm.swappiness`
   設置可能比較合理（繼續讀下面關於 :code:`vm.swappiness` 的描述）。


------------


.. translate-collapse::

   As part of my work improving kernel memory management and cgroup v2,
   I've been talking to a lot of engineers about attitudes towards memory
   management, especially around application behaviour under pressure and
   operating system heuristics used under the hood for memory management.

As part of my work improving kernel memory management and cgroup v2,
I've been talking to a lot of engineers about attitudes towards memory
management, especially around application behaviour under pressure and
operating system heuristics used under the hood for memory management.


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

