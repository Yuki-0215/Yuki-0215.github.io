import sys
# print(sys.prefix) # 获取python安装路径
# print(sys.exec_prefix) # 获取python执行路径

# sys.prefix 和 sys.exec_prefix 属性分别返回 Python 安装路径和执行路径,其中包含了标准库.这里我们导入的 sys 模块就是 Python 的标准库之一,之所以我们可以在代码中直接使用 sys 模块,这是因为这些标准库所在路径默认被包含在了 sys.path 中,这个路径是一个列表,包含了 Python 查找模块的路径.在导入模块时,Python 会按照 sys.path 中的路径顺序进行查找.
for path in sys.path:
  print(path)

'''
/Users/beiyiwangdejiyi/Desktop/lixie-work/note-k8s/blog/docs/3.develop/python/code # 当前目录(之所以可以运行 python 代码是因为这个在 path 路径中)
/opt/homebrew/Cellar/python@3.13/3.13.2/Frameworks/Python.framework/Versions/3.13/lib/python313.zip
/opt/homebrew/Cellar/python@3.13/3.13.2/Frameworks/Python.framework/Versions/3.13/lib/python3.13
/opt/homebrew/Cellar/python@3.13/3.13.2/Frameworks/Python.framework/Versions/3.13/lib/python3.13/lib-dynload
/opt/homebrew/lib/python3.13/site-packages
'''

# 上面列表中的路径就是 Python 查找模块的路径,包括当前目录、Python 安装目录、第三方库目录等,我们通过 pip 安装的第三方库会被添加到 site-packages 目录中.现在知道为什么我们可以直接导入当前目录和标准库中的模块了吧?因为这些路径都被包含在了 sys.path 中,Python 会按照这些路径顺序进行查找.

# 如果我们本地开发的一些包或者模块想让其他项目,我们可以将 这些包或者模块的路径添加到sys.path ,这样就可以在其他项目中导入这些包或者模块了

# 假设有一个自定义模块 mymodule.py 放在/path/to/your/modules 目录下:

def hello():
  return "Hello from mymodule!"

# 现在我们可以通过 sys.path 将这个模块添加到 Python 的搜索路径中,使Python 能够找到并导入这个模块



import sys

new_path = '/path/to/your/modules' # 自定义模块路径
if new_path not in sys.path:
  sys.path.append(new_path)

for path in sys.path:
  print(path)
