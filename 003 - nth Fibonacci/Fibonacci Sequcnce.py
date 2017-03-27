nterms = int(input('nth term？'))
n1 = 0
n2 = 1
count = 2
print('斐波那契数列：')
if nterms<=1:
    print(n2)
elif nterms==2:
    print(n2+n2)
else:
    while count < nterms:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
print(nth,end=" , ")

fibo = [1,1]
n=5
for i in range(2,n):
    fibo.append(fibo[i-1]+fibo[i-2])
print(fibo)
