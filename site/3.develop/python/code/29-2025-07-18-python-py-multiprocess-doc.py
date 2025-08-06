import os
import time

def long_time_task(name):
  print(f'Run task {name}: {os.getpid()}')
  start = time.time()
  time.sleep(2)
  end = time.time()
  print(f'Task {name} runs {end - start} seconds')

if __name__ == '__main__':
  from multiprocessing import Process
  print(f'Parent process {os.getpid()}')
  start = time.time()
  p1 = Process(target=long_time_task, args=('A',))
  p2 = Process(target=long_time_task, args=('B',))
  print('Waiting for all subprocesses done ...')
  p1.start()
  p2.start()
  p1.join()
  p2.join()
  end = time.time()
  print(f'All subprocesses done . time is: {end - start}')

# 不使用多进程
# if __name__ == '__main__':
#   print(f'Parent process {os.getpid()}')
#   start = time.time()
#   long_time_task('A') # 顺序执行
#   long_time_task('B') # 顺序执行
#   end = time.time()
#   print(f'All runs {end - start} seconds')
