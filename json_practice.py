import json

employee = {
    "name": "Alice",
    "salary": 1200000,
    "experience": 3.5,
    "skills": ["React", "Python", "FastAPI"]
}

employees = [
    {
        "name": "Tamil",
        "salary": 1200000,
        "experience": 3.5,
        "skills": ["React", "Python"]
    },
    {
        "name": "John",
        "salary": 1800000,
        "experience": 7,
        "skills": ["Java", "AWS"]
    }
]
#Read employees
def read_employees(filename):
    try:
        with open(filename,"r") as file:
            employee_data = json.load(file)
            return employee_data
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return []
#Add employee
def add_employee(filename,employee):
    employee_data = read_employees(filename)
    employee_data.append(employee)
    with open(filename,"w") as file:
        json.dump(employee_data,file,indent=4)
#Update employee
def update_employee(filename,oldEmployeeName):
    employees = read_employees(filename)
    #breakpoint()
    for index,employee in enumerate(employees):
        if employee["name"] == oldEmployeeName:
            newEmployeeName = input("Enter new name: ")
            employees[index]["name"] = newEmployeeName
            break
    else:
        raise ValueError(f"Employee '{oldEmployeeName}' not found")
    with open(filename,"w") as file:
        json.dump(employees,file,indent=4)
    
#Delete employee
def delete_employee(filename,employeeName):
    employees = read_employees(filename)
    for index,employee in enumerate(employees):
        if employee["name"] == employeeName:
            del employees[index]
            break
    else:
        raise ValueError(f"Employee '{employeeName}' not found")
    with open(filename,"w") as file:
        json.dump(employees,file,indent=4)
#Search employee
def search_employee(filename,employeeName):
    employees = read_employees(filename)
    for employee in employees:
        if employee["name"] == employeeName:
            return employee
    return None

def store_employee_data_in_json(filename,employee):
    with open(filename,"w") as file:
        json.dump(employee,file,indent=4)

def load_employee_data_from_json(filename):
    try:
        with open(filename,"r") as file:
            employee = json.load(file)
            return employee
    except FileNotFoundError as e:
        print(e)
    except json.JSONDecodeError as e:
        print(e)

if __name__ == "__main__":
    file_name = "employee.json"
    employee_data = read_employees(file_name)
    #add_employee(file_name,employee)
    print(search_employee(file_name,"Jhon"))
    print(update_employee(file_name,"Jhon"))
    delete_employee(file_name,"Jhonathan")