Write a program to keep CPU usage as sin funcion
================================================

:slug: sine-cpu
:lang: en
:date: 2008-06-02 23:27
:tags: java, microsoft
:issueid: 30

Imported from:
`renren <http://blog.renren.com/blog/230263946/298871889>`_.

It is said that this is a problem from interview of Microsoft. Write a program, which makes the CPU usage curve in Windows Task Manager shows a Sin function.

.. image:: http://fm531.img.xiaonei.com/pic001/20080602/23/14/large_10019p67.jpg
   :align: center
   :alt: Sine function 1


.. image:: http://fm541.img.xiaonei.com/pic001/20080602/23/14/large_9935o67.jpg
   :align: center
   :alt: Sine function 2


The program below is written in java:

.. code-block:: java

    public class sincpu {
        private static final int cycle=1024,tick = 256;
        public static void main (String[] args) throws InterruptedException {
            for(int i = 0;;i++){
                work(calcNextSleep(i % cycle));
                sleep(tick - calcNextSleep(i % cycle));
            }
        }
        
        private static long calcNextSleep(long i){
            return (int)(Math.sin((double)i * 2 * Math.PI / cycle) * tick + tick) / 2;
        }
        
        private static void sleep (long sleepTime) throws InterruptedException
        {
            if(sleepTime < 2)
                Thread.yield();
            else
                Thread.sleep(sleepTime);
        }
        
        private static void work (long period) {
            long start = System.currentTimeMillis();
            for(;;){
                Math.sin(1);
                if(System.currentTimeMillis() - start >= period)
                    break;
            }
        }
    }

Be careful you need to turn off other cores if you have multi-core CPU.


.. image:: http://fm411.img.xiaonei.com/pic001/20080602/23/14/large_9946k67.jpg
   :align: center
   :alt: multi-core CPU
