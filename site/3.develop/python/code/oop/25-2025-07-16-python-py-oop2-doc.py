class Animal():
  def __init__(self,name,age) -> None:
    self.name = name
    self.age = age

  def speak(self):
    print(f"{self.name} says something")

class Dog(Animal):
  def speak(self):
    print(f"Dog: {self.name} is woof! {self.name} is {self.age} year old!")

  def run(self):
    print(f"{self.name} is running!")

class Cat(Animal):
  def speak(self):
    print(f"Cat: {self.name} is Meow! {self.name} is {self.age} year old!")

def animal_speak(animal: Animal):
  animal.speak()

dog = Dog('Tom',1)
cat = Cat('lili',2)

animal_speak(dog)
animal_speak(cat)

print(isinstance(dog, Dog))
print(isinstance(cat, Cat))
print(isinstance(dog, Animal))
print(isinstance(cat, Animal))
