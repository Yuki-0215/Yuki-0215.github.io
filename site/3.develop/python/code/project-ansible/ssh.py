import paramiko

# 远程执行命令
def execute_remote_commond(host, port, command, username, password):
  try:
    print(f'Executing command: {command} on {host}')
    # 创建 SSHClient 对象
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    client.connect(host, port, username, password)
    # 执行命令
    _, stdout, stderr = client.exec_command(command)

    # 输出结果
    output = stdout.read().decode()
    error = stdout.read().decode()

    # 关闭连接
    client.close()
    return output, error
  except Exception as e:
    return None, str(e)
