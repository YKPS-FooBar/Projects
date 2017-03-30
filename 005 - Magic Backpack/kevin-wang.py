b = []
Backpack = b
print("Hello， well come to the Backpack. Here you can add or delete things in the backpack in order to creat your own personal backpack. \
\nThe things you can do：\
\n1.Type:[add xxx(no space) (the nth place you want the item at)] to add an item into the backpack.\
\n2.Type:[delete xxx(name)(no space)](this will delete the last term with the name xxx) or [delete xxx(nth term)(no space)] to delete an item from the backpack.\
\n3.Type:[Backpack] to show the things inside your backpack.\
\n4.Type:[help] to show the things you can do and the comman for them.")
while 1 == 1:
    i = input("\nType what you want to do:")
    if "add" in i:
        a = i.split()[1]
        f = i.split()
        if len(f) == 3:
            c = int(i.split()[2])
            d = c-1
            b.insert(d, a)
        elif len(f) == 2:
            b.append(a)
    if "delete" in i:
        e = i.split()[1]
        if e in b:
            b.remove(e)
        else:
            e = int(e)
            if len(b) >= e-1:
                b.remove(b[e-1])
            else:
                if len(b) == 1:
                    print("\nThere is only one term in the backpack, you cannot delete the",e,"term.")
                elif len(b) == 0:
                    print("\nThere is no term left in the backpack, you cannot delete the",e,"term.")
                else:
                    print("\nThere is only",len(b),"term left in the backpack, you cannot delete the",e,"term.")
    if "Backpack" in i:
        if len(b) == 0:
            print("\nThere is nothing inside.")
        else:
            print()
            print(*Backpack, sep=', ')
    if "backpack" in i:
        if len(b) == 0:
            print("\nThere is nothing inside.")
        else:
            print()
            print(*Backpack, sep=', ')
    if "help" in i:
        print("\n1.Type:[add xxx (the nth place you want the item at)] to add an item into the backpack.\
\n2.Type:[delete xxx (the nth place you want the item at)] to delete an item from the backpack.\
\n3.Type:[Backpack] to show the things inside your backpack.\
\n4.Type:[help] to show the things you can do and the comman for them.")
