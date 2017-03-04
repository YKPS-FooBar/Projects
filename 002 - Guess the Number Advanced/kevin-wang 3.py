import random
lowest_number=1 #enter the lowest number that you want others to guess
height_number=1#enter the greatest number that you want others to guess
A=random.randint(lowest_number,height_number)
times=10 #enter the time you want other to guess
print("welcome to the 'guess the number'game!!!\n \n \n \nIn this game, you should guess a whole number from",lowest_number,"to",height_number," \n \n \n  ")
for chance in range(times):
    print("Now, you have",times-chance,"chances left \n \n \n")
    A_1=int(input("please enter a guess(numbers only):"))
    if A_1 > A:
        print("\n \n \nGuess lower\n \n \n")
    elif A_1 < A:
        print("\n \n \nGuess higher\n \n \n")
    else:
        print("well done!!!\n \n \n \nYou get the answer!")
        break
else:
    print("Sorry,you out of chances\n \n \n")
