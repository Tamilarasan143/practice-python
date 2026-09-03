
class Employee:
    company = "Lumel Technologies"
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def get_employee_detail(self):
        return f"{self.name} + {self.salary} + {self.role}"
    @classmethod
    def get_company(cls):
      return cls.company
    def give_raise(self,amount):
        self.salary += amount
        return  self.salary

employee = Employee("tamil",12000,"hello")
employee_john = Employee("john",10000,"yes")
print(employee.get_employee_detail())
print(employee.give_raise(2000))
print(employee.get_employee_detail())
print(employee.get_company())
print(employee_john.get_company())
