import random

user_wins=0
computer_wins=0

options=["stone","paper","scissor"]

while True:
    user_input=input(" Type stone/paper/scissor or Q to quit ").lower()
    if user_input=='Q':
        break

    if user_input not in options:
        continue

    random_number =random.randint(0,2)
    #rock:0, paper:1, scissor:2
    computer_pick=options[random_number]
    print("computer picked" , computer_pick+".")

    if user_input=="stone" and computer_pick=="scissor":
        print("you won")
        user_wins+=1

    elif user_input=="paper" and computer_pick=="stoneQ":
        print("you won")
        user_wins+=1

    elif user_input=="scissor" and computer_pick=="paper":
        print("you won")
        user_wins+=1
    else:
        print("you lost")
        computer_wins+=1

print(" you won", user_wins+ "times. ")
print("the computer won"+computer_wins+ ".")
print("goodbye")        
