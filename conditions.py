name = "Tamil"
age = 24
print("type(name)", type(name))
# if else condition
if type(name) == "str":
    print("the type of name is string")
else:
    print("the type of name is unknown")

# Ternary Operator
print(f"{name} is above 18 and a major") if age > 18 else print(
    f"{name} is under 18 and a miner")
