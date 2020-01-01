Btrfs vs ZFS 實現 snapshot 的差異
================================================

:slug: btrfs-vs-zfs-difference-in-implementing-snapshots
:translation_id: btrfs-vs-zfs-difference-in-implementing-snapshots
:lang: zh
:date: 2020-01-01 13:45
:tags: btrfs, zfs, cow, snapshot, clone, subvolume, dedup, reflink
:series: FS notes
:status: draft


Btrfs 和 ZFS 都是開源的寫時複製(Copy on Write, CoW）文件系統，都提供了相似的子卷管理和
快照(snapshot）的功能。網上有不少文章都評價 ZFS 實現 CoW FS 的創新之處，進而想說「 Btrfs
只是 Linux/GPL 陣營對 ZFS 的拙劣抄襲」，或許（在存儲領域人盡皆知而領域外）鮮有人知在 ZFS
之前就有 `NetApp <https://en.wikipedia.org/wiki/NetApp>`_ 的商業產品
`WAFL(Write Anywhere File Layout) <https://en.wikipedia.org/wiki/Write_Anywhere_File_Layout>`_
實現了 CoW 語義的文件系統，並且集成了快照和卷管理之類的功能。我一開始也帶着「 Btrfs 和 ZFS
都提供了類似的功能，因此兩者必然有類似的設計」這樣的先入觀念，嘗試去使用這兩個文件系統，
卻經常撞上兩者細節上的差異，導致使用時需要不盡相同的工作流，
或者看似相似的用法有不太一樣的性能表現，又或者一邊有的功能（比如 ZFS 的 inband dedup ，
Btrfs 的 reflink ）在另一邊沒有的情況。

爲了更好地理解這些差異，我四處查詢這兩個文件系統的實現細節，於是有了這篇筆記，
記錄一下我查到的種種發現和自己的理解。:del:`（或許會寫成一個系列？還是先別亂挖坑不填。）`
只是自己的筆記，所有參閱的資料文檔都是二手資料，沒有深挖過源碼，還參雜了自己的理解，
於是難免有和事實相違的地方，如有寫錯，還請留言糾正。

Btrfs 的子卷和快照
-------------------------------------------------------------------

先從兩個文件系統中（表面上看起來）比較簡單的 btrfs 的子卷（subvolume）和快照（snapshot）說起。

在 btrfs 中，存在於存儲媒介中的只有「子卷」的概念，「快照」只是個創建「子卷」的方式，
換句話說在 btrfs 的術語裏，子卷（subvolume）是個名詞，而快照（snapshot）是個動詞。
如果脫離了 btrfs 術語的上下文，或者不精確地隨口說說的時候，也經常有人把 btrfs
的快照命令創建出的子卷叫做一個快照。或者我們可以理解爲，
**互相共享一部分元數據（metadata）的子卷互爲彼此的快照（名詞）** ，
那麼按照這個定義的話，在 btrfs 中創建快照（名詞）的方式其實有兩種：

1. 通過 :code:`btrfs subvolume snapshot` 命令創建快照
2. 通過 :code:`btrfs send` 命令並使用 :code:`-p` 參數發送快照，並在管道另一端接收

定義中「互相共享一部分 **元數據** 」比較重要，因爲除了快照的方式之外， btrfs
的子卷間也可以通過 reflink 的形式共享數據塊。我們可以對一整個子卷（甚至目錄）執行
:code:`cp -r --reflink=always` ，創建出一個副本，副本的文件內容和原本的數據通過 reflink
共享數據，而不共享元數據，這樣創建出的就不是快照。

這裏也順便提一下 :code:`btrfs send` 命令的 :code:`-p` 參數和 :code:`-c` 參數的差異。
只看 `btrfs-send(8) <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-send#DESCRIPTION>`_ 的描述的話：

| -p <parent>
|     send an incremental stream from parent to subvol
|
| -c <clone-src>
|     use this snapshot as a clone source for an incremental send (multiple allowed)

看起來這兩個都可以用來生成兩個快照之間的差分，只不過 -p 只能指定一個「parent」，
而 -c 能指定多個「clone source」。在
`unix stackexchange 上有人寫明了這兩個的異同 <https://unix.stackexchange.com/a/490857>`_
。使用 -p 的時候，產生的差分首先讓接收端用 subvolume snapshot 命令對 parent 子卷創建一個快照，
然後發送指令將這個快照修改成目標子卷的樣子，而使用 -c 的時候，首先在接收端用 subvolume create
創建一個空的子卷，隨後發送指令在這個子卷中填充內容，其數據塊儘量共享 clone source 已有的數據。
所以 :code:`btrfs send -p` 在接收端產生是有共享元數據的快照，而 :code:`btrfs send -c`
在接收端產生的是僅僅共享數據而不共享元數據的子卷。