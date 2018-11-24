# Do 'fibo = [1]*2' instead ;)
fibo = [1,1]

# SPAGHETTI!!!
n = int(input("."))
if n == 1:
    print("1 or 2")
else:
    while n > fibo[-1]:
        fibo.append(fibo[-1]+fibo[-2])
    if n == fibo[-1]:
        print(fibo.index(n)+1)
    else:
        print(".")
