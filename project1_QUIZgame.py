print("Welcome to the quiz game")

playing=input("Do you wanna play?")
print(playing)

if playing.lower()!= "yes":
    quit()
   
print("ok lets continue :) ")
score=0

print("your first question is :")
question=input("what is the full form of the CPU : ")
print(question)
if question.lower()=="central processing unit":
    print("corrrect")
    score +=1
else:
    print("incorrect")

print("your second  question is :")
question=input("what is the full form of the ROM : ")
print(question)
if question.lower()=="read only memory":
    print("corrrect")
    score +=1
else:
    print("incorrect")

print("your third question is :")
question=input("what is the full form of the RAM : ")
print(question)
if question.lower()=="random access memory":
    print("corrrect")
    score +=1
else:
    print("incorrect")

print("your fourth question is :")
question=input("what is the full form of the PC : ")
print(question)
if question.lower()=="personal computer":
    print("corrrect")
    score +=1
else:
    print("incorrect")

print("your fifth  question is :")
question=input("what is the full form of the EPROM: ")
print(question)
if question.lower()=="erasable programmable read only memory":
    print("corrrect")
    score +=1
else:
    print("incorrect")

print("you got "+ str(score) + " correct")
print("your percentage is "+str((score/5)*100)+ "%")
