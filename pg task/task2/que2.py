#program that generate random number b/w 1 & 100 until it generate number that is prefect square.print number &its square root,then terminate loop using break statement.
def perfect_square(num):
    root = int(num ** 0.5)  
    return root * root == num
for number in range(1, 101):
    if perfect_square(number):
        square_root = int(number ** 0.5)
        print("The number " + str(number) + " is a perfect square with a square root of " + str(square_root) + ".")
        break
    print("Checked number:" +str(number))