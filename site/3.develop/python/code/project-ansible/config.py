import yaml

# 加载配置文件

def load_configuration(config_file_path: str):
  with open(config_file_path, 'r') as file:
    return yaml.safe_load(file) # 解析 yaml 文件

if __name__ == '__main__':
  data = load_configuration('playbook.yaml')
  print(data)
