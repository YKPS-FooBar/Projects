b = []
Backpack = b
print("Hello， well come to the Backpack. Here you can add or delete things in the backpack in order to creat your own personal backpack. \
\nThe things you can do：\
\n1.Type:[add xxx (the nth place you want the item at)] to add an item into the backpack.\
\n2.Type:[delete xxx(name)] or [delete xxx(nth term)] to delete an item from the backpack.\
\n3.Type:[Backpack] to show the things inside your backpack.\
\n4.Type:[help] to show the things you can do and the comman for them.")
while 1 == 1:
    i = input("\nType what you want to do:")
    if "add" in i:
        a = i.split()[1]
        c = int(i.split()[2])
        d = c-1
        b.insert(d, a)
    if "delete" in i:
        e = i.split()[1]
        if e in b:
            b.revome(e)
        else:
            e = int(e)
            if len(b) >= e-1:
                b.remove(b[e-1])
            else:
                if len(b) == 1:
                    print("\nThere is only one term in the backpack, you cannot delete the",e,"term.")
                elif len(b) == 0:
                    print("There is no term left in the backpack, you cannot delete the",e,"term.")
                else:
                    print("There is only",len(b),"term left in the backpack, you cannot delete the",e,"term.")
    if "Backpack" in i:
        print()
        print(*Backpack, sep=', ')
    if "help" in i:
        print("\n1.Type:[add xxx (the nth place you want the item at)] to add an item into the backpack.\
\n2.Type:[delete xxx (the nth place you want the item at)] to delete an item from the backpack.\
\n3.Type:[Backpack] to show the things inside your backpack.\
\n4.Type:[help] to show the things you can do and the comman for them.")
