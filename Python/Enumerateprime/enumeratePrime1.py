def eliminate(i):
    for i in range(i, N+1, i):
        isPrime[i] = False

N = int(input())
isPrime = [True]*(N+1)
isPrime[0] = False
isPrime[1] = False
for i in range(2,N+1):
    if isPrime[i]:
        print(i, end = ' ')
        eliminate(i)
