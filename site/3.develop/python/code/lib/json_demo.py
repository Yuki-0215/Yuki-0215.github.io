import json

data = {
  'name': 'lixie',
  'age': 14
}

# 将字典转换为Json 字符串，（json 中字符串都是双引号）
json_str = json.dumps(data)
print(json_str)

# 将Json 字符串转换为字典。
print(json.loads(json_str))
