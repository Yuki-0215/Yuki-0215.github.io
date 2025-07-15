from host import Host
from task import Task
from concurrent.futures import ThreadPoolExecutor

class ExeutionEngine:
  """执行引擎"""
  def __init__(self):
    self.hosts = []
    self.tasks = []

  def add_host(self, host):
    self.hosts.append(host)

  def add_task(self, task):
    """"添加任务"""
    self.tasks.append(task)

  def run(self):
    """执行任务"""
    def _execute_task(host, task):
      task.result = host.execute_command(task.command)
      return task, host
    with ThreadPoolExecutor() as executor:
      # 为每个主机执行任务
      futures = []
      for host in self.hosts:
        print(f"PLAY [{host.address}] {'*' * 50}")
        for task in self.tasks:
          futures.append(executor.submit(_execute_task, host, task))
      for future in futures:
        # 等待任务执行完成
        task, host = future.result() # 获取 task 和 host
        try:
          if task.status == "failure":
            raise Exception(task.result["stderr"])
        except Exception as exc:
            task.result = {"stdout": "", "stderr": str(exc), "exit_status": -1}
            task.status = "failure"

        print(f"{host.address} | {task.name} | {task.result} | {task.status}")
