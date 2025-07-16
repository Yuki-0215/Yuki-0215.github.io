class Student(object):
  def __init__(self, name, score) -> None:
    self.name = name
    self.score = score

  def print_score(self):
    print(f"{self.name}: {self.score}")

# james = Student('Tom', 99)
# Yuki = Student('Yuki', 100)

# james.print_score()
# Yuki.print_score()

class Dog():
  def __init__(self,name, age):
    self.name = name
    self.age = age
    self.__color = 'white'

  def bark(self):
    print(f"{self.name} says woof! I'm {self.age} years old")

  def get_color(self):
    return self.__color

  def set_color(self, color):
    if color not in ['red', 'blue','yellow']:
      raise ValueError('Invalid color')
    self.__color = color

# my_dog = Dog('Tom', 3)
# print(my_dog.__color)
# my_dog.__color = 'black'

my_dog = Dog('Tom', 3)
print(my_dog.get_color())
my_dog.set_color('black')
print(my_dog.get_color())
