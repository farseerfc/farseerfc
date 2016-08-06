寫程序讓CPU佔用率保持正弦函數
==========================================

:slug: sine-cpu
:lang: zh
:date: 2008-06-02 23:27
:tags: java, microsoft
:issueid: 30

導入自
`renren <http://blog.renren.com/blog/230263946/298871889>`_

據說是一道微軟的面試題。如題，寫程序，讓Windows的任務管理器中的性能監視器呈現正弦曲線。

.. image:: http://fm531.img.xiaonei.com/pic001/20080602/23/14/large_10019p67.jpg
   :align: center
   :alt: 正弦曲線

.. image:: http://fm541.img.xiaonei.com/pic001/20080602/23/14/large_9935o67.jpg
   :align: center
   :alt: 正弦曲線

.. PELICAN_END_SUMMARY


潛心鑽研良久，得代碼：（java）

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


多核CPU上測試時要注意關掉一個CPU：



.. image:: http://fm411.img.xiaonei.com/pic001/20080602/23/14/large_9946k67.jpg
   :align: center
   :alt: 多核CPU上測試
