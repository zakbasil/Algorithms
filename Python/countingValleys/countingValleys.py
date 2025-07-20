# numChars = int(input().rstrip())
strInput = str(input().rstrip())
countValley = 0
currentLevel = 0

for i in strInput:
    if i == 'D':
        currentLevel -= 1
    if i == 'U':
        currentLevel += 1
    if i == 'U' and currentLevel == 0:
        countValley += 1
print(countValley)
