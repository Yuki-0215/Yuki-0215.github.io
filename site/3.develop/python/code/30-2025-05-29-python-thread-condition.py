import random
import time
import threading

# threading 模块 Condition 类

class Account:
  def __init__(self, balance):
    self.balance = balance # 账户余额
    self.lock = threading.RLock() # 创建一个锁对象
    self.condition = threading.Condition(self.lock) # 创建一个条件对象

  def withdraw(self, amount): # 取钱
    with self.condition: # 使用 with 语句获取和释放锁
      while self.balance < amount:
        self.condition.wait() # 等待条件变量
      new_balance = self.balance - amount
      time.sleep(random.random()) # 模拟存钱耗时
      self.balance = new_balance
      print(f'Withdraw {amount} from account, balance:{self.balance}, current thread: {threading.current_thread().name}')


  def deposit(self, amount): # 存钱
    with self.condition: # 使用 with 语句获取和释放锁
      new_balance = self.balance + amount
      time.sleep(random.random()) # 模拟存钱耗时
      self.balance = new_balance
      self.condition.notify_all()
      print(f'Deposit {amount} from account, balance:{self.balance}, current thread: {threading.current_thread().name}')

if __name__ == '__main__':
  account = Account(1000)
  threads = []
  # 创建 5 个线程,每个线程取 300 元
  for i in range(5):
    t = threading.Thread(target=account.withdraw, args=(300,))
    threads.append(t)
    t.start()
  # 创建 5 个线程,每个线程取 200 元
  for i in range(5):
    t = threading.Thread(target=account.deposit, args=(200,))
    threads.append(t)
    t.start()
  for t in threads:
    t.join()
  print(f'Final balance: {account.balance}')

