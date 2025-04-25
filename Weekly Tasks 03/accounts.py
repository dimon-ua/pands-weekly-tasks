# Author Dima
# Program: reads in a 10 character account number and outputs the account number with only the last 4 digits showing and the first 6 digits replaced with X

numbers_input = input("Please enter N-number of digits: ")
# we need a var with lentgh to check 10 digits number or more/less
numbers_input_len = len(numbers_input)

# at this section we will check which number to check, if equal 10, evaluate fisrt statement
if numbers_input_len == 10:
    hidden_number = numbers_input.replace(numbers_input[0:6], "XXXXXX")
    print(hidden_number)
else:
# in case of more then 10 or less number, evaluate this section.
    visible_number = numbers_input[-4:]
    hidden_number = len(numbers_input[0:-4])
    print("{}{}".format(hidden_number*'x', visible_number))
    
# do not relly like the ELSE section, a bit stupid I think, 
# will think how to make it readable and understandable

