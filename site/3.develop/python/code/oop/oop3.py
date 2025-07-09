# 创建 Animal 父类
class Animal:
  def __init__(self, name):
    self.name = name

  def speak(self):
    print(f"{self.name} is speaking ~")

class Fly:
    def fly(self):
        print(f"{self.name} is flying")

# 创建 Dog 子类
class Dog(Animal,Fly):
  def __init__(self, name, age): # 调用父类的属性
    super().__init__(name)
    self.age = age

  def speak(self):
    super().speak() # 调用父类的方法
    print(f"{self.name} says woof! it's {self.age} year old")

  def run(self):
    print(f'{self.name} is running!')

# 创建 Cat 子类
class Cat(Animal):
  def speak(self):
   print(f'{self.name} says Meow')

def animal_speak(animal: Animal):
  animal.speak()
  print('==========')

dog = Dog('jack', 12)
# dog.speak()
# dog.run()
# dog.fly()

cat = Cat('Tom')
# cat.speak()

animal_speak(dog)
animal_speak(cat)

# isinstance() 函数判断一个对象是否是一个已知的类型
print(isinstance(dog, Dog))
print(isinstance(cat, Cat))
print(isinstance(dog, Animal))
print(isinstance(cat, Animal))
