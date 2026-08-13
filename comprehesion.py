numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# output [4, 16, 36, 64, 100]

print([num * num for num in numbers if num%2 == 0])

employees = [
    {
        "name": "Tamil",
        "salary": 1200000,
        "experience": 3.5,
        "skills": ["React", "Python", "Docker"]
    },
    {
        "name": "John",
        "salary": 1800000,
        "experience": 7,
        "skills": ["Java", "AWS", "Docker"]
    },
    {
        "name": "Alice",
        "salary": 1500000,
        "experience": 4,
        "skills": ["React", "Next.js", "Python"]
    },
    {
        "name": "Bob",
        "salary": 900000,
        "experience": 1,
        "skills": ["Python", "Docker"]
    }
]
# senior_names output is ["John", "David"]

print("High-salary names",[employee["name"] for employee in employees if employee["salary"] > 1000000])
print("Unique skills",{ skill for employee in employees for skill in employee["skills"]  }) 
print("Salary dictionary",{employee["name"]:employee["salary"] for employee in employees})