import time
import random
from concurrent.futures import ThreadPoolExecutor

def crawl(url):
  print(f'Start crawling {url}')
  start = time.time()
  time.sleep(random.randint(1, 5)) # 模拟爬取网页的时间
  end = time.time()
  print(f"Finish crawling {url}, time: {end - start}s")


# 线程池
'''
if __name__ == '__main__':
  print('Start crawling...')
  urls = ['http://www.baidu.com', 'http://www.qq.com', 'https://fastclass.cn']
  start = time.time()
  with ThreadPoolExecutor() as executor:
    executor.map(crawl, urls)
  end = time.time()
  print(f'All crawling done, time: {end - start} seconds')
'''


# 上面代码中我们使用ThreadPoolExecutor类 创建了一个线程池,注意这里我们使用 with 语句,这样可以自动关闭线程池,然后调用map() 方法执行多任务.map() 方法会自动分配任务给线程池中的线程,然后等待所有任务执行完毕

# 执行结果
'''
$ python 30-2025-05-29-python-thread-concurrent.py
Start crawling...
Start crawling http://www.baidu.com
Start crawling http://www.qq.com
Start crawling https://fastclass.cn
Finish crawling http://www.baidu.com, time: 1.0043399333953857s
Finish crawling https://fastclass.cn, time: 3.9982779026031494s
Finish crawling http://www.qq.com, time: 3.9983737468719482s
All crawling done, time: 3.9989569187164307 seconds
'''

# 需要注意: ThreadPoolExecutor 类实例化的时候包含了一个参数 max_workers, 表示线程池中最多可以创建的线程数量,如果不指定就是默认值. 默认值: min(32, (os.cpu_count() or 1) + 4) ,也就是最多创建32 个线程或者 cpu 核数+4 个线程.
# 比如这里如果指定最多创建 2 个线程,将ThreadPoolExecutor() 改成ThreadPoolExecutor(max_workers=2), 那么执行任务的最大线程数就是2 个,执行结果如下

'''
if __name__ == '__main__':
  print('Start crawling...')
  urls = ['http://www.baidu.com', 'http://www.qq.com', 'https://fastclass.cn']
  start = time.time()
  with ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(crawl, urls)
  end = time.time()
  print(f'All crawling done, time: {end - start} seconds')
'''


# 执行结果
'''
$ python 30-2025-05-29-python-thread-concurrent.py                                                                                                                                                                                         (dev/cert-manager)
Start crawling...
Start crawling http://www.baidu.com
Start crawling http://www.qq.com
Finish crawling http://www.qq.com, time: 2.0050690174102783s
Start crawling https://fastclass.cn
Finish crawling http://www.baidu.com, time: 4.005120038986206s
Finish crawling https://fastclass.cn, time: 2.0028698444366455s
All crawling done, time: 4.008568048477173 seconds
'''
# 从上面输出可以看到，最多只有 2 个线程在执行任务，其他任务需要等待。当然除了使用 map 方法外，我们还可以使用 submit 方法来提交任务，submit 方法会返回一个 Future 对象，可以用来获取任务的执行结果，比如下面的例子：

if __name__ == '__main__':
  print('Start crawling...')
  urls = ['http://www.baidu.com', 'http://www.qq.com', 'https://fastclass.cn']
  start = time.time()
  with ThreadPoolExecutor() as executor:
    futures = [executor.submit(crawl, url) for url in urls]
    for future in futures:
      print(future.result()) # 获取任务的执行结果
  end = time.time()
  print(f'All crawling done, time: {end - start} seconds')
