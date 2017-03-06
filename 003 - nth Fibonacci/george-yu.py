# Do not copy my code!

fibo = [1, 1]

n = int(input('n = '))

for i in range(2, n):
    fibo.append(fibo[i-1] + fibo[i-2])

print(fibo[n-1])
