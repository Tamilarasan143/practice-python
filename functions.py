# def means define
# In python by default the function are return "None Object" until we return anything

import numbers
from typing import Dict
def greeting():
    print("Hello World")


greeting()


# Parameter function
def addition(one, two):
    return one + two


print(addition(two=2, one=1))

#Advance Functions 

def greet(name: str) -> str:
    return f"Hello {name}"

greet("Tamil")

def calculate_yearly_income(
    salary: float,
    bonus_percentage: float
) -> float:
    bonus = salary * bonus_percentage
    return salary + bonus

print(calculate_yearly_income(500000,10))

def create_employee(name:str,salary:int,experience:float,role:str = "Developer") -> Dict[str, str or float]:
    return {
        "name": name,
        "salary":salary,
        "experience":experience,
        "role":role
    }

print(create_employee(salary=500000,name="Tamil",experience=3.9))
# just spread operator in typescript
def calculate_average(*args) -> int:
    if len(args) == 0 or args == None or type(args) != isinstance(args,numbers.Number):
        return "non number"
    average = 0
    for number in args:
        if isinstance(number,numbers.Number):
            average += number
    return average / len(args)

print(calculate_average(500000, 700000, "900000"))

employee= {
    "name":"Tamil",
    "salary":12000
}

employee1= {
    **employee,
    "salary": 130000
}
def get_employees(**args):
    print(args)

get_employees(**employee)
get_employees(**employee1)


# lambda

employees = [
    {"name": "Tamil", "salary": 1200000},
    {"name": "John", "salary": 1800000},
    {"name": "Alice", "salary": 1500000},
    {"name": "Bob", "salary": 900000},
]
value = sorted(employees,key=lambda employee: employee["salary"])
print("map")
print(list(map(lambda employee: employee["name"] ,value)))
print("filter")
print({employee["name"] for employee in employees if employee["salary"] > 1000000})
print(list(filter(lambda employee: employee["name"] if employee["salary"] < 1000000 else None,value)))

print("map + filter")
print(list(map(lambda employee: employee["name"],filter(lambda employee: employee["salary"] > 1000000,value))))