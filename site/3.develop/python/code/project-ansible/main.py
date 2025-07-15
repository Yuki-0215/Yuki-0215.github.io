from config import load_configuration
from task import Task
from host import Host
from engine import ExeutionEngine

if __name__ == '__main__':
  conf = load_configuration('playbook.yaml')

  engine = ExeutionEngine()

  # 将主机添加到任务管理器中
  for host in conf['hosts']:
    engine.add_host(Host(['address'], host['username'], host['password']))

  # 将任务添加到任务管理中
  for task in conf['tasks']:
    engine.add_task(Task(task['name'], task['command']))

  engine.run()
  print('任务执行完成!!!')
