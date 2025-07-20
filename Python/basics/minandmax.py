arr = list(map(int, input().split(' ')))
minVal = float('inf')
maxVal = -float('inf')

for i in arr:
    minVal =  min(minVal, i)
    maxVal = max(maxVal, i)

print(minVal, maxVal)