#write program to print all even numbers between 1 and 20 , skipping number 10 using continue statement
for num in range(1,21):
    if num %2!=0:
        continue
    if num==10:
        continue
    print(num)