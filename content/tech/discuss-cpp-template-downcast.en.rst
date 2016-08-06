Discuss C++ Template Downcast
=============================

:slug: discuss-cpp-template-downcast
:lang: en
:date: 2012-02-26 05:54:57
:tags: template, C
:series: YSSY_C
:issueid: 36

.. contents::

This is a discuss in C board in bbs.sjtu.edu.cn, about type down-cast in C++ template.

Original Discuss
++++++++++++++++

http://bbs.sjtu.edu.cn/bbstcon,board,C,reid,1330078933,file,M.1330078933.A.html

The problem
+++++++++++

Today I read a book about we can do cast-down in template, so I write this to test:

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

It is strange when :code:`f` it don't allow my specified :code:`f<A>``.

But in :code:`ff` it allowed :code:`ff<BB<long>>``.

Tested under VC10 and GCC3.4

My answer to the problem
++++++++++++++++++++++++

Let's think ourself as compiler to see what happened there.

Define mark :code:`#` : :code:`A#B` is the instantiated result when we put :code:`B` into the parameter :code:`T` of :code:`A<T>` .

First we discuss ff
*******************

.. code-block:: c++

    DD<long> dd;

After this sentense, the compiler saw the instantiation of :code:`DD<long>` , so it instantiate :code:`DD#long` , and also :code:`BB#long` .

.. code-block:: c++

    ff(dd);

This sentense required the compiler to calculate set of overloading functions.

Step 1 we need to infer :code:`T` of :code:`ff<T>` from argument :code:`DD#long -> BB<T>` . Based on the inference rule:

::

    Argument with type :code:`class_template_name<T>` can be use to infer :code:`T``.

So compiler inferred :code:`T` as :code:`long` . Here if it is not :code:`BB` but :code:`CC` which is complete un-related, we can also infer, as long as :code:`CC` is a template like :code:`CC<T>` .

Step 2 Template Specialization Resolution. There is only one template here so we matched :code:`ff<T>` .

Step 3 Template Instantiation

After inferred :code:`long -> T` , compiler instantiated :code:`ff#long` .

Set of available overloading functions : :code:`{ff#long}` 

Then overloading resolution found the only match :code:`ff#long``, checked its real parameter :code:`DD#long` can be down-cast to formal parameter :code:`BB#long` .

Then we discuss f
*****************

.. code-block:: c++

    f(b);

Calculate set of overloading functions.

Step 1 infer all template parameters for template :code:`f` . According to inference rule:

::

    Parameter with type T can be used to infer T 。

So :code:`B -> T` is inferred.

Step 2 Template Specialization Resolution.

Here :code:`B` is not :code:`A` so we can not apply specialization of :code:`f<A>` , remaining :code:`f<T>` as the only alternative.

Step 3 Template Instantiation.

When we put :code:`B` into :code:`f<T>` to instantiate as :code:`f#B` , we need to instantiate :code:`traits#B``. 

There is no specialization for :code:`B` so we use template :code:`traits<T>` , :code:`traits#B::value=false` , so :code:`enable_if#false` didn't contains a :code:`type` , an error occurred.

The only template is mismatch, available overloading functions is empty set. So we got an error.

