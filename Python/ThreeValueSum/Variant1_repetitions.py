N = int(input())
arr = list(map(int, input().rstrip().split(' ')))

def twoSum(t):
    i,j = 0, len(arr) - 1
    while(i<=j):
        x = arr[i] + arr[j]
        if x == t:
            return(True)
        elif x < t:
            i += 1
        else:
            j -= 1 
    return(False)


def compute3VS():
    for i in arr:
        if twoSum(N-i):
            return(True)
    return(False)

arr.sort()
print(compute3VS())