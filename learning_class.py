from dataclasses import dataclass
from enum import Enum
from composition import Department
class EmployeeRole(Enum):
    DEVELOPER = "Developer"
    MANAGER = "Manager"
    TRAINEE = "Trainee"

@dataclass
class Employee:
    name: str
    salary:float
    role:EmployeeRole
    department: Department
    company = "Lumel Technologies"

    def get_employee_detail(self):
        return f"{self.name} + {self.salary} + {self.role.value}"
    @classmethod
    def get_company(cls):
      return cls.company
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company
    @staticmethod
    def validate_employee_salary(salary):
        return salary >0
    def give_raise(self,amount):
        self.salary += amount
if  __name__ == "__main__":
 department = Department("IT")
 employee = Employee("tamil",12000,EmployeeRole.DEVELOPER,department)
 employee_john = Employee("john",10000,EmployeeRole.MANAGER,department)
 print(employee)
 print(employee.give_raise(2000))
 print(employee.get_employee_detail())
 print(employee.get_company())
 print(employee.change_company("Microsoft"))
 print(employee_john.get_company())
 print(Employee.validate_employee_salary(1000))
