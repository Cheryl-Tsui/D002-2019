number=[]
difference=999999999999999999999999999999999999999
b=int(input("Enter a number."))
number=number+[b]
for d in range(1,10):
    a=int(input("Enter a number."))
    for c in number:
        if c>=a:
            z=c-a
            if z<difference:
                difference=z
            elif z==difference:
                difference=z
        elif c<a:
            z=a-c
            if z<difference:
                difference=z

    number=number+[a]
    print(difference)
            


