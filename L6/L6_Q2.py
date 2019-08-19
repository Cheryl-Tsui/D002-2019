import random
goat_1=100
goat_2=200
shown_goat=300
new_choose=0
win_change=0
lose_change=0
win_same=0
lose_same=0
for x in range(100):
    car=random.randint(1,3)
    print(car)
    for a in range(1,4):
        if car!=a:
            goat_1=a
    for b in range(1,4):
        if b!=car and b!=goat_1:
            goat_2=b
 
    print(car,goat_1,goat_2)
    choose=random.randint(1,3)
    if choose==car:
        lose_change=lose_change+1
    elif choose==goat_1:
        win_change=win_change+1
    elif choose==goat_2:
        win_change=win_change+1

print("Win change:%d." %win_change)
print("Lose change:%d." %lose_change)

for y in range(100):
    car=random.randint(1,3)
    print(car)
    for a in range(1,4):
        if car!=a:
            goat_1=a
    for b in range(1,4):
        if b!=car and b!=goat_1:
            goat_2=b
 
    print(car,goat_1,goat_2)
    choose=random.randint(1,3)
    if choose==car:
        d=random.randint(1,2)
        if d==1:
            shown_goat==goat_1
            print("Door %d is goat." %goat_1)
        if d==2:
            shown_goat==goat_2
            print("Door %d is goat." %goat_2)
    elif choose==goat_1:
        shown_goat==goat_2
        print("Door %d is goat." %goat_2)
    elif choose==goat_2:
        shown_goat==goat_1
        print("Door %d is goat." %goat_1)       
    if choose==car:
        win_same=win_same+1
        continue
    elif choose==goat_1:
        lose_same=lose_same+1
        continue
    elif choose==goat_2:
        lose_same=lose_same+1
        continue


print("Win same:%d." %win_same)
print("Lose same:%d." %lose_same)

if win_change>win_same:
    print("Since win_change>win_same, changing will have more advantage.")
if win_change<win_same:
    print("Since win_change<win_same, does not change is better.")
if win_change==win_same:
    print("There is no difference in terms of which one is better.")
