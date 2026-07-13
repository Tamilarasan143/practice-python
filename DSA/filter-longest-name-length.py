from typing import Dict


employees = [
    {
        "name": "Tamil",
        "salary": 1200000,
        "experience": 3.5,
        "skills": ["React", "Python"],
    },
    {
        "name": "John",
        "salary": 1800000,
        "experience": 7,
        "skills": ["Java", "AWS"],
    },
    {
        "name": "Alice",
        "salary": 1500000,
        "experience": 4,
        "skills": ["React", "Next.js"],
    },
    {
        "name": "Bob",
        "salary": 900000,
        "experience": 1,
        "skills": ["Python"],
    },
]

def iterate_developer(developer:str,developer_name:list[str]):
    print(developer)
    if len(developer_name) > 0:
        for name in developer_name:
            print(name)
    else:
        print(f"No Records matched : {developer}")
    print("----------------")

# Easy One Traverse
max_employee_name_length = 0
max_employee_with_big_name = ""
for employee in employees:
    employee_name_length = len(employee["name"])
    if employee_name_length > max_employee_name_length:
       max_employee_name_length = employee_name_length
       max_employee_with_big_name = employee["name"]

print(f"employee with the big name {max_employee_with_big_name } and the length {max_employee_name_length}")
# Time Complex: O(n) and one travsal

# Medium

employee_skill_list_count:Dict[str, int] = {}
for employee in employees:
    for skill in employee["skills"]:
         employee_skill_list_count[skill] = employee_skill_list_count.get(skill, 0) + 1

print(f"employee skills total skill count {employee_skill_list_count}")
# Time complex: O(n* k) and nested travsal

# Hard

#example output 
react_skill_set = {"react","reactjs"}
python_skill_set  ={"python"}
aws_skill_set = {"aws"}
employee_total_salary = 0
total_employees = len(employees)
highest_salary_employee = { 
    "name": employees[0]["name"], 
    "salary":employees[0]["salary"] 
    }
lowest_salary_employee = { 
    "name": employees[0]["name"], 
    "salary":employees[0]["salary"] 
    }
react_developers = []
python_developers = []
aws_developers = []
total_employees_experience:float = 0
junior_developer_count = 0
senior_developer_count = 0
mid_developer_count = 0
for employee in employees:
    employee_total_salary += employee["salary"]
    total_employees_experience += float(employee["experience"])
    if highest_salary_employee["salary"] < employee["salary"]:
        highest_salary_employee = {"name": employee["name"],"salary": employee["salary"]}
    if lowest_salary_employee["salary"] > employee["salary"]:
        lowest_salary_employee = {"name": employee["name"],"salary": employee["salary"]}
    if employee["experience"] < 2 :
        junior_developer_count +=1
    if employee["experience"] >= 2 and employee["experience"] <=5:
        mid_developer_count +=1
    if employee["experience"] > 5:
        senior_developer_count +=1
    for skill in employee["skills"]:
        skill_key = f"{skill} Developer"
        if skill.lower() in react_skill_set :
            react_developers.append(f"{employee['name']}")
        if skill.lower() in python_skill_set:
            python_developers.append(f"{employee['name']}")
        if skill.lower() in aws_skill_set:
            aws_developers.append(f"{employee['name']}")
print("===========================")
print("Employee Analytics")
print("===========================")
print(f"Total Employees: {total_employees}")
print(f"Total Salary: {employee_total_salary}")
print(f"Average Salary: {float(employee_total_salary / total_employees)}")
print(f"Highest Paid: {highest_salary_employee['name']}")
print(f"lowest Salary: {lowest_salary_employee['name']}")
iterate_developer("React Developers",react_developers)
iterate_developer("Python Developers",python_developers)
iterate_developer("AWS Developers",aws_developers)
print(f"Average Experience: {float(total_employees_experience / total_employees)}")
print(f"Senior Developers: {senior_developer_count}")
print(f"Mid Developers: {mid_developer_count}")
print(f"Junior Developers: {junior_developer_count}")

