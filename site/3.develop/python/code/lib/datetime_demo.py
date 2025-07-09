import datetime

# 打印当前时间

now_time = datetime.datetime.now()
print(now_time, now_time.year, now_time.month, now_time.day)

# 格式化时间格式

formatted = now_time.strftime("%Y-%m-%d %H-%M-%S")
print(formatted)