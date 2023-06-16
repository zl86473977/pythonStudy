# list_arr = ['你', '好', '吗', '兄', '弟']
# i = 0
# while i < len(list_arr):
#     print(list_arr[i])
#     i += 1

print('求平均值')
total = 0
count = 0
user_input = input("输入数字，以q终止")
while user_input != 'q':
    num = float(user_input)
    total += num
    count += 1
    user_input = input("输入数字，以q终止")
if count == 0:
    result = 0
else:
    result = total / count
print('the avarage is' + str(result))
