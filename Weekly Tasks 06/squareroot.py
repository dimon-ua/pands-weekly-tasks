# By the task of this program we neet to write a func to find a square root number not using build in methos

# creating a func with n parameter
def sqrt(n):
    x = 3
    approx = 0.5 * n
# an iteration where in three steps finding the square root number with some Math steps
    for i in range(x):
        better_approx = 0.5*(approx + n/approx)
        approx = better_approx 
    print(f"The square root of {n} is approx. {better_approx}. ")

root_num = float(input("Please enter a positive number: "))
sqrt(root_num)
