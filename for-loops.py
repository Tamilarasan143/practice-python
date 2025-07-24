end_number = 10
break_loop = 12
for number in range(0, end_number, 2):
    print("numbers", number)
    if number >= break_loop:
        break
else:
    print(f"The {break_loop} is greater then {end_number}")

# Nested Loop

for x in range(3):
    for y in range(2):
        print(f"{x} : {y}")
