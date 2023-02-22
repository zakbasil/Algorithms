def newYear(q):
    bribes = 0
    for i in range(len(q)-1,-1,-1):
        if (q[i] - (i + 1) > 2):
            return("Too chaotic")
        for j in range(max(0,q[i]-2),i):
            print(q[i], q[j],i,j)
            if (q[j] > q[i]):
                bribes+=1
    return(bribes)

print(newYear([1,2,3,5,4,6,7,8])) #1
print(newYear([4,1,2,3])) #c
print(newYear([2, 1, 5, 3, 4])) #3
print(newYear([2, 5, 1, 3, 4])) #c

