from learning_class import Employee


class Developer(Employee):
    def __init__(self,name,salary,role,language):
        super().__init__(name,salary,role)
        self.language = language

    def get_language(self):
        return self.language
    def get_employee_detail(self):
        employee_detail = super().get_employee_detail()
        return  f" {employee_detail} + {self.language}"

developer = Developer("Tamil",12000,"Role","Python")
print(developer.get_language())
print(Developer.get_company())
print(Developer.mro())
print(developer.get_employee_detail())