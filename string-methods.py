#If you want to specify the data type of a variable, this can be done with casting.

#Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

name = "tamilarasane"
print(name[::-1])
print(name.count("t"))
print(name.replace("t", "T"))
print(name[-1])
print(name[0])
name_length  = len(name)
if name_length % 2 == 0:
    divided_length = name_length / 2
    print(name[int(divided_length) - 1] + name[int(divided_length)])
else :
    print(name[int(round(name_length/2,0))])