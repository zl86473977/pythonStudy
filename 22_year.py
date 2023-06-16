contacts = ['康子', '亮仔', '坤坤']

year = 2023
# 受顺序控制
# for name in contacts:
#     message_content = """
#     1111，1111。
#     2222，2222。
#     3{0}33，3333.
#     4{0}44，4444，
#     5{1}555555！
#     6666{1}666！
#     """.format(year, name)
#     print(name, message_content)

# 受字段控制，顺序自由
# for name in contacts:
#     message_content = """
#     1111，1111。
#     2222，2222。
#     3{year_0}33，3333.
#     4{year_0}44，4444，
#     5{name_0}555555！
#     6666{name_0}666！
#     """.format(name_0=name, year_0=year)
#     print(name, message_content)

# 更简洁的写法
# for name in contacts:
#     message_content = f"""
#     1111，1111。
#     2222，2222。
#     3{year}33，3333.
#     4{year}44，4444，
#     5{name}555555！
#     6666{name}666！
#     """
#     print(name, message_content)

"""
康子 
    1111，1111。
    2222，2222。
    3202333，3333.
    4202344，4444，
    5康子555555！
    6666康子666！
    
亮仔 
    1111，1111。
    2222，2222。
    3202333，3333.
    4202344，4444，
    5亮仔555555！
    6666亮仔666！
    
坤坤 
    1111，1111。
    2222，2222。
    3202333，3333.
    4202344，4444，
    5坤坤555555！
    6666坤坤666！

"""

gpa_dict = {
    '小明': 3.251,
    '小花': 3.869,
    '小李': 2.683,
    '小张': 3.685
}
for name, gap in gpa_dict.items():
    # print("{0}你好，你的当前绩点为：{1:.2f}".format(name, gap))
    print(f"{name}你好，你的当前绩点为：{gap:.2f}")