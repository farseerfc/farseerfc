写程序让CPU占用率保持正弦函数
==========================================

:slug: sine-cpu
:lang: zhs
:date: 2008-06-02 23:27
:tags: java, microsoft

导入自
`renren <http://blog.renren.com/blog/230263946/298871889>`_

据说是一道微软的面试题。如题，写程序，让Windows的任务管理器中的性能监视器呈现正弦曲线。

.. image:: http://fm531.img.xiaonei.com/pic001/20080602/23/14/large_10019p67.jpg
   :align: center
   :alt: 正弦曲线

.. image:: http://fm541.img.xiaonei.com/pic001/20080602/23/14/large_9935o67.jpg
   :align: center
   :alt: 正弦曲线


潜心钻研良久，得代码：（java）

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


多核CPU上测试时要注意关掉一个CPU：



.. image:: http://fm411.img.xiaonei.com/pic001/20080602/23/14/large_9946k67.jpg
   :align: center
   :alt: 多核CPU上测试
