import os

cmd_path = os.getcwd() # 输出工作路径
print(cmd_path)


with open('test.txt',mode='w',encoding='utf-8') as f:
  f.write('Hello Python!')

with open('test.txt',mode='r',encoding='utf-8') as f:
  print(f.readline())