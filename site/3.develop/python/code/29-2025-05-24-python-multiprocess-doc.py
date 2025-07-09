import os
import time

def long_time_task(name: str):
  print(f'Run task {name} ({os.getpid()})...')
  start = time.time()
  time.sleep(2) # 模拟耗时操作
  end = time.time()
  print(f'Task {name} runs {end - start} seconds.')

# 使用进程池
if __name__ == '__main__':
  from multiprocessing import Pool, cpu_count
  cpu = cpu_count()
  print(f'Parent process {os.getpid()}.')
  print(f'CPU core count: {cpu}.')
  start = time.time()
  p = Pool(cpu) # 创建进程池，最大进程数为CPU核心数
  for i in range(cpu*2): # 顺序创建多个进程
    p.apply_async(long_time_task, args=(i,)) # 异步执行任务
  print('Waiting for all subprocesses done...')
  p.close() # 关闭进程池，不再接受新的进程
  p.join() # 阻塞主进程，等待所有子进程结束
  end = time.time()
  print(f'All runs {end - start} seconds. ')


# 使用多进程(大概运行时间为2s，多进程大大提高了运行效率，但是进程不是越多越好，因为进程创建也是需要消耗资源，最好的方式就是和CPU核数相等，这样就可以充分使用CPU)
'''
if __name__ == '__main__':
  from multiprocessing import Process
  print(f'Parent process {os.getpid()}.')
  start = time.time()
  p1 = Process(target=long_time_task, args=('A',)) # 创建进程A
  p2 = Process(target=long_time_task, args=('B',)) # 创建进程B
  p1.start() # 启动进程A
  p2.start() # 启动进程B
  p1.join() # 等待进程A结束
  p2.join() # 等待进程B结束
  end = time.time()
  print(f'All runs {end - start} seconds')
'''

# 不使用多进程（说明任务A和任务B 都在一个主进程中）
'''
if __name__ == '__main__':
  print(f'Parent process {os.getpid()}.')
  start = time.time()
  long_time_task('A') # 顺序执行
  long_time_task('B') # 顺序执行
  end = time.time()
  print(f'All runs {end - start} seconds')
'''

