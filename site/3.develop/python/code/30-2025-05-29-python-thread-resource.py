import random
import time
import threading

class Account:
  def __init__(self, balance):
    self.balance = balance # 账户余额
    self.lock = threading.RLock() # 创建一个可重入锁
    self.condition = threading.Condition(self.lock) # 创建一个条件变量

  '''手动获取和释放锁
    def witdraw(self, amount):
      # 获取锁
      self.lock.acquire()
      try:
        new_balance = self.balance - amount
        time.sleep(random.random())
        self.balance = new_balance
      finally:
        # 释放锁
        self.lock.release()
    def witdraw(self, amount):
      with self.lock: # 使用 with 语句自动获取和释放锁
        new_balance = self.balance - amount
        time.sleep(random.random())
        self.balance = new_balance

  '''
  def withdraw(self, amount):
    with self.condition: # 使用 with 语句自动获取和释放锁
      while self.balance < amount:
        self.condition.wait() # 等待条件变量
      new_balance = self.balance - amount
      time.sleep(random.random()) # 模拟提现的时间
      self.balance = new_balance
      print(f'Withdraw {amount} from account, balance: {self.balance}')


  def deposit(self, amount):
    self.lock.acquire()
    try:
      new_balance = self.balance + amount
      time.sleep(random.random())
      self.balance = new_balance
    finally:
      # 释放锁
      self.lock.release()

if __name__ == '__main__':
  account = Account(1000) # 创建一个账户,初始余额 1000
  therads = []
  # 创建 5 个线程,每个线程取钱 200 元
  for i in range(5):
    t = threading.Thread(target=account.witdraw, args=(200,))
    therads.append(t)
    t.start()
  for t in therads:
    t.join() # 所有线程执行完毕之后,期望输出账户余额
  print(f'Account balance: {account.balance}')
