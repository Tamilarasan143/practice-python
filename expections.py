def get_employee_salary_experience():
    try:
        salary = float(input("Enter your salary: "))
        experience = float(input("Enter your experience: "))
        print("Salary", salary)
        print("Experience", experience)
    except ValueError:
        print("Please enter a valid number")
    except Exception as e:
        print(e)
    else:
        print("else block executed")
    finally:
        print("finally block executed")

class InvalidEmployeeDetails(Exception):
    pass
def validate_employee_details(name, salary, experience):
    if not name or name.strip() == "":
        raise InvalidEmployeeDetails("Invalid name, Must be string and not be empty")
    if salary < 0:
        raise InvalidEmployeeDetails("Invalid salary , Must not be negative")
    if experience < 0:
        raise InvalidEmployeeDetails("Invalid experience, Must not be negative")
    return True
    
def validate_employee(name, salary, experience):
    try:
       validate_employee_details(name, salary, experience)
    except InvalidEmployeeDetails as e:
        print(e)
    else:
       print(f"Name: {name}, slalry: {salary}, experience: {experience}")
    finally:
        print("finally block executed")
        

if __name__ == "__main__":
    validate_employee("Tamil", 1200000, 2)
    validate_employee("", 0, 2)