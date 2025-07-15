import paramiko

class Host():
  """主机类"""
  def __init__(self, address, username, password) -> None:
    self.address = address
    self.username = username
    self.password = password
  def __repr__(self):
    return f"Host({self.address!r}, {self.username!r})"

  def execute_command(self, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
      # 连接到远程服务器
      client.connect( self.address, username=self.username, password=self.password)
      # 执行命令
      _, stdout, stderr = client.exec_command(command)
      # 获取命令退出状态(0表示成功,非 0 表示失败)
      exit_status = stdout.channel.recv_exit_status()
      # 输出结果
      result = {
        "stdout": stdout.read().decode(),
        "stdout": stderr.read().decode(),
        "exit_status": exit_status
      }
    except Exception as e:
      result = {"stdout":"", "stderr": str(e), "exit_status": -1}
    finally:
      client.close()
    return result
