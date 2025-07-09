import paramiko

# 创建 SSHClient 对象
client = paramiko.SSHClient()

# 自动添加主机密钥,(如果之前没有连接过)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接到远程服务器
client.connect(hostname='192.168.0.201', username='openbayes', password='openbayes')

# 执行命令
_, stdout, stderr = client.exec_command('lsblk -f')

# 输出结果
print(stdout.read().decode())
print(stderr.read().decode())

# 关闭连接
client.close()
