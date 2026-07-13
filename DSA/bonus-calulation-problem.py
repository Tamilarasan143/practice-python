employee = {
    "name": "Tamil",
    "salary": 1200000,
    "skills": ["React", "Next.js", "Python"]
}
name = employee["name"]
salary = employee["salary"]
skills = employee["skills"]
yearly_bonus = salary * (15 / 100)


print(f"Yearly_Bonus: {yearly_bonus}")
print(f"Monthly_Salary: {salary // 12}")
print(f"Yearly_Income: {salary + yearly_bonus}")
print(f"Salary: {salary}") 
print(f"Skills: {', '.join(skills)}")