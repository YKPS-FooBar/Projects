NAME=input("enter your name:")
print("Hello",NAME,", well come to the true or false game.   \n \nToday, we are going to answer five questions, if they are all correct, then you win the game.    \n \nIf not, you lost.\n \n")
print("Question_1: What is the ture answer of 1*1+2*3? \n")
Answer_1=input('enter your answer:')
if Answer_1 == "7":
        print("\n \n \nWell done",NAME,"!!! \n \n \n \n \nNow, the second question is comming\n \nQuestion_2:What is the sum of 273*124?\n ")
else:
        print("\n\n\n",NAME,",you Lost!!!!!!!!!!")
        exit(1)
Answer_2=input("enter your anwser:")
if Answer_2 == "33852":
        print("\n \n \nGreat",NAME,"!!! \nNow \nQuestion_3: Which number is wrong in the following: \n2,3,5,7,11,12 \n")
else:
        print("\n \n \nSorry, you are wrong. \n \n \n      -_- \n \n \n \n")
        exit(1)
Answer_3=input("enter your anwser:")
if Answer_3 == "12":
        print("\n \n \nFantasic!! \nThen \nQuestion_4:f(x)=X^2+2*12 \nFind the value of f(4) \n")
else:
        print("\n \n \n",NAME,", you are nearly there... \n Try harder next time.")
        exit(1)
Answer_4=input("enter your anwser:")
if Answer_4 == "40":
        print("\n \n \nWell Play!!!!!!!!!! \n \nFinally you reach the last question:Is one a real number?(type 'Yes'or'No')")
else:
        print("\n \n \n",NAME,", the bad news is that you didn't pass the game. \nTry next time.")
        exit(1)
Answer_5=input("enter your answer:")

if Answer_5 == "Yes" or Answer_5 == "yes":
        print("\n \n \nCongratulation!!!",NAME,"You Passed The Game!!! \n \n \n \n:) \n \n \now, you can close the game.")
else:
        print("\n \n \n",NAME,", you didn't win the game.")
        exit(1)
