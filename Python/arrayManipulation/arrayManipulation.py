
def arrayManipulation(n, queries):
    arr = [0]*n
    for i in queries:
        a,b,k = i
        arr[a] = arr[a]+k
        arr[b] = arr[b]-k
    
    curr = 0
    maxValue = 0
    for i in arr:
        curr = curr + i
        maxValue = max(curr,maxValue)
    
    return maxValue

n = 10
queries = [[1,2,100],[2,5,100],[3,4,100]]
print(arrayManipulation(n,queries))