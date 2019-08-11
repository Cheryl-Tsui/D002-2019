n=int(input("Please input a positive integer number larger than 2.:\n"))
r=2
while n>1:
    if (n%r==0):
        print("It is a not prime number.")
        break
    else:
        r=r+1
        if (r>n):
            print("It is a prime number.")
            break
    
    
