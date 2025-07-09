import os
import time
import random
from multiprocessing import Process, Queue
# Python 代码的目的是使用 multiprocessing 模块中的 Queue 实现进程间通信，一个写进程向队列写数据，另一个读进程从队列读数据（Queue 和 Pipe 都是进程安全的（Queue 的底层也是通过 Pipe 来实现的，所以性能比 Pipe 差），可以在多个进程之间共享数据，但是 Queue 多个进程可以共享的，而 Pipe 是两个进程之间共享的）

def write(q):
  print(f'Process {os.getpid()} is writing to queue')
  for value in ['A','B','C']:
    print(f'Put {value} to queue')
    q.put(value)
    time.sleep(random.random())

def read(q):
  print(f'Process {os.getpid()} is reading from queue')
  while True:
    value = q.get(True)
    print(f'Get {value} from queue...')

if __name__ == '__main__':
  q = Queue() # 创建一个队列
  pw = Process(target=write, args=(q,)) # 创建写进程
  pr = Process(target=read, args=(q,)) # 创建读进程
  pw.start()
  pr.start()
  pw.join()
  pr.terminate() # 强制终止进程
  print('All data have been written and read.')
