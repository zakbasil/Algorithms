from collections import Counter
n = input("Enter the string")
counterDict = Counter(n)
countOddChars = 0
for i in counterDict.values():
    if i % 2 == 1:
        countOddChars += 1
if countOddChars > 1:
    print("No")
else:
    print("yes")