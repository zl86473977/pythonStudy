class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"name:{self.name}, id is {self.id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, id, month_salary):
        super().__init__(name, id)
        self.month_salary = month_salary

    def calculate_monthly_pay(self):
        return self.month_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        return self.daily_salary * self.work_days


zs = FullTimeEmployee('zs', '001', 5000)
ls = PartTimeEmployee('ls', '002', 200, 20)

zs.print_info()
ls.print_info()
print(zs.calculate_monthly_pay())
print(ls.calculate_monthly_pay())