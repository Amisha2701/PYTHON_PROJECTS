import random
num=input("enter a number")
print(num)

if num.isdigit():
    num=int(num)

    if num is 0:
        print("please type number greater than 0 next time")
        quit()
else:
    print("type a number next time")
    quit()

random_number=random.randint(0,num)
count=0

while True:
    count += 1
    user_guess=input("guess the number: ")

    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("please type a number next time")
        continue

    if user_guess==random_number:
        print("u are correct")
        break
    else:
        print("your guess is not right try again")

print("total number of guesses were"+ str(count)+"only ")


    
