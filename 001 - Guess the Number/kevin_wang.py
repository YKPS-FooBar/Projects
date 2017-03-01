A=int(input(enter a number you want other to guess(only a number):))
print("welcome to the 'guess the number'game!!!\n \n \n ")
A_1=int(input("please enter a guess(only a number):"))
while 1==1:
    if A_1 == A:
        print("well done!!!\n \n \nYou get the answer!")
        break
    if A_1 < A:
        print("\n \n \nHigher\n \n \n")
        A_1=int(input("please enter a guess(only a number):"))
    if A_1 > A:
        print("\n \n \nLower\n \n \n")
        A_1=int(input("please enter a guess(only a number):"))
