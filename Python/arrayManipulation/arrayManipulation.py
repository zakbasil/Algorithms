def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for i in queries:
        a, b, k = i
        arr[a] = arr[a] + k
        arr[b + 1] = arr[b + 1] - k

    curr = 0
    maxValue = 0
    for i in arr:
        curr = curr + i
        maxValue = max(curr, maxValue)

    return maxValue


n = 10
queries = [[1, 5, 3], [5, 8, 7], [6, 9, 1]]
print(arrayManipulation(n, queries))
