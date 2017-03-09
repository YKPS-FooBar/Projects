Fibonacci Sequence
n = int(input ('Input the nth term for the Fibonacci sequence: '))
x = [1,1]
for i in range (2,n):
      x.append(x[i-1]+x[i-2])
print (x[n-1])
