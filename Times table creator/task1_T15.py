user_num = int(input("Please enter a number!:"))
# Requests input from user and changes into integer


# For loop that will start at 1 and go upto and include 12 not 13
# Will get the user input and mulitple it by every number from 1 to 12
# Each time it will be print and be formatted as the print statement shows below
for i in range(1, 13):
    print(f' {user_num} x {i} = {user_num * i}')
