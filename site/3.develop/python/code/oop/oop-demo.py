# 定义类
class Stduent():
  def __init__(self, name, age, sex, id_card, score) -> None:
    self.name = name
    self.age = age
    self.sex = sex
    self.id_card = id_card
    self.score = score

  def print_score(self):
    print(f"{self.name} : {self.age} : {self.sex} : {self.id_card}: {self.score}")

# 实例化
'''
zhangsan = Stduent('zhangsan',18, 'man', 123456, 88)
lili = Stduent('li',20, 'woman', 22222, 100)
'''


# 访问对象的属性和方法
'''
zhangsan.print_score()
lili.print_score()
'''



# 定义类（狗的类）
class Dog():
  def __init__(self, name, age ) -> None:
    self.name = name
    self.age = age
    # __开头的属性是私有属性，只有在类的内部可以使用
    self.__color = 'black' # 设置私有属性

  # 如果希望外部访问私有属性，就需要定义获取私有属性的方法
  def get_color(self):
    return self.__color

  def set_color(self, color):
    if color not in ['black','white']:
      print('color must be black or white')
      raise ValueError('color must be black or white')
    self.__color = color

  def sit(self):
    print(self.name.title() + "is now sitting")

  def bark(self):
    print(f"{self.name.title()} is barking. it's {self.age} years old, color is {self.__color}")

# 创建一个对象
my_dog = Dog('Tom', 3)


# 访问对象的属性和方法
print(my_dog.name)
print(my_dog.age)
# my_dog.sit()
my_dog.bark()

# 访问私有属性
print(f'默认的颜色: {my_dog.get_color()}')

# 通过外部设置私有属性
my_dog.set_color('white')
print(f'修改之后的颜色: {my_dog.get_color()}')