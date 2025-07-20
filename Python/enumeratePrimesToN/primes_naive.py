n = int(input("Enter N: ").rstrip())
primes = [2]
for i in range(3,n+1,2):
    flag = 0
    for j in range(2, (i//2)+1):
        if (i%j == 0):
            flag = 1
    if flag == 0:
        primes.append(i)

print(primes)