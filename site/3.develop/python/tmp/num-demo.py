def check_value(x):
  if x < 0:
    raise ValueError("值不能为负数")

try:
  check_value(-5)
except ValueError:
  print("捕获到值错误,重新引发...")
  raise
