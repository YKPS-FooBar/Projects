import random

aw=random.randint(1,100)
a=int(0)
while aw==aw:
    n=float(input('guess a numer between 1-100'))
    if a<3:
        if n==aw:
            print('Right')
            break
        elif n<aw:
            print('Try again, guess a bigger number')
            a=int(a+1)
        else:
            print('Try again, guess a smaller number')
            a=int(a+1)
    else:
        print('You Lose!! The anwser is')
        print(aw)
        break

