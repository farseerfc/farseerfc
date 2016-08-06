PyRuby
======

:slug: mix-ruby
:lang: jp
:date: 2012-03-02 23:09
:tags: python, ruby
:issueid: 42

きょう、Githubに `PyRuby <https://github.com/danielfm/pyruby>`_ というプロジェクトを見ました。それの説明にこう書いています: 

::

    PyRuby - Some Ruby for your Python!
    PyRuby is a simple way to leverage the power of Ruby to make your Python code more readable and beautiful.
    
    Usage
    All you have to do is import the ruby module:
    
    import ruby
    From now on you should be able to write Ruby code within a regular Python module. An example:
    
    1.upto(10) { |n| puts n }

さらに、 `PyPI <http://pypi.python.org/pypi/pyruby/1.0.0>`_ にそれのパッケージもあった。

最初に、これはもう一つのPyPyで実現したRubyだと思った。少なくとも、本当のRubyをPythonから呼び出すの何かの魔法も可能かもしれない。

それのソースコートはこうなっています。 ruby.py
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


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
    

本当だ、Pythonの中にRubyを呼び出すという考えはアホだ。

