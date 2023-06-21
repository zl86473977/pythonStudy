class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {
            "语文": 0,
            "数学": 0,
            "英语": 0,
        }

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f"学生{self.name}(学号:{self.student_id})的成绩为：")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}")

stu1 = Student('rous', "001")
stu2 = Student('heis', "002")
print(stu1.name)
stu1.set_grade("数学", 99)
stu1.print_grades()










# class Person:
#     def put(self, machine, item):
#         print('put', item, 'into', machine)
#
#     def open(self, machine):
#         print('open', machine)
#
#
# class WashMachine:
#     def __init__(self, weight):
#         self.weight = weight
#
#     def clean(self, item):
#         print('clean', item)
#
#     def hot(self, item):
#         print('hot', item)
#
#
# me = Person()
#
# wm = WashMachine(10)
#
# me.put('衣服', wm)
# me.put('洗衣粉', wm)
# me.open(wm)
# wm.clean('衣服')
# wm.hot('衣服')
#
#
# print('我' * 3)

