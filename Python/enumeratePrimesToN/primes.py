#enumerating primes in a moderate speed by trial method O(nloglogn)
def primesTo(n):
    primes = []
    isPrime = [True]*(n+1)
    isPrime[0] = isPrime[1] = False

    for i in range(2,n+1):
        if(isPrime[i]):
            primes.append(i)
            for k in range(i,n+1,i):
                isPrime[k] = False
    return(primes)


#enumerating primes in a moderate speed by trial method by adding a sieve of p^2 O(nloglogn) but optimized the factors allowing faster execution
def fasterPrimesTo(n):
    size = int(0.5*(n-3)) + 1
    primes = [2]
    isPrime = [True]*(n+1)
    for i in range(0,size):
        if(isPrime[i]):
            p = (i*2) +3
            primes.append(p)
            for k in range((2*i*i + 6*i + 3), size,p):
                isPrime[k] = False

    return(primes)

#slow method
# print(len(primesTo(100000000)))

#faster
print(len(fasterPrimesTo(100000000)))
