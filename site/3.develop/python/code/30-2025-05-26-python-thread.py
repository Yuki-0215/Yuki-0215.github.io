# 多线程是一种轻量级的进程,线程是操作系统能够进行运算的最小单位,他被包含在进程之后,一个进程可以拥有多个线程,这些线程在共享内存的情况下互相独立.
# 每个线程都有自己的一组寄存器,堆栈和局部变量,线程之间的切换和调度不会引起进程的切换,只是线程的切换,这样就可以实现多个线程并发执行
# 在 Python 中,要实现多线程,我们可以使用 threading 模块,这个模块提供了 Thread 类来表示一个线程对象,然后通过 start()方法启动一个线程,通过 join()方法等待线程执行完毕

## 创建线程
import time
import random
import threading
from concurrent.futures import ThreadPoolExecutor

def crawl(url):
  print(f'Start crawling {url}')
  start = time.time()
  time.sleep(random.randint(1, 5)) # 模拟爬取网页的时间
  end = time.time()
  print(f"Finish crawling {url}, time: {end - start}s")

class CrawlThread(threading.Thread):
  def __init__(self, url):
    super().__init__()
    self.url = url

  def run(self): # 重写 run 方法,run 方法是线程的入口
    crawl(self.url)










# 继承 Thread 类并重写 run() 方法的方式来自定义线程,比如我们可以这样来实现,如下所示:
'''
if __name__ == '__main__':
  print('Start crawling...')
  urls = ['http://www.baidu.com', 'http://www.qq.com', 'https://fastclass.cn']
  start = time.time()
  threads = []
  for url in urls:
    t = CrawlThread(url) # 创建自定义线程对象
    threads.append(t)
    t.start() # 启动线程,会自动调用 run 方法
  for t in threads:
    t.join() # 等待线程执行完毕
  end = time.time()
  print(f'All crawling done, time: {end - start} seconds')
'''




# 不使用多线程,我们可以这样来执行:
'''
if __name__ == '__main__':
  print('Start crawling...')
  urls = ['http://www.baidu.com', 'http://www.qq.com', 'https://fastclass.cn']
  start = time.time()
  for url in urls:
    crawl(url)
  end = time.time()
  print(f'All crawling done, time: {end - start} seconds')
'''

'''
$ python 30-2025-05-26-python-thread.py                                                                                                                                                                                                         (dev/cert-manager)
Start crawling...
Start crawling http://www.baidu.com
Finish crawling http://www.baidu.com, time: 3.002347230911255s
Start crawling http://www.qq.com
Finish crawling http://www.qq.com, time: 2.005033254623413s
Start crawling https://fastclass.cn
Finish crawling https://fastclass.cn, time: 4.000101089477539s
All crawling done, time: 9.007641077041626 seconds
'''
# 从输出可以看到,三个网页都是顺序爬取的,一共使用了 9s

# 如果我们使用多线程的话,就可以同时爬取多个网页了,这样就可以大大提高程序的执行效率,减少总共耗时,实现如下:

'''
if __name__ == '__main__':
  import threading
  print('Start crawling...')
  urls = ['http://www.baidu.com', 'http://www.qq.com', 'https://fastclass.cn']
  start = time.time()
  threads = []
  for url in urls:
    t = threading.Thread(target=crawl, args=(url,))
    threads.append(t)
    t.start() # 启动线程
  for t in threads:
    t.join() # 等待线程执行完毕
  end = time.time()
  print(f'All crawling done,time: {end - start} seconds')
'''

# 上面代码中我们通过 Thread 类创建了 3 个线程对象,然后调用 start() 方法启动线程,最后调用 join() 方法等待线程执行完毕.执行结果

'''
$ python 30-2025-05-26-python-thread.py
Start crawling...
Start crawling http://www.baidu.com
Start crawling http://www.qq.com
Start crawling https://fastclass.cn
Finish crawling https://fastclass.cn, time: 1.0044221878051758s
Finish crawling http://www.baidu.com, time: 3.005406141281128s
Finish crawling http://www.qq.com, time: 4.005501985549927s
All crawling done,time: 4.006248950958252 seconds
'''
# 从输出结果可以看到,三个网页是同时爬取的,不需要等待一个网页爬取完毕后才能下一个网页,总耗时 4 秒左右,几乎等于耗时最长的一个任务的执行时间,大大提高了程序的执行效率

