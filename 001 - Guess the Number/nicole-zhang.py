a = 3
guess = int(input("Please guess a number between 1 and 10:"))
if guess == a:
    print("Correct")
            
while guess != a:
    print("You are wrong")
    guess = int(input("Please guess a number between 1 and 10:"))
    if guess == a:
        print("Correct")
        break
