# 场景
# ORM： 对象关系映射，把数据库中的表映射成类，表中的字段映射成类的属性

'''
元类是类的类，类是对象的模版，元类是类的模版，元类是用来创建类的，就像类是用来创建对象的一样。
在python中，一切皆对象，那么类也是对象，正如你用类来创建对象一样，也可以使用元类创建类。
'''

# type() 函数
'''
我们知道Python中，一切皆对象，同样的道理，那么类也是对象，既然是对象，那么是什么类型呢？type 函数不就可以返回一个对象的类型吗？那么我们来看看类的类型是什么:
'''

class Student:
  pass

# print(type(Student)) # <class 'type'> 元类 metaclass

'''
从上面输入结果可以看出，类的类型是type，这就是元类，元类是用来创建类的类，type 函数既可以返回一个对象的类型，也可以创建新的类型，也就是我们无需用过class 关键字就可以定义类了，比如我们想要创建出Student 类，可以通过type 函数来创建
'''

# 如果类中包含方法，我们可以先定义该函数

def print_hello(self):
  print(f'Hello, {self.name}!')

# 使用type() 创建类

# Student = type('Student',(object,), dict(name='James', hello=print_hello))
# 使用lamdba 表达式
# Student = type('Student',(object,),{'name': 'James','hello': lambda self: print(f'Hello, {self.name}!') })


'''
s = Student() # 实例化
s.hello()

print(type(Student))
'''


# metaclass (类的模版)
# metaclass -> class -> object

# 定义一个元类，继承type
class Meta(type):
  """
  cls: 当前创建的类的对象
  name: 类的名字
  bases: 类继承的父类
  dct: 类的方法和属性的字典
  """
  def __new__(cls, name, bases, dct):
    print('Meta.__new__')
    # 在创建类的时候自动添加一个 hello方法和 name 属性
    dct['hello'] = lambda self: print(f'Hello, {self.name}!')
    dct['name'] = 'James'
    return super().__new__(cls, name, bases, dct)

  def __len__(self):
    return 100

class MyClass(metaclass=Meta):
  pass

m = MyClass()
print(m.name)
m.hello()
print(len(MyClass))

