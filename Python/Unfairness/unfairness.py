arr =  list(map(int,input().rstrip().split(' ')))
k = int(input())

print(arr)
arr.sort()
index = 0
unfairness = arr[k-1] - arr[0]
for i in range(0,len(arr)-k):
    if unfairness > arr[i + k - 1] - arr[i]:
        unfairness = arr[i + k - 1] - arr[i]
        index = i
print(arr[index:index+k])
