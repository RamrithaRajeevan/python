#write program to count total number of digits in a number using while loop
def count_digits(number):
    num_str = str(number)
    count = 0
    while count < len(num_str):
        if num_str[count].isdigit(): 
            count += 1
        else:
            count += 1
    
    return count

number = int(input("Enter a number: "))
print(f"Total number of digits: {count_digits(number)}")
