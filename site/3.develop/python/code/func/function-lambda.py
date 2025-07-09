# 高阶函数
# 接受函数作为输入或者返回函数的函数叫做高阶函数,它是函数式编程的重要组成部分,假设我们相对一个项目列表执行迭代,并将其顺序打印出来,我们可以轻松构建一个如下所示的函数

list_of_items = [1,2,3,4,5,6]

def iterate(list_of_items):
  for item in list_of_items:
    print(item)

# 函数调用
# iterate(list_of_items)

# 将函数作为参数传入函数
def iterarte_custon(list_of_items, custom_func): # custom_func 是一个函数,将函数作为参数传入
  for item in list_of_items:
    custom_func(item)

# 上面iterarte_custon 就是一个高阶函数,我们将custom_func 函数作为参数传入iterarte_custon,这样看起来很简单,但其实功能非常强大.

# 函数可以被返回

def add(x, y):
  return x + y

def sub(x, y):
  return x - y

def mult(x, y):
  return x * y

def div(x,y):
  return x / y

def calculator(opcode):
  if opcode == '+':
    return add
  elif opcode == '-':
    return sub
  elif opcode == '*':
    return mult
  else:
    return div

'''
my_calc = calculator('+')
print(my_calc(5, 4))
'''

# 匿名函数(lambda)
# 匿名函数是一种间接的函数定义方式,使用 lambda 关键字,不需要使用 def 定义函数名,lambda 函数语法定义如下:
# lambda

# 普通函数
def add(x, y):
  return x + y

# 匿名函数
add_lambda = lambda x, y: x + y
'''
print(add_lambda(3, 5))
'''


# 常见高阶函数
# python 内置了很多高阶函数,比如 map,filter 和 reduce等,他们可以帮组我们更方便地处理数据,下面我们来看几个常见的高阶函数用法

# max()/min() 除了按照元素本身比较外,还支持用户 key 指定一个函数,按照元素总的某项值进行比较.这个函数满足一下要求:

# - 参数是序列的一项
# - 返回一个可比较类型(如字符串,数字等)

# 获取列表最大值/最小值
data = [1, 10, 5, 7, 6]
'''
print(max(data))
print(min(data))
'''


# 获取字典列表中某个字段最大值
data = [
    {'name': '张三', 'gender': 'male', 'age': 27, 'score': 88},
    {'name': '李四', 'gender': 'female', 'age': 21, 'score': 66},
    {'name': '王五', 'gender': 'male', 'age': 24, 'score': 73},
    {'name': '赵六', 'gender': 'female', 'age': 20, 'score': 92},
    {'name': '孙七', 'gender': 'female', 'age': 22, 'score': 80},
]

# max() 支持按用户指定函数(规则)，求最大值
# print('年龄最大的', max(data, key=lambda x: x['age']))

# min() 支持按用户指定函数(规则)，求最小值
# print('分数最低的',min(data, key=lambda x: x['score']))
# max 和 min 函数可以获取列表中的最大值和最小值，但是如果这个列表不是简单的数字列表，而是一个字典列表，我们可以通过 key 参数指定一个函数，按照这个函数的返回值进行比较，通常我们会使用 lambda 表达式来指定这个函数。

# sorted()
# 和上面的 max 和 min 函数类似，sorted() 除了按元素本身比较外，还支持通过 key 指定一个函数，按元素总的某项值进行比较。这个函数满足以下要求：

data = [
    {'name': '张三', 'gender': 'male', 'age': 27, 'score': 88},
    {'name': '李四', 'gender': 'female', 'age': 21, 'score': 66},
    {'name': '王五', 'gender': 'male', 'age': 24, 'score': 73},
    {'name': '赵六', 'gender': 'female', 'age': 20, 'score': 92},
    {'name': '孙七', 'gender': 'female', 'age': 22, 'score': 80},
]

# sorted() 支持按用户指定函数(规则)，进行排序，还可以指定 reverse=True 进行逆序 (默认是从小到大排序,如果reverse=True就是从大到小)
# print('按分数排序', sorted(data, key=lambda x: x['score'], reverse=True))

# map 函数
# map 函数是python中的一个内置函数，它接受两个参数： 一个函数和一个迭代对象，然后将传入的函数依次作用于序列的每一个元素，并将结果作为新的迭代器返回
# map: 对列表中的每一个元素都执行一个函数，返回一个新列表
# map(function,iterable)


# 函数
def square(x):
  return x * x

# 可以迭代的列表
numbers = [1, 2, 3, 4, 5]

print(list(map(square, numbers))) # [1, 4, 9, 16, 25]

# lambda 表达式
print(list(map(lambda x: x * x, numbers)))

# filter: 对列表中的每一个元素都执行一个函数，返回一个新列表，只包含执行结果为True 的元素
# filter(function,iterable) # function(x) 返回True 或 False， True 保留，False 过滤掉

def is_even(x):
  return x % 2 == 0

print(list(filter(is_even, numbers))) # [2, 4] 能被2除进的保留，其他的过滤

# lambda 表达式
print(list(filter(lambda x: x % 2 == 0, numbers)))

# reduce： 对列表中的每个元素都执行一个函数，返回一个值
# reduce() 函数是把一个函数作用在一个序列[x1, x2, x3, ...] 上，这个函数必须接收两个参数，reduce 把结果继续喝序列的下一个元素做累计计算


# 需要注意 reduce() 函数在 Python 3 中已经被移动到 functools 模块中，需要先导入才能使用。
from functools import reduce
def add(x ,y):
  return x + y

numbers = [1, 2, 3, 4, 5]

print(reduce(add, numbers)) # 15

# lambda 表达式
print(reduce(lambda x,y: x + y, numbers))


