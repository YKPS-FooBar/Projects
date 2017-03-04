import random
lowest_number=1 #enter the lowest number that you want others to guess
height_number=1000#enter the greatest number that you want others to guess
A=random.randint(lowest_number,height_number)
times=10 #enter the time you want other to guess
print("welcome to the 'guess the number'game!!!\n \n \nIn this game, you should guess a whole number from",lowest_number,"to",height_number," \n \n  ")
A_1=int(input("please enter a guess(numbers only):"))
for chance in range(times):
        if A_1 == A:
            print("well done!!!\n \n \nYou get the answer!")
            break
        if A_1 < A:
            print("\n \nGuess Higher\n \n \nYou have",times-chance,"chances left \n \n")
            A_1=int(input("please enter a guess(only a number):"))
        if A_1 > A:
            print("\n \nGuess Lower\n \n \nYou have",times-chance,"times chances \n \n")
            A_1=int(input("please enter a guess(only a number):"))
else:
    print("\n \n \nSorry,you out of chances\n \n \n")
