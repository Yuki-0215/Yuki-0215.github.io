class Student():
  @property
  def score(self):
    return self._score

  @score.setter
  def score(self, value):
    if not isinstance(value, int):
      raise ValueError('score must be an integer!')

    if value < 0 or value > 100:
      raise ValueError('score must between 0-100!')
    self._score = value

  @property
  def birth(self):
    return self._birth

  @birth.setter
  def birth(self, value):
    self._birth = value

  @property
  def age(self):
    return self._age

s = Student()
s.score = 22
print(s.score)

s.birth = 111
print(s.birth)

s.age = 12 
print(s.age)
