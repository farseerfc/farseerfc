柱面-磁頭-扇區尋址的一些舊事
================================================

:slug: history-of-chs-addressing
:translation_id: history-of-chs-addressing
:lang: zh
:date: 2020-02-21 15:45
:tags: FS筆記, FS notes, CHS, cylinder, head, sector 
:series: FS筆記
:status: draft

在 SSD 這種新興存儲設備普及之前，很長一段時間硬盤是個人計算機的主要存儲設備。
更往前的磁帶機不常見於個人計算機，軟盤的地位很快被硬盤取代，到 SSD 出現爲止像
`MiniDisc <https://en.wikipedia.org/wiki/MiniDisc>`_ 、
`DVD-RAM <https://en.wikipedia.org/wiki/DVD-RAM>`_
等存儲設備也從未能挑戰過硬盤的地位。硬盤作爲主要存儲設備，自然也影響了文件系統的設計。

這篇筆記稍微聊一聊硬盤這種存儲設備的尋址方式對早期文件系統設計的一些影響，特別是
柱面-磁頭-扇區尋址（Cylinder-head-sector addressing, 簡稱CHS尋址）的起源和發展。
現今的硬盤已經不再採用 CHS 尋址，其影響卻還能在一些文件系統設計中看到影子。

柱面、磁頭、扇區以及相關術語
----------------------------------------------------------


.. panel-default::
    :title: 磁盤示意圖（來自維基百科 `Cylinder-head-sector 詞條 <https://en.wikipedia.org/wiki/Cylinder-head-sector>`_ ）

    .. image:: {static}/images/chs-illustrate-trans.svg
        :alt: chs-illustrate-trans.svg

如右圖所示，一塊硬盤(Hard Disk Drive, HDD)是一個圓柱體轉軸上套着一些磁碟片(plate)，
然後有一條磁頭臂(actuator arm)插入磁碟片間的位置，加上一組控制芯片（controller）。
每個磁碟片有上下兩面塗有磁性材質，磁頭臂上有一組磁頭（head），每個磁頭對應磁盤的一個面，
所以比如一個 3 碟的磁盤會有 6 個磁頭。

每個磁碟片上定義了很多同心圓，叫做磁道（track），磁道位於盤面上不同半徑的位置，
通過旋轉磁碟臂能讓磁頭移動到特定的半徑上，從而讓讀寫磁頭在不同的磁道間跳轉。
不同磁頭上同磁道的同心圓共同組成一個柱面（cylinder），或者說移動磁碟臂能選定磁盤中的一個柱面。
磁道上按等角度切分成多個小段，叫做扇區（sector），每個扇區是讀寫數據時採用的最小單元。

早期軟盤和硬盤的尋址方式被稱作「柱面-磁頭-扇區尋址」，簡稱 CHS 尋址，
是因爲這三個參數是軟件交給硬件定位到某個具體扇區單元時使用的參數。
首先柱面參數讓磁頭臂移動到某個半徑上，尋址到某個柱面，然後激活某個磁頭，然後隨着盤面旋轉，
磁頭定位到某個扇區上。

「柱面-磁頭-扇區」這個尋址方式，聽起來可能不太符合直覺，尤其是柱面的概念。直覺上，
可能更合理的尋址方式是「盤片-盤面-磁道-扇區」，而柱面在這裏是同磁道不同盤片盤面構成的一個集合。
不過理解了磁盤的機械結構的話，柱面的概念就比較合理了，尋址時先驅動磁頭臂旋轉，
磁頭臂上多個磁頭一起飛到某個磁道上，從而運動磁頭臂的動作定義了一個柱面。


.. tikz::
    :libs: positioning,calc,decorations.pathreplacing
    
    \def\centerarc[#1](#2)(#3:#4:#5:#6){
        \draw[#1] ($(#2)+({#5*cos(#3)},{#6*sin(#3)})$) arc [start angle=#3, end angle=#4, x radius=#5, y radius=#6];
    }
    \def\sectors(#1){
        \foreach \r in {1.1,1.3,...,1.9} {
            \foreach \x in {0,20,...,350} { \centerarc[](#1)(\x:\x+18:(\r+\r):(\r)); };
        };
    }
    \def\plate[#1](#2){
        \filldraw[fill=#1!50!white, thick] (#2) ellipse [x radius=4, y radius=2];
        \fill[#1!40!white] (#2) ellipse [x radius=3.6, y radius=1.8]; 
        \fill[#1!30!white] (#2) ellipse [x radius=3.2, y radius=1.6]; 
        \fill[#1!20!white] (#2) ellipse [x radius=2.8, y radius=1.4]; 
        \fill[#1!10!white] (#2) ellipse [x radius=2.4, y radius=1.2]; 
        \draw[fill=white] (#2) ellipse [x radius=2, y radius=1];
    }

    \plate[red](4,0);       \sectors(4,0);
    \plate[orange](4,1);    \sectors(4,1);
    \draw[thick] (0,0) -- (0,1) (8,0) -- (8,1);
    \draw (4,1) node {磁碟3};
    
    \plate[yellow](4,4);    \sectors(4,4);
    \plate[green](4,5);     \sectors(4,5);
    \draw[thick] (0,4) -- (0,5)  (8,4) -- (8,5);
    \draw (4,5) node {磁碟2};

    \plate[cyan](4,8);      \sectors(4,8);
    \plate[blue](4,9);      \sectors(4,9);
    \draw[thick] (0,8) -- (0,9)  (8,8) -- (8,9);
    \draw (4,9) node {磁碟1};

    \draw (-1,9) node {磁頭0};
    \draw (-1,8) node {磁頭1};
    \draw (-1,5) node {磁頭2};
    \draw (-1,4) node {磁頭3};
    \draw (-1,1) node {磁頭4};
    \draw (-1,0) node {磁頭5};

    \foreach \x in {0,20,...,350} { \centerarc[red!80!black, thick](4,9)(\x:\x+18:3.8:1.9); };
    \draw[red!80!black, ->, very thick, fill=white, text=black] (4,12) node[above] {磁道} -> (4,10.9);

    \def\sectorline[#1](#2,#3,#4){
        \fill[#1!50!white] (#2,#3+3.0) rectangle (#2+7.75,#3+3.5);\draw[dash pattern=on 20 off 3, very thick] (#2+0.25,#3+3.25) -- (#2+7.5,#3+3.25);
        \draw (#2,#3+3.25) node[left] {磁頭 #4};
        \fill[#1!40!white] (#2,#3    ) rectangle (#2+7.75,#3+0.5);\draw[dash pattern=on 20 off 3, very thick] (#2+0.25,#3+0.25) -- (#2+7.5,#3+0.25);
        \draw (#2,#3+0.25) node[left] {磁頭 #4};
        \fill[#1!30!white] (#2,#3-2.5) rectangle (#2+7.75,#3-3.0);\draw[dash pattern=on 20 off 3, very thick] (#2+0.25,#3-2.75) -- (#2+7.5,#3-2.75);
        \draw (#2,#3-2.75) node[left] {磁頭 #4};
        \fill[#1!20!white] (#2,#3-5.5) rectangle (#2+7.75,#3-6.0);\draw[dash pattern=on 20 off 3, very thick] (#2+0.25,#3-5.75) -- (#2+7.5,#3-5.75);
        \draw (#2,#3-5.75) node[left] {磁頭 #4};
        \fill[#1!10!white] (#2,#3-8.5) rectangle (#2+7.75,#3-9.0);\draw[dash pattern=on 20 off 3, very thick] (#2+0.25,#3-8.75) -- (#2+7.55,#3-8.75);
        \draw (#2,#3-8.75) node[left] {磁頭 #4};
    }
    \sectorline[blue](10,9,1);
    \sectorline[cyan](10,8.5,2);
    \sectorline[green](10,8,3);
    \sectorline[yellow](10,7.5,4);
    \sectorline[orange](10,7,5);
    \sectorline[red](10,6.5,6);

    \draw [decorate,decoration={brace,amplitude=5}] (18,12.25) -- (18, 9.5) node [black,right,midway,xshift=5] {柱面 1};
    \draw [decorate,decoration={brace,amplitude=5}] (18, 9.25) -- (18, 6.5) node [black,right,midway,xshift=5] {柱面 2};
    \draw [decorate,decoration={brace,amplitude=5}] (18, 6.25) -- (18, 3.5) node [black,right,midway,xshift=5] {柱面 3};
    \draw [decorate,decoration={brace,amplitude=5}] (18, 3.25) -- (18, 0.5) node [black,right,midway,xshift=5] {柱面 4};
    \draw [decorate,decoration={brace,amplitude=5}] (18, 0.25) -- (18,-2.5) node [black,right,midway,xshift=5] {柱面 5};

    \draw[->, thick] (12, 13) node [left] {扇區} -> (16,13);