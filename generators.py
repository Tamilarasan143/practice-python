def count_up_to(n):
    if (n <= 0):
        print("Please provide a positive number")
        return
    for i in range(n):
        yield i
for i in count_up_to(20):
    print(i)
my_generator = count_up_to(20)
print(my_generator)
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))

# employee reacord

employees = [
    {"name": "Tamil", "salary": 1200000},
    {"name": "John", "salary": 1800000},
    {"name": "Alice", "salary": 1500000},
    {"name": "Bob", "salary": 900000},
]

def employee_list(employees):
    for employee in employees:
        yield employee["name"]


        
get_employee_detail = (employee["name"] for employee in employees)

print(next(get_employee_detail))
print(next(get_employee_detail))
print(next(get_employee_detail))
print(next(get_employee_detail))
