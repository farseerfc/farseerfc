從 fsck 到 CoW: 文件系統與硬件意外的戰爭
================================================

:slug: from-fsck-to-cow-war-between-fs-and-hardware-failure
:translation_id: from-fsck-to-cow-war-between-fs-and-hardware-failure
:lang: zh
:date: 2020-02-20 15:45
:tags: FS筆記, FS notes, btrfs, zfs, cow, snapshot, clone, subvolume, dedup, reflink, SPA, DMU, DSL, ZPL
:series: FS筆記
:status: draft


.. contents:: 目錄

上一篇「`Btrfs vs ZFS 實現 snapshot 的差異 <{filename}./btrfs-vs-zfs-difference-in-implementing-snapshots>`_
」講到兩個主要的寫時拷貝（Copy on Write, CoW）文件系統（Filesystem, FS
），但是沒提爲什麼我們需要 CoW FS 。

.. tikz::
    :libs: automata,positioning

    \draw[help lines]       (0,0)                       grid (3,2);
    \node[state,initial]    (q_0)                       {$q_0$};
    \node[state]            (q_1) [above right=of q_0]  {$q_1$};
    \node[state]
    (q_2) [below right=of q_0]
    {$q_2$};
    \node[state,accepting](q_3) [below right=of q_1]
    {$q_3$};
    \path[->] (q_0) edge
    node
    {0} (q_1)
    edge
    node [swap] {1} (q_2)
    (q_1) edge
    node
    {1} (q_3)
    edge [loop above]
    node
    {0} ()
    (q_2) edge
    node [swap] {0} (q_3)
    edge [loop below]
    node
    {1} ();


test7