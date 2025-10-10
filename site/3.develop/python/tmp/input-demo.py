import random

# 游戏选项
choices = ["石头", "剪刀", "布"]

# 计算结果函数
def determine_winner(player: str, computer: str):
  if player == computer:
    return "平局"

  elif (player == "石头" and computer == "剪刀") or \
    (player == "剪刀" and computer == "布") or \
      (player == "布" and computer == "石头") :
        print('人获胜')
  else:
    print('机器获胜')


# 主程序
def play_game():
  print('欢迎来到石头剪刀布游戏!')
  print("请输入 '石头', '剪刀', 或 '布'")

  # 获取用户输入
  player_choice = input('请输入你的选择: ')

  if player_choice not in choices:
    print("无效的选择,请重新输入~")
    return

  # 电脑随机选择
  computer_choice = random.choice(choices)
  print(f'电脑的选择: {computer_choice}')

  # 判断胜负
  result = determine_winner(player_choice, computer_choice)
  print(result)

# 运行游戏
play_game()

