#snake water gun game
#random choices between snake or water or gun
#ask user snake water or gun
#play game 10 times with computer show results

import random
print("snake-water-gun")
n=int(input("enter the number of rounds:"))

options=["s","w","g"]

rounds=1
comp_win=0
user_win=0

while rounds<=n:
    print(f"round:{rounds}\n snake-'s'\n water-'w'\n gun-'g'")
    try:
        player=input("choose your input")
    except EOFError as e:
        print(e)
    if player!="s" and player!= "w" and player!= "g":
        print("invalid input try again")
        continue
    computer=random.choice(options)

    if computer=="s":
        if player=="w":
            comp_win+= 1
        elif player== "g":
            user_win+= 1

    elif computer=="w":
        if player=="s":
            user_win+=1
        if player=="g":
            comp_win+=1

    elif computer=="g":
        if player=="w":
            user_win+=1
        if player=="s":
            comp_win+=1

    if user_win>comp_win:
        print(f"you win round {rounds}\n")
    elif comp_win>user_win :
        print(f"you lost round {rounds}\n")
    else:
        print(f"round {rounds} resulted in tie")

    rounds+=1

if user_win>comp_win:
    print("congrats!! you win")
elif comp_win>user_win:
    print("you lost the game")
else:
    print("the match resulted in a draw")





