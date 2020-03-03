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
    :libs: positioning,calc
    
    
        \def\centerarc[#1](#2)(#3:#4:#5:#6)% Syntax: [draw options] (center) (initial angle:final angle:radius)
        { \draw[#1] ($(#2)+({#5*cos(#3)},{#6*sin(#3)})$) arc [start angle=#3, end angle=#4, x radius=#5, y radius=#6]; }

        \def\sectors(#1){
            \foreach \r in {1.0,1.2,...,2.0} {
                \foreach \x in {0,20,...,350} { \centerarc[](#1)(\x:\x+18:\r*2:\r); };
            };
        };
        \def\plate[#1](#2){
            \filldraw[fill=#1!50!white] (#2) ellipse [x radius=4, y radius=2];
            \fill[#1!40!white] (#2) ellipse [x radius=3.5, y radius=1.75]; 
            \fill[#1!30!white] (#2) ellipse [x radius=3, y radius=1.5]; 
            \fill[#1!20!white] (#2) ellipse [x radius=2.5, y radius=1.25]; 
            \draw[fill=white] (#2) ellipse [x radius=2, y radius=1];
        }
        %\draw[help lines]  (0,0) grid (20,10);

        \plate[red](4,0);
        \sectors(4,0);
        \plate[orange](4,1);
        \sectors(4,1);
        \draw (0,0) -- (0,1);  \draw (8,0) -- (8,1);
        \draw (4,1) node {Plate 3};
        

        \plate[yellow](4,4);
        \sectors(4,4);
        \plate[green](4,5);
        \sectors(4,5);
        \draw (0,4) -- (0,5);  \draw (8,4) -- (8,5);
        \draw (4,5) node {Plate 2};

        \plate[cyan](4,8);
        \sectors(4,8);
        \plate[blue](4,9);	
        \sectors(4,9);
        \draw (0,8) -- (0,9);  \draw (8,8) -- (8,9);
        \draw (4,9) node {Plate 1};

        \draw (-1,9) node {Head 1};
        \draw (-1,8) node {Head 2};
        \draw (-1,5) node {Head 3};
        \draw (-1,4) node {Head 4};
        \draw (-1,1) node {Head 5};
        \draw (-1,0) node {Head 6};

        %\plate[white](15,5);
        %\sectors(15,5);
        \foreach \x in {0,20,...,350} { \centerarc[red!80!black, thick](4,9)(\x:\x+18:3.6:1.8); };
        \draw[red!80!black, ->, very thick, fill=white, text=black] (4,12) node[above] {Track} -> (4,10.8);




test7