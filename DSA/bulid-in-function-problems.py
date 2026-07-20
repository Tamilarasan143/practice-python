


from cmath import rect
from typing import Dict


employees = [
    {"name": " Tamil ", "salary": 1200000},
    {"name": " John ", "salary": 900000},
]
# Easy
print("Easy ===========>")
employees_strip_list = []
for employee in employees:
    update_employee = employee.copy()
    update_employee["name"] = update_employee["name"].strip()
    employees_strip_list.append(update_employee)
print("original",employees)
print("updated",employees_strip_list)

# Medium
print("Medium ===========>")
skills = "React, Python, FastAPI, Docker"
new_skills = []
for skill in skills.split(","):
    new_skills.append(skill.strip().lower())
print(new_skills)
employees_strip_dic:Dict[str, int] = {}
for employee in employees_strip_list:
     employees_strip_dic[employee["name"]] = employees_strip_dic.get(employee["name"],employee["salary"]) // 2
print(employees_strip_dic)
# Hard
print("Hard ===========>")
def iterate_print_obj(title,value = "",dev_list = False,obj_key = None):
    if dev_list == False:
      print(f"{title} : ")
    type_value = lambda val: isinstance(val,str) or isinstance(val,int)
    if type_value(value):
        print(value)
    else:
        for val in value:
          if type_value(val):
            print(f"{val} Developers") if dev_list else print(val)
          elif isinstance(val,Dict):
             print(val[obj_key]) if obj_key != None else print(value)
          else:
              for nested_val in val:
                  print(nested_val)
              
    
employees_list = [
    {
        "name": "Tamil",
        "salary": 1200000,
        "experience": 3.5,
        "skills": ["React", "Python", "Docker"],
    },
    {
        "name": "John",
        "salary": 1800000,
        "experience": 7,
        "skills": ["Java", "AWS", "Docker"],
    },
    {
        "name": "Alice",
        "salary": 1500000,
        "experience": 4,
        "skills": ["React", "Next.js", "TypeScript"],
    },
    {
        "name": "Bob",
        "salary": 900000,
        "experience": 1,
        "skills": ["Python", "Docker"],
    },
    {
        "name": "David",
        \
        "salary": 2100000,
        "experience": 9,
        "skills": ["React", "AWS", "Kubernetes"],
    },
]
total_employees_salary = 0
unique_skills_set = set()
developers_obj = {
    "react": [],
    "python":[], 
    "aws":[]
}
developers_diff_experience = {
    "junior":[],
    "mid":[],
    "senior":[],
}
total_number_employees = len(employees_list)
sorted_employees_based_on_salary = sorted(employees_list,key=lambda employee:employee["salary"],reverse=True)
highest_paid_employee = sorted_employees_based_on_salary[0]
lowest_paid_employee = sorted_employees_based_on_salary[total_number_employees - 1]
for employee_detail in employees_list:
   employee = employee_detail.copy()
   total_employees_salary += employee["salary"]
   if employee["experience"] <=2:
       developers_diff_experience["junior"].append(employee["name"])
   elif employee["experience"] <=5:
       developers_diff_experience["mid"].append(employee["name"])
   else:
       developers_diff_experience["senior"].append(employee["name"])
   for skills in employee["skills"]:
       unique_skills_set.add(skills)
       if skills.strip().lower() in ["react","reactjs"]:
           developers_obj["react"].append(employee["name"])
       if skills.strip().lower() == "python":
           developers_obj["python"].append(employee["name"])
       if skills.strip().lower() == "aws":
           developers_obj["aws"].append(employee["name"])
print("===========================")
print("Employee Analytics")
print("===========================")
iterate_print_obj("Total Employees:" , total_number_employees)
iterate_print_obj("Highest_salaried_employee:", f"{highest_paid_employee['name']} - {highest_paid_employee['salary']}")
iterate_print_obj("lowest_salaried_employee:", f"{lowest_paid_employee['name']} - {lowest_paid_employee['salary']}")
iterate_print_obj("", developers_diff_experience,True)
iterate_print_obj("", developers_obj,True)
iterate_print_obj("Unique Skills:", unique_skills_set)
iterate_print_obj("Top 3 Highest Salaries:", sorted_employees_based_on_salary[:3],False,"name")