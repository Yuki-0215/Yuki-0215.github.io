import random

choices = ["石头", "剪刀","布"]

def judge(player: str , computer: str):
  if player == computer:
    return '平局'
  elif player == '石头' and computer == '剪刀':
    return '玩家赢'
  elif player == '剪刀' and computer == '布':
    return '玩家赢'
  elif player == '布' and computer == '石头':
    return '玩家赢'
  else:
    return '电脑赢'

def play_game():
  print('欢迎来到石头剪刀布游戏!')
  print('请输入石头 剪刀 或 布')

  # 获取用户的输入
  player_choice = input("你的选择: ")

  # 检查输入是否有效
  if player_choice not in choices:
    print('输入无效,请重新输入...')
  else:
    computer_choice = random.choice(choices)
    print(f"电脑的选择: {computer_choice}")
  # 判断胜负
  result = judge(player_choice, computer_choice)
  print(result)

play_game()
