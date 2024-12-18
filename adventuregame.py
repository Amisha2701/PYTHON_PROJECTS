name=input("enter your name ")
print("welcome",name+" to this adventure game")

answer=input("you are on a dirt road , it has came to an end and you can go either left or rignt. What whould you like to choose " ).lower()

if answer == "left":
    answer=input("you come to a river, you can walk around it or swim across. type walk to walk and swim to swim ")

    if answer=="swim":
        print("you swam across and were eaten by a crocodile and you loose ")
    elif answer=="walk":
        print("you walked really long and came end to the road, and you lost the game ")
    else:
        print("not a valid option , you loose")

elif answer=="right":
    answer=input("you came across a bridge, it looks scary, do you want to cross it? press cross to cross it and back to go back. ")

    if answer == "back":
        print("ohhh shit !! you got scared no worries will take u back but you will lose ")
    elif answer == "cross":
        answer=input("oh nicee!! you are quite adventorous now lets cross the bridge together. You met a stranger here do you wanna talk ?? type yes for yes and no for no: ").lower()
        if answer=="yes":
            print("you talked to stranger and they gave you gold and you won ")
        elif answer=="no":
            print("you didnt talk to stranger thats why u losse ")
        else:
            print("not a valid option and you loose ")
    else:
        print("not a valid option and you loose")
else:
    print("not a valid option and you loose.")
