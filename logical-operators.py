# There are three types of logical operators in python  : and , or , not
high_income = True
good_credit = False
student = True

# Short circuit evaluation
#     True           False               True
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
