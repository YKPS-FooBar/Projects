n = int(input ('Input the nth term for the Fibonacci sequence: '))
fibo = [1,1]
while n not in fibo:
      fibo.append(fibo[-1])

print(fibo.index(x)+1)
