# Program: Collatz Conjecture
# slight description: if even, divide by 2; if odd, multiply by 3 and add 1
# asking user to input a postivie number 
positive_integer = int(input("Enter any positive integer: "))

# creating empty list
numbers_list = []
# number which was input by the user put into list
numbers_list.append(positive_integer)
index = 0

# at this section we have to avoid infinte loop, because iteratation at the end always will send us to number 4 again 
while numbers_list[index] != 1:  # interrupt the programm to avoid infinite loop 1-4-2-1  
    # if number is even
    if numbers_list[index] % 2 == 0:
        # we are taking the last number and putting it to the list
        numbers_list.append(numbers_list[-1]//2)     
        index +=1   
    else:
        # if odd multiply by 3 and add 1 and also put it ina list
        numbers_list.append(numbers_list[-1] * 3 + 1)        
        index +=1  

# output the list of numbers which we got in a while loop
print(numbers_list)
