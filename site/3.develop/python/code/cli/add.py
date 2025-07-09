import sys

def add(a,b):
  return a + b

if len(sys.argv) != 3:
  print("用法: Python example.py num1 num2")
else:
  try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    result = add(num1 ,num2)
    print(f"结果: {result}")
  except ValueError:
    print("参数必须是数字！！！")
  finally:
    sys.exit(1)