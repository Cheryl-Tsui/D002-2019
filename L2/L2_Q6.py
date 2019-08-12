Time_Guessed=0
from random import randint
computer=randint(1,100)
print(computer)
for play in range(3):
    while Time_Guessed<=2:
        player=int(input("Enter a number."))
        if computer>player:
            print("Your guess is too low.")
            Time_Guessed=Time_Guessed+1
            continue
        if player>computer:
            print("Your guess is too high.")
            Time_Guessed=Time_Guessed+1
            continue
        if player>100 or player<1:
            print("Wrong input and guess number in [1,100].")
            Time_Guessed=Time_Guessed+1
            continue
        if computer==player:
            print("Congradulations!You have guess %d times."%Time_Guessed)
            break
    break

