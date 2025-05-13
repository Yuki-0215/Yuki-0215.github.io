class Animal: # object 是所有类的父类
  def __init__(self, name) -> None:
    self.name = name

  def speak(self):
    print(f"{self.name} says something")


class Flyable:
  def __init__(self, name) -> None:
    self.name = name

  def fly(self):
    print(f"{self.name} is flying")




class Dog(Animal): # Animal 就是Dog 的父类，Dog 就是Animal 的子类
  def __init__(self, name, age) -> None:
    super().__init__(name) # 调用父类的构造函数
    self.age = age

  def speak(self): # 重写父类的方法
    super().speak() # 调用父类的方法
    print(f'{self.name} is barking, age is {self.age}')

  def run(self):
    print(f"{self.name} is running!")

class Cat(Animal):
  def speak(self):
    print(f"{self.name} says Meow!")

  def jump(self):
    print(f"{self.name} is jumping")


dog = Dog('lib', 3)
'''
dog.speak()
'''


cat = Cat("Tom")
'''
cat.speak()
cat.jump()
'''



class Bird(Animal, Flyable): # 多重继承
  def __init__(self, name) -> None:
    Animal.__init__(self, name)
    Flyable.__init__(self, name)

  def speak(self):
    super().speak()
    print(f"{self.name} is chirping")

  def fly(self):
    super().fly()
    print(f"{self.name} is flying on the sky")

'''
print("===============")
bird = Bird("Polly")
bird.speak()
bird.fly()
'''



def animal_speak(animal: Animal):
  animal.speak()
  print('==============')

animal_speak(dog)
animal_speak(cat)