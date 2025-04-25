# Author Dima
# Program: asks the user to input two numbers and then prints it in human readable format

# asking a user to input two numbers
amount1 = input("Please enter first amount(in cent) ") 
amount2 = input("Please enter second amount(in cent) ")

# getting numbers into Integer type to make some Math with them 
amount1 = int(amount1) / 100
amount2 = int(amount2) / 100

sum = amount1 + amount2

# output in readable format with the Euro sign
print(f'The sum of these is \N{euro sign}{sum}')
