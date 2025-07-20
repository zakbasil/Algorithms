inputList = list(map(int, input("Enter the list: ").rstrip().split(' ')))
searchElement = int(input("Enter the search element: "))
found = False
for i in inputList:
    if i == searchElement:
        found = True
        print("Element found")
        break
if not found:
    print("Not found")
