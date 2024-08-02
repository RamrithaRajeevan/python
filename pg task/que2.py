#create program that ask user for number until they enter a negative number.print sum of all positive number enterd by user,terminating loop when a negativenumber is entered using break statement
def sum_of_num():
    sum=0
    while True:
        num=int(input("Enter number:"))
        if num < 0:
            break
        sum += num
    return sum

Sum=sum_of_num()
print("sum of all positive number:",Sum)