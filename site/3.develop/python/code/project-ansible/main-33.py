from concurrent.futures import ThreadPoolExecutor
from config import load_configuration
from ssh import execute_remote_commond

def execute_tasks(hosts, tasks):
  with ThreadPoolExecutor() as executor:
    # 提交任务
    futures = []
    for host in hosts:
      for task in tasks:
        future = executor.submit(execute_remote_commond, host['address'],host['port'],
                                 task['command'],host['username'], host['password'])
        futures.append(future)
    for future in futures:
      output, error = future.result()
      if error:
        print(f'Error: {error}')
      else:
        print(f'Output: {output}')

if __name__ == '__main__':
  conf = load_configuration('playbook.yaml')
  execute_tasks(conf['hosts'], conf['tasks'])
