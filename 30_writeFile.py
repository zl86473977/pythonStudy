# with open("./30_data.txt", "w", encoding="utf-8") as f:
#     f.write("Hello!\n")
#     f.write("Yoooo")


# ‘r’:默认值，表示从文件读取数据。
# ‘w’:表示要向文件写入数据，并截断以前的内容
# ‘a’:表示要向文件写入数据，添加到当前内容尾部
# ‘r+’:表示对文件进行可读写操作（删除以前的所有数据）
# ‘b’:表示要读写二进制数据

# with open("./30_data.txt", "r+", encoding="utf-8") as f:
#     print(f.read())
#     f.write("Hello!\n")

with open("./30_data.txt", "w", encoding="utf-8") as f:
    f.write("我欲乘风归去， \n又恐琼楼玉宇，\n高处不胜寒。\n")

with open("./30_data.txt", "a", encoding="utf-8") as f:
    f.write("起舞弄清影， \n何似在人间。")