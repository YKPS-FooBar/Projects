import random
a = random.randint(0,10)
count = 1
guess = int(input("Please guess a number between 1 and 10:"))
if guess == a:
    print("Correct")
            
while guess != a:
    print("You are wrong")
    count = count + 1
    guess = int(input("Please guess a number between 1 and 10:"))
    if guess == a:
        print("Correct")
    if count == 5:
        break
