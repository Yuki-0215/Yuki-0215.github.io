import argparse

# 创建一个解析器对象
parser = argparse.ArgumentParser(description="这是一个单间的计圈器tools")

# 添加一些参数

parser.add_argument("num1", type=float, help="第一个数字")
parser.add_argument("num2", type=float, help="第二个数字")

# 解析参数
args = parser.parse_args()

# 进行加法计算
result = args.num1 + args.num2

print(f"{args.num1} + {args.num2} = {result}")