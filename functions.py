# def means define
# In python by default the function are return "None Object" until we return anything
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

def create_employee(name:str,salary:int,experience:float,role:str = "Developer"):
    return {
        "name": name,
        "salary":salary,
        "experience":experience,
        "role":role
    }

print(create_employee(salary=500000,name="Tamil",experience=3.9))