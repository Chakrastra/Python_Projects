#using regex

#conditions
# a-z
# 0-9
# . _ can be 1 time(before @)
# @ time 1
# . at 2nd or 3rd position from the last

import re
email_condition="^[a-z]+[\._]?+[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email=input('Enter your Email : ')

if re.search(email_condition,user_email):
    print("Valid Email")
else:
    print("Invalid Email")