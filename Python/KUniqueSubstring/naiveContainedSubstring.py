inputString = input("Enter the string: ")
constraint = int(input("Enter the val of K: "))
result = 0
i,j = 0,0

while i <= j and i<len(inputString) and j<len(inputString):
    if len(set(inputString[i:j+1])) == constraint:
        result = max(result, len(inputString[i:j+1]))
        j += 1
    elif (len(set(inputString[i:j+1])) < constraint):
        j += 1
    else:
        i += 1
print(result)
        



# for i in range(len(inputString)):
#     for j in range(i, len(inputString)+1):
#         if len(set(inputString[i:j])) == constraint:
#             result = max(result, len(inputString[i:j]))
# print(result)