# 异常类型

# IndexError索引错误
# number_list = [0, 1, 2, 3]
# number_list[4]  # list index out of range


# ZeroDivisionError除零错误
# print(100/0)  # division by zero

# FileNotFoundError 找不到文件错误
# f = open('./hi.txt', 'r')  # No such file or directory: './hi.txt'


try:
    user_weight = float(input("清输入您的体重(单位:kg)："))
    user_height = float(input("清输入您的身高(单位:m)："))
    user_BMI = user_weight / user_height ** 2
# 只要命中一条except则往下的所有都不会执行
except ValueError:
    print("输入不为合理数字，清重新运行程序，并输入正确的数字。")
except ZeroDivisionError:
    print("身高不能为零，请重新运行程序，并输入正确的数字。")
except:
    print("发生了未知错误，请重新运行程序")
else:
    print("您的BMI值为:" + str(user_BMI))
finally:
    print("程序结束执行。")

