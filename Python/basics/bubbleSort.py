inputList = list(map(int, input("Enter the list: ").rstrip().split(' ')))

for i in range(len(inputList)-1):
    for j in range(i,len(inputList)):
        if inputList[i]> inputList[j]:
            inputList[i],inputList[j] = inputList[j],inputList[i]

print(inputList)