name= input("Enter your name : ")
salary= float(input("Enter your salary : "))
experience= float(input("Enter your experience : "))
skills= input("Enter your skills : ").split(",")

if(experience<2):
    print("Junior Developer")
elif(experience>=2 and experience<5):
    print("Mid Level Developer")
else:
    print("You are a senior developer.")

print(F"Name : {name} \nSalary : {salary} \nExperience : {experience} \nSkills : {skills}")