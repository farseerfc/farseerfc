關於C++模板的類型轉換的討論
=======================================

:slug: discuss-cpp-template-downcast
:lang: zh
:date: 2012-02-26 05:54:57
:tags: template, C
:series: 飲水思源C板
:issueid: 36

.. contents::

這兩天在飲水思源的C板，關於C++模板的類型轉換的一個討論，後面是我的解答。


討論地址
++++++++++++


http://bbs.sjtu.edu.cn/bbstcon,board,C,reid,1330078933,file,M.1330078933.A.html

原問題
+++++++++



今天在書上看到模板演繹的時候可以允許cast-down，於是我寫了個東西：

.. code-block:: c++

    template <bool _Test, class _Type = void>
    struct enable_if { };
    
    template<class _Type>
    struct enable_if<true, _Type> {
        typedef _Type type;
    };
    
    class A { };
    class B : A { };
    
    template <typename T>
    struct traits { static int const value = false; };
    
    template <>
    struct traits<A> { static int const value = true; };
    
    template <typename T>
    void f(T, typename enable_if<traits<T>::value>::type* = 0) { }
    
    template <>
    void f<A>(A, enable_if<traits<A>::value>::type*) { }
    
    
    
    template <typename T>
    class BB {};
    
    template <typename T>
    class DD : public BB<T> {};
    
    template <typename T> void ff(BB<T>) {};
    
    int main(int argc, char * argv[])
    {
        A a; B b;
        DD<long> dd;
        //f(b);
        ff(dd);
    }

奇怪的是重載決議的時候， :code:`f` 的情況下它就不讓我特化的 :code:`f<A>` 進來。

但是在 :code:`ff` 的情況下， :code:`ff<BB<long>>` 卻進來了。

在VC10和GCC3.4下測試

我的解答
++++++++++++

我們來設身處地地作爲編譯器，看一遍到底發生了什麼。

約定符號 :code:`#` : :code:`A#B` 是把 :code:`B` 帶入 :code:`A<T>` 的參數 :code:`T` 之後實例化得到的結果。

首先看ff的情況。
***********************

.. code-block:: c++

    DD<long> dd;

處理到這句的時候，編譯器看到了 :code:`DD<long>` 的實例化，於是去實例化 :code:`DD#long` ，繼而實例
化了 :code:`BB#long` 。

.. code-block:: c++

    ff(dd);

這句，首先計算重載函數集合。

第一步，需要從參數 :code:`DD#long -> BB<T>` 推斷 :code:`ff<T>` 的 :code:`T` 。根據函數模板參數推斷規則：

::

    :code:`class_template_name<T>` 類型的參數，可以用於推斷 :code:`T` 。

於是編譯器推斷 :code:`T` 爲 :code:`long` 。這裏就算不是 :code:`BB` 而是完全無關的 :code:`CC` 都可以推斷成功，只要 :code:`CC` 也
是一個 :code:`CC<T>` 形式的模板。

第二步，模板特化匹配。因爲只有一個模板，所以匹配了最泛化的 :code:`ff<T>` 。

第三步，模板實例化。

推斷了 :code:`long -> T` 之後，編譯器實例化 :code:`ff#long` 。

重載函數集合： :code:`{ff#long}` 

然後重載抉擇找到唯一的可匹配的實例 :code:`ff#long` ，檢查實際參數 :code:`DD#long` 可以隱式轉換到
形式參數 :code:`BB#long` ，從而生成了這次函數調用。

再來看f的情況。
**********************

.. code-block:: c++

    f(b);

計算候選重載函數集合。

第一步，對所有 :code:`f` 模板推斷實參。根據函數模板參數推斷規則：

::

    帶有 :code:`T` 類型的參數，可以用於推斷 :code:`T` 。

於是 :code:`B -> T` 被推斷出來了。

第二步，模板特化匹配。

這裏 :code:`B` 不是 :code:`A` ，所以不能用 :code:`f<A>` 特化，只能用 :code:`f<T>` 模板。

第三步，模板實例化。

:code:`B` 帶入 :code:`f<T>` 實例化成 :code:`f#B` 的過程中，實例化 :code:`traits#B` 。

由於沒有針對 :code:`B` 的特化，所以用 :code:`traits<T>` 模板， :code:`traits#B::value=false` ，進而 :code:`enable_if#false` 沒有 :code:`type` ，出錯。

唯一的模板匹配出錯，重載函數集合爲空，SFINAE原則不能找到合適的匹配，於是報錯。

