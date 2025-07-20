arr = list(map(int, input().split(' ')))

maxVal = -float('inf')
secLarge = -float('inf')
for i in arr:
    if maxVal < i:
        secLarge = maxVal
        maxVal = i

print(secLarge)