import random

choices = ["石头", "剪刀", "布"]

def system_judge(player: str, computer: str):
  if player == computer:
    return "平局"
  elif player == "石头" and computer == "剪刀":
    return "玩家赢"
  elif player == "剪刀" and computer == "布":
    return "玩家赢"
  elif player == "布" and computer == "石头":
    return "玩家赢"
  else:
    return "电脑赢"

def play_game():
  print(f'欢迎来到石头剪刀布游戏!')
  print(f'请输入石头 剪刀或 布')

  # 获取用户输入
  user_player_choice = input("请输入你的选择: ")
  if user_player_choice not in choices:
    print('输入无效,请重新输入')
  else:
    computer_choice = random.choice(choices)
    print(f'电脑的选择: {computer_choice}')
  result = system_judge(user_player_choice, computer_choice)
  print(result)

play_game()


