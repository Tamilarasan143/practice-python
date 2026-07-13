employees = [
    {"name": "Tamil", "skills": ["React", "Next.js", "Python"]},
    {"name": "John", "skills": ["Java", "Spring"]},
    {"name": "Alice", "skills": ["React", "Node.js"]},
    {"name": "Bob", "skills": ["Angular"]},
]

for index, employee in enumerate(employees):
    if any(skills.lower() in ["react","reactjs"] for skills in employee["skills"]):
          print(f"{index}: {employee['name']}")
    