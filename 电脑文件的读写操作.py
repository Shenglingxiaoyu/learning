'''电脑文件的读写操作'''
'''file = open('文件名',文件的操作方式(读还是写),编码类型)'''
#r模式表示读取文件
file = open('text.txt','r')
print(file.readline())
file.close()

#w模式表示写入文件，若文件不存在变回创建文件，若文件存在变回覆盖原有内容
file1 = open('a_text.txt','w')
file1.write('hello world')
file1.close()

#a模式为追加模式，若文件存在则在文件末尾写入内容，若文件不存在则创建文件
file2 = open('b_text.txt','a')
file2.write('python')
file2.close()
