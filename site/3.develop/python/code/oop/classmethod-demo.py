# classmethod 方法

import settings
class Mysql():
  def __init__(self,ip,port):
      self.ip=ip
      self.port=port

  def func(self):
    print(f'{self.ip}:{self.port}')

  @classmethod # 将下面的函数装饰绑定给类的方法
  def from_conf(xxx):
    print(xxx)
    return xxx(settings.IP, settings.PORT)


'''
obj = Mysql('192.168.0.1',3306)
print(obj.func())
'''

'''
obj2 = Mysql(settings.IP,settings.PORT)
obj2.func()
'''

obj = Mysql.from_conf()
print(obj.__dict__)
