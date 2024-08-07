#program that ask user for number until they enter 0.print sum of all number entered by user except for number7,using continue to ship adding 7 to all sum
sum=0
while True:
    num=int(input("Enter number:"))
    if num==0:
        break
    if num==7:
        continue
    sum+=num
print(sum)  
