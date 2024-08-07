#write a program to find 1st 5 multiply of 3 , but if a multiply of 3 is divisible by 4,skip it using a continue statement

def multiply_3():
    i=1
    count=0
    while count<5:
        mul=i*3
        if mul%4==0:
            i+=1
            continue
        print(mul)
        count+=1
        i+=1

multiply_3()