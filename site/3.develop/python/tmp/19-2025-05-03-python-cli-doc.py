import sys

# 打印所有命令行参数
print("所有命令行参数: " , sys.argv)

# 打印脚本名称
print("打印脚本名称: ",sys.argv[0])

# 打印第一个命令行参数
if len(sys.argv) > 1:
  print("第一个命令行参数: ", sys.argv[1])