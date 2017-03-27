#list

list=['q','w','e','r']
while 1==1:
    add=input("What do you want to do? Add/Delete/Print all/specific item")
    if add=='Add':
        i=input('Which item do you want to add?')
        list.append(i)
        if list.count(i)>1:
            list.remove(i)
            print('The item already exist, try again')
        else:
            print('Now the list include')
            print(','.join(list))

    elif add=='Delete':
        d=input('Which item do you want to delete?')
        if d in list:
            list.remove(d)
            print('Now the list inculde')
            print(','.join(list))
        else:
            print('Can not find the item, try again')

    elif add=='Print all':
        print(','.join(list))

    elif add=='specific item':
        k=int(input('Which one you want to find(specific nember)'))
        if k<(len(list)+1):
            print('The item you want to find is')
            print(list[k-1])
        elif k<1:
            print('Can not find the item, try again')
        else:
            print('Can not find the item, try again')
        
    else:
        print('Sorry I do not understant, please try again')
