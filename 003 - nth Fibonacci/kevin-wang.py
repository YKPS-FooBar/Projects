f=[1,1]
n=int(input("the nth number in the Fibonacci Sequence:"))
for i in range(2,n):
    f.append(f[i-1]+f[i-2])
print("\n \n \n \nThe answer is:",f[n-1])
