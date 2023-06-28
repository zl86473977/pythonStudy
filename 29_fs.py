# "r" 读取模式-只读(默认)
# "w" 西入模式-只写
f = open("./29_data.txt", "r", encoding="utf-8")

# print(f.read()) #会读全部的文件内容，并打印
# print(f.read()) #会读空字符串，并打印

# print(f.read(10)) # 会读第1-10个字节的文件内容

# print(f.readline()) # 会读一行文件内容，并打印

# line = f.readline()
# while line != "":  # 判断当前行是否为空
#     print(line)  # 不为空则打印当前行
#     line = f.readline()  # 读取下一行

# readlines会读全部文件内容，并把每行作为列表元素返回
print(f.readlines())
# lines = f.readlines()  # 把每行内容储存到列表里
# for line in lines:  # 遍历每行内容
#     print(line)  # 打印当前行

f.close()  # 关闭文件 释放资源

# with open("./29_data
# .txt", "r", encoding="utf-8") as f:
#     print(f.read())  # 对文件的操作
