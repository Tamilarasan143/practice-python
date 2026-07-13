employee_count = int(input("How many employees?: "))
employee_list = []
def get_employee_experience_level(experience):
    if experience < 2:
        return "Junior Developer"
    elif experience >= 2 and experience < 5:
        return "Mid Level Developer"
    else:
        return "Senior Developer"
yearly_bonus_percentage = 15 / 100
while employee_count > 0:
    name = input("Enter employee name: ")
    salary = float(input("Enter employee salary: "))
    experience = float(input("Enter employee experience: "))
    skills = [skill.strip() for skill in input("Enter your skills: ").split(",")]
    employee_list.append({
        "name": name,
        "salary": salary,
        "experience": experience,
        "skills": skills
    })
    employee_count -= 1
if len(employee_list) > 0:
 for index, employee in enumerate(employee_list):
    print(f"Employee {index + 1}:")
    print(f"Name: {employee['name']}")
    print(f"Salary: {employee['salary']}")
    print(f"Yearly Bonus: {employee['salary'] * yearly_bonus_percentage}")
    print(f"Experience: {employee['experience']}")
    print(f"Experience Level: {get_employee_experience_level(employee['experience'])}")
    if "Reactjs" in employee['skills'] or "react" in employee['skills']:
         print(f"React Developer: Yes")
    print(f"Skills: {', '.join(employee['skills'])}")
    print()
else:
    print("No employees were entered.")