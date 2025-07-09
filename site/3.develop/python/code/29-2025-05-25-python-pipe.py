from multiprocessing import Process, Pipe
import os
import time
import random

def write(conn):
  print(f'Process {os.getpid()} is writing to pipe ')
  for value in ['A','B','C']:
    print(f'Put {value} to pipe...')
    conn.send(value) # 把数据放入管道
    time.sleep(random.randon()) # 随机休眠

def read(conn):
  print(f'Process {os.getpid()} is reading from pipe')
  while True:
    value = conn.recv()
    print(f'Get {value} from pipe...')

if __name__ == '__main__':
  parent_conn, child_conn = Pipe() # 创建一个管道
  pw = Process(target=write, args=(child_conn,))
  pr = Process(target=write, args=(child_conn,))
  pw.start()
  pr.start()
  pw.join()
  pr.terminate()
  print('All data have been written and read')
