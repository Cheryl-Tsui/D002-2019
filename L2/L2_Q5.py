import random
number_p_win=1
for play in range (3):
    while number_p_win<=3:
        print('Welcome to the rock-paper-scissor game!\nYou are going to play against a minion!')
        print("""
        1.                 2.                           3.
            _______                 _______                      _______
        ---'   ____)            ---'   ____)____             ---'   ____)____
              (_____)                     ______)                      ______) 
              (_____)                     _______)                  __________)
              (____)                     _______)                  (____)
        ---.__(___)             ---.__________)              ---.__(___)
        """) # 1 for rock; 2 for paper; 3 for scissor

        # step1: get player's choice, save it in variable p_choice
        p_choice=int(input("Please choose a number; 1 for stone, 2 for paper, and 3 for scissors."))
        # step2: generate a random choice for minion, save it in variable m_choice
        from random import randint
        m_choice = randint(1,3)

        # status is used for the win/lose/draw of the game
        # status = 1 means player wins; status = 2 means minion wins; status = 3 means draw;
        # status = 4 means user gives invalid input, e.g. player inputs -1 or 4
        status = 0 # initialized as 0
        # step 3: given choices from player and minion, decide the game status
        if m_choice==p_choice:
            status=3
            
            if status==3:
                print("draw")
            continue
        elif m_choice==1 and p_choice==2:
            status=1
        elif m_choice==2 and p_choice==3:
            status=1
        elif m_choice==3 and p_choice==1:
            status=1
        elif p_choice==1 and m_choice==2:
            status=2
        elif p_choice==2 and m_choice==3:
            status=2
        elif p_choice==3 and m_choice==1:
            status=2
        else:
            status=4
            break
        # step4: display the minion's choice
        if m_choice == 1:
            print("Minion chooses rock!")
        elif m_choice == 2:
            print("Minion chooses paper!")
        elif m_choice == 3:
            print("Minion chooses scissor!")

        if status==1:
            print("you win!")
            number_p_win=number_p_win+1
            if number_p_win==4:
                print("You are the KING!")
                break
            continue
        if status==2:
            print("minion win!")
            continue
        if status==3:
            print("draw")
            continue
