# There is no need of any kind keywords like const , var ,
# let to present variables in python just use name and = to there values
a = False
b = 4.99
c = "Hi"
d= 10

print(d)
name = "tamil"
name_length = len(name)
print(name_length)
print(name[0])
print(name[0:name_length])

# escape character
# \" add "" in center of string
# \' add ' in center of string
# \\ add \ in center of string
# \n to break the string or new line string

# Formatted String
escape_name = f"tamil length : {name_length}"
print(escape_name)

# if you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)