def minMax(k, arr):
    arr.sort()
    unfairness = arr[k-1] - arr[0]

    for i in range(0,len(arr)-k+1):
        if (unfairness > arr[i+k-1]-arr[i]):
            unfairness = arr[i+k-1]-arr[i]
    return(unfairness)


k = int(input("Enter size of subarray:"))
arr = list(map(int,input("Enter elements: ").rstrip().split(' ')))
print(minMax(k,arr))