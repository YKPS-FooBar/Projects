a = ['1', '2', '3']

while 1 ==1:
    print('These are the items in your backpack:', *a, sep=', ')
    print('You can either add, remove or print specific items in your backpack')
    s = (input('Please type in your command(add, remove, print): '))

    if s == 'add':
        i = input('What do you want to add into your backpack?')
        if i in a:
            print('This item already exists')
            print('')
        else:
            a.append(i)

    elif s == 'remove':
        i = input('Which item in your backpack do you want to remove?')
        if i in a:
            a.remove(i)
        else:
            print('This item does not exist')
            print('')
            
    elif s == 'print':
        i = int(input('Which item do you want to be printed?'))
        if i < len(a)+1:
            if i < 1:
                print('Please enter a positive number')
                print('')
            else:
                print(a[i-1])                    
        else:           
            print('This item does not exist')
            print('')
