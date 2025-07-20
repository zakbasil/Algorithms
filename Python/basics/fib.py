import sys
sys.setrecursionlimit(1000000)

fiboDictionary = {0:1,1:1}
def fib(n):
    if n <=1:
        return(n)
    else:
        if n in fiboDictionary.keys():
            return(fiboDictionary[n])
        else:
            fiboDictionary[n] = fib(n-1) + fib(n-2) 
            return( fiboDictionary[n])
    
n = int(input())
print(fib(n))