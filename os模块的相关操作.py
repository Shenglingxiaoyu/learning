'''os模块可以对操作系统进行调用'''
import os
import os.path
'''os.system('notepad.exe')'''      #打开系统的记事本

#打开QQ的操作
'''os.startfile(r'C:\Program Files (x86)\Tencent\QQ\Bin\qq.exe')'''  #r的作用是使字符串里的转义字符不起作用

'''listdir的使用'''
lst = os.listdir('../pythonProject')
print(lst)

'''创建目录'''
os.mkdir('newdir')

'''创建多级目录'''
os.makedirs('A/B/C')

'''移除目录'''
os.rmdir('newdir')

'''移除多级目录'''
os.removedirs('A/B/C')

'''将path设置为当前工作目录'''
os.chdir('D:\pythonProject')
print(os.getcwd())     #返回当前工作路径

'''获取文件的绝对路径'''
print(os.path.abspath('os模块的相关操作.py'))

'''判断文件是否存在'''
print(os.path.exists('os模块的相关操作.py'),os.path.exists('sejrh'))

'''对文件路径进行拼接'''
print(os.path.join('pythonProject','os模块的相关操作.py'))

'''分离文件名与拓展名'''
print(os.path.splitext('os模块的相关操作.py'))  #多数可用于批量修改文件

'''提取文件的名字，不包括路径'''
print(os.path.basename('D:\pythonProject\os模块的相关操作.py'))

'''提取文件的路径但不包括文件名'''
print(os.path.dirname('D:\pythonProject\os模块的相关操作.py'))

'''用于判断是否为路径'''
print(os.path.isdir('os模块的相关操作.py'))