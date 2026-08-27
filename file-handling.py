employees = ["Tamil", "John", "Alice", "Bob"]

def store_employees_to_file(filename, employees):
    with open(filename,"w") as file:
        for employee in employees:
            file.write(employee + "\n")

def add_employee_to_file(filename,employee):
    with open(filename,"a") as file:
        file.write(employee + "\n")

def read_employees_from_file(filename):
    try:
        with open(filename,"r") as file:
            employees = [line.strip() for line in file]
            return employees
    except FileNotFoundError as e:
        print(f"The file '{filename}' was not found. Error: {e}")
        return None

def delete_employee_from_file(filename,employee):
    try:
        with open(filename,"r") as file:
            employees = [line.strip() for line in file]
            if employee in employees:
                employees.remove(employee)
                with open(filename,"w") as file:
                    for employee in employees:
                        file.write(employee + "\n")
            else:
                print(f"The employee '{employee}' was not found in the file.")
    except FileNotFoundError as e:
        print(f"The file '{filename}' was not found. Error: {e}")

def update_employee_in_file(filename,old_employee,new_employee):
    try:
        with open(filename,"r") as file:
            employees = [line.strip() for line in file]
            if old_employee in employees:
                employees.remove(old_employee)
                employees.append(new_employee)
                with open(filename,"w") as file:
                    for employee in employees:
                        file.write(employee + "\n")
            else:
                print(f"The employee '{old_employee}' was not found in the file.")
    except FileNotFoundError as e:
        print(f"The file '{filename}' was not found. Error: {e}")
    
if  __name__ == "__main__":
    file_name = "employees.txt"
    store_employees_to_file(file_name, employees)
    add_employee_to_file(file_name,"Arun")
    content = read_employees_from_file(file_name)
    if content is None:
        pass
    else:
        print(content)
    delete_employee_from_file(file_name,"John")
    content = read_employees_from_file(file_name)
    if content is None:
        pass
    else:
        print(content)
    update_employee_in_file(file_name,"Tamil","Tamil Arasan")
    content = read_employees_from_file(file_name)
    if content is None:
        pass
    else:
        print(content)
