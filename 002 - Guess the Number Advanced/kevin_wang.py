import random
A=random.randint(1,1000)
times=5 #enter the time you want other to guess
print("welcome to the 'guess the number'game!!!\n \n \n ")
A_1=int(input("please enter a guess(only a number):"))
for chance in range(times):
        if A_1 == A:
            print("well done!!!\n \n \nYou get the answer!")
            break
        if A_1 < A:
            print("\n \n \nHigher\n \n \n")
            A_1=int(input("please enter a guess(only a number):"))
        if A_1 > A:
            print("\n \n \nLower\n \n \n")
            A_1=int(input("please enter a guess(only a number):"))
else:
    print("\n \n \nSorry,you out of chances\n \n \n")
