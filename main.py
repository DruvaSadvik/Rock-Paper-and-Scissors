import random
ran_num = random.randint(1, 3)
#function for game
def game(you1,comp1):
    if you1==comp1:
        print("the game is tie")
    elif you!=comp:
        if you==1 and comp==2:
            print("you loose")
        elif you==1 and comp==3:
            print("your the winner")
        elif you == 2 and comp == 1:
            print ("your the winner")
        elif you==2 and comp==3:
            print("you loose")
        elif you==3 and comp==1:
            print("you loose")
        elif you==3 and comp==2:
            print("your the winner")
        else:
            return 0
    else:
        return 0


you = int(input("CHOOSE \n"
          "ROCK for 1\n"
          "PAPER for 2\n"
          "SCISSORS for 3\n"))
if ran_num==1:
    comp=1
elif ran_num==2:
    comp=2
elif ran_num==3:
    comp=3
else:
    print("invalid command")




if comp==1:
    choice2 = "ROCK"
elif comp==2:
    choice2 = "PAPER"
elif comp==3:
    choice2="SCISSORS"
else:
    print("")

if you==1:
    choice1 = "ROCK"
elif you==2:
    choice1 = "PAPER"
elif you==3:
    choice1 ="SCISSORS"
else:
    print("")

print(f"you choosed {choice1} ")
print(f"computer choosed {choice2}")
game(you,comp)

