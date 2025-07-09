class Task:
  def __init__(self, name, command):
    self.name = name
    self.command = command
    self.result = None # 任务执行结果
    self.status = "pending" # 任务状态, pending, success, faild
  def __repr__(self):
    """返回任务的字符串表示"""
    return f"Task({self.name!r}, {self.command!r}, status={self.status!r})"
