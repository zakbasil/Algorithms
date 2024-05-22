numChars = int(input().rstrip())
strInput = str(input().rstrip())

countValley = 0
currentLevel = 0
for i in strInput:
    temp = currentLevel
    if i == 'D':
        currentLevel -= 1
    if i == 'U':
        currentLevel += 1
    
    if temp == -1 and currentLevel == 0:
        countValley += 1

print(countValley)


{ } { }
1 0 1 0

{ }  }  {
1 0 -1 0

{ { { } } }
1 2 3 2 1 0


{ { {
1 2 3