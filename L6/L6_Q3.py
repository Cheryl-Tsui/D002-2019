import random
number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random_no_1 =[]
random_no_2 =[]
random_no_3 =[]
random_no_4 =[]
random_no_5 =[]
a=random.randint(1,20)
b=random.randint(1,20)
c=random.randint(1,20)
d=random.randint(1,20)
e=random.randint(1,20)
random_no_1 = random_no_1 + [a] + [b] + [c] + [d] + [e]
random_no_2 = random_no_2 + [b] + [c] + [d] + [e]
random_no_3 = random_no_3 + [c] + [d] + [e]
random_no_4 = random_no_4 + [d] + [e]
random_no_5 = random_no_5 + [e]

n=0
y=0
for k in random_no_1:
    z= [number] - [random_no_1]
    if [random_no_1][n]>z:
        z=y
        
    if z==1:
        number = number - random_no_1[k]  
        if len(number)==5:
            print(number)
            break

for k in random_no_2:
    z= number - random_no_2
    if z==1:
        number = number - random_no_2[k]
        if len(number)==5:
            print(number)
            break

for k in random_no_3:
    z= number - random_no_3
    if z==1:
        number = number - random_no_3[k]
        if len(number)==5:
            print(number)
            break

for k in random_no_4:
    z= number - random_no_4
    if z==1:
        number = number - random_no_4[k]
        if len(number)==5:
            print(number)
            break

for k in random_no_5:
    z= number - random_no_5
    if z==1:
        number = number - random_no_5[k]
        if len(number)==5:
            print(number)
            break
