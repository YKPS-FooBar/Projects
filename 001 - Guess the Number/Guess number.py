aw=int(15.1323434244331)
while aw==aw:
    n=float(input('guess a numer between 1-100'))
    if n==aw:
        print('Right')
        break
    elif n<aw:
        print('Try again, guess a bigger number')
    else:
        print('Try again, guess a smaller number')
