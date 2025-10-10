


import time
import random

def crawl(url: str):
  start = time.time()
  print(f'Crawling {url}...')
  time.sleep(random.randint(1,5))
  end = time.time(
  )
  print(f'Crawling {url} done, time: {end - start} seconds')

if __name__ == '__main__':
  import threading
  print('Start crawing...')
  urls = ['http://www.baidu.com', 'http://www.qq.com', 'https://fastclass.cn']
  start = time.time()
  threads = []
  for url in urls:
    t = threading.Thread(target=crawl,args=(url,))
    threads.append(t)
    t.start()
  for t in threads:
    t.join()
  end = time.time()
  print(f'All crawling done, time: {end - start} seconds')
