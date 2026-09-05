from dataclass_modal import Project
from dataclasses import dataclass
from learning_class import Employee , EmployeeRole
from composition import Department

@dataclass
class Developer(Employee):
    language:str
    project:Project
    def get_language(self):
        return self.language
    def get_employee_detail(self):
        employee_detail = super().get_employee_detail()
        return  f" {employee_detail} + {self.language}"
    # polymorphism diff class and diff object same function but diff functionality but also extends same inherit class
    def get_work(self):
        return "Coding Work"


class Manager(Employee):
    # polymorphism diff class and diff object same function but diff functionality but also extends same inherit class
     def get_work(self):
        return "Maintain Work"

if __name__ == "__main__":
 department = Department("Engineering")
 project = Project("Gen AI")
 developer = Developer("Tamil",12000,EmployeeRole.MANAGER,department,"Python", project)
 manager = Manager("Tamil",12000,EmployeeRole.DEVELOPER,department)
 print(developer)
 print(manager.get_work())
 print(developer.department.name)
 print(manager.department.name)
 developer.department.change_department("AI")
 print(developer.department.name)
 print(manager.department.name)