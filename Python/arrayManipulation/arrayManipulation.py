def arrayManipulation(size, queries):
    arr = [0] * (size + 1)
    for i in queries:
        start, end, value = i
        arr[start] = arr[start] + value
        arr[end + 1] = arr[end + 1] - value

    accumulated = 0
    maxValue = 0
    for i in arr:
        accumulated = accumulated + i
        print(accumulated, end = ' ')
        maxValue = max(accumulated, maxValue)
    print()
    return maxValue


n = 10
queries = [[1, 5, 3], [5, 8, 7], [6, 9, 1]]
print(arrayManipulation(n, queries))

        