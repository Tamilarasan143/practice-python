command = ""
while command.lower() != "quit":
    command = input(">")
    print("You : ", command)

print("You are Quit!")
stop = True
count = 5
forward_string = ""
revers_string = ""
while stop:
    for number in range(1, count + 1, 1):
        forward_string = forward_string + f"{number}"
        print(forward_string)
        if number == count:
            break
    for number in range(count, -1, -1):
        revers_string = forward_string[0:number]
        print(revers_string)
        count -= number
        if number == count:
            stop = False
            break
