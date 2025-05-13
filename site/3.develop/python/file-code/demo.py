# file = open('example.txt',mode='w',encoding='utf-8')
# file.write('Hello world!\n xiege66')
# file.close

# read() 读取整个文件，并返回一个字符串

'''
file = open('example.txt', 'r')
context = file.read()
print(context)
file.close
'''


# readline() 读取文件中的一行内容

'''
file = open('example.txt', mode='r')
context1 = file.readline()
print(context1)
'''


# readlines() 按行读取每一行返回一个列表
'''
file = open('example.txt', mode='r')
context1 = file.readlines()
print(context1)
'''

# write
# 同样通过文件对象的 write() 和 writelines() 方法可以写入文件内容。
'''
file = open('example.txt',mode='w',encoding='utf-8')
file.write('Hello lixie~')
file.close
'''

# writelines()
'''
lines = ["Hello, World!\n", "Python is fun!\n"]

file = open('example.txt',mode='w')
file.writelines(lines)
file.close
'''
