PyRuby
======

:slug: mix-ruby
:lang: zh
:date: 2012-03-02 23:09
:tags: python, ruby
:issueid: 42

今天在GitHub上閒逛的時候看到一個叫做 `PyRuby <https://github.com/danielfm/pyruby>`_ 的項目。項目的Readme說得很好：

::

    PyRuby - Some Ruby for your Python!
    PyRuby is a simple way to leverage the power of Ruby to make your Python code more readable and beautiful.
    
    Usage
    All you have to do is import the ruby module:
    
    import ruby
    From now on you should be able to write Ruby code within a regular Python module. An example:
    
    1.upto(10) { |n| puts n }

甚至 `PyPI <http://pypi.python.org/pypi/pyruby/1.0.0>`_ 上還有這個項目的包。

一開始我還以爲這又是一個野心勃勃的基於PyPy的Ruby實現，或者某種trick在Python裏面直接調用Ruby解釋器。

然後我想看看這個的源代碼
++++++++++++++++++++++++++++++++++++

只有一個ruby.py文件，內容是：

.. code-block:: python
    
    # -*- coding: utf-8 -*-
    
    print("""
                                                                                                        
                                  `.-:/+ossyhhddmmmmNNNNNNNmmmmmdddddhhhyyyyhhhyo:`                     
                           .:+sydNNNmmdhhysso++/+++++++////::::::-.```......--/oymms.                   
                      `:ohmdys+//::/::--::::////:-.```......`````.://:-`         `/dNs.                 
                   .+hNds:`-:-:///::------::///++///:--....--::///::-`.///.        `oMm/                
                 /hNmo.`   ``    `....```````````      ...------:::-:/+/-.:/:`       /NMs               
                oMd/`      `::::--.---://+`           //`     `````-:::::+/-`::.`     :NM+              
                yN`       -+.`         `/`           o.               ``::.-:. ``      :NN:             
               :Nm        -             ./           :    `.-://///:-.   `-` ``         :NN-            
              /NM/           .-:::-.`   `/            `:sdmdhyMMMMMMNNmy/`               :mNo`          
            :hMd:          /dmddddNNmdy+-.          `smmy/-```hMMMMMMMhydm/ `-.``     `...:mMm+.        
          -hNd/-/o/-..-::`.ydmmmmNMMMMMMNh:/+-      dMN-`-+hmmmmdhhhhdddmMN-`-/o:    .-::::/oydms-      
         oNMo:+/::.         ``...--:/+ohNMNhs-      :hNmmdyo:..``yo-```.--. `-`-+shdddhs+-` `.//yms.    
        .MMo:/`o:.:+sso+:-`             sM+           ./-`       /mNh+-....-/ymNNdo::--/shd+`  -`:mm:   
        /MM-o ./ ohhsooohNmy::sh.      `yM/                       `:oyyyyyyhys+:.` hy    `/Nh`  : -NN.  
        -MM// -: ``   y: odddhh+     -omNh-          `--.` ``          ````    .:ohMMs.    +Ms  /  yMo  
         hMoo .+.    :Mh  ````    `/hNd/.`           ohdddy::...`..`      `-/sdmdyo+NMNh+- :Mh  /  sMs  
         .mmh:..:.  :NMm       `-/dMNM+         ./+++/:`.hM:`.````.` `-/shmNmh+-`  /Mmooso.hM/ .: `mM/  
          .mNs://: .NMNMs-   -:-.`/+-sms.   `  `shyyyhy`sNd`   `.:+sdmmmdMM-.    .oNM+    :m/ `s``yMh   
           -mMo  . sMNdMNNh+-.        .ydyoyy`        ``+o::+shdddhs+:-.:MM.`.-+hNMMh-    `.`-/::dNs`   
            -NM-   mMMMh:MMdNmhs+:-..```-ohs-`...-:/+syhddmMMs:-.`    `/mMMdmmddNMm+`      ..-/hNh-     
             sMy   NMMM`:Mh`-/mMmmmdddddddddhhhdNNdhyo+:--.yMs  `..:+ymMMMMd+--yNh.        `+hNh:       
             -Mm   NMMM/yMh  -NM-`..--:NMo:--.`+My         :MNoydmNMMNmhdMh` -dNs`        `yMd:         
             `MN   mMMMMMMMyshMN+:---.-MN-.....+My...-:/oyhdMMMMNmdy+-` +Mh:sNm/          yMy`          
              MN   yMMMMMMMMMMMMMMMMMNMMMMNNNNNMMMNNNMMMMMNmhMM/-.      `yMMNs.          /My            
             `MN   :MMmMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmdy+:-``NM-      ./hNNy-           /Nd`            
             -Mh    dMydMmsNMNdNNMMmmmNMMMdddhys+yMo``       /Nm:  `:yNNdo.           .sNd.             
             +Ms    .mMsMN::NN:.:MN: `.+NM.      +Mo          +Mm+ymNdo-            .omm+`              
             yM:     .hNMd+:sMN. oMm.   oMo      +Mh   ```.:+shMNmy+-``.-:-..-//-`:yNmo`                
             mM.       :ohmNNMMdhyMMdo//+Mm//////sMNhyhhdmNNmhs/-``./+/:--+so/-:smNy/`                  
            .Mm        ``  .-:/+osyyhhddddddddddhhyysoo+/:-.  `./+//--+oo/--+ymmy/.                     
            :Mh   .:   `+:`        `.------------`      ```-////:/++/:../ydNdo:`                        
            +Ms   `/`    :+o+:-```              ``..-::///++///:-.`-+ydNdo:`                            
            oMs     :/:.``  `..---.``` ````````..-:/:::---.`  `-ohmmh+:`                                
            /Mh       .://///:::-----.-----.......`       `-+hmmy+-                                     
             sMy`                                ``````-+ydmy+-                                         
              /mNs-`                        `./ohmNMNNNmy+-                                             
                /yNmho/:.``````````.-:/+syhdNmdyso+/-.`                                                 
                  `:+ydmNMNNNNNNNNNmdhys+/:.`                                                           
                         ``.....`                                                                       
                                                                                                        
        LOL U MAD?
    """)
    
    import sys
    sys.exit(1)
    
    
是的……的確……這種嘗試把Python和Ruby放在一起的想法絕對是瘋了……

