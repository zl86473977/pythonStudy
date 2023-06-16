def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        category = '偏瘦'
    elif bmi <= 25:
        category = '正常'
    elif bmi <= 30:
        category = '偏胖'
    else:
        category = '肥胖'
    print(f"你的BMI分类为: {category}")
    return bmi


your_weight = input('体重')
your_height = input('身高')
result = calculate_bmi(float(your_weight), float(your_height))
print(result)