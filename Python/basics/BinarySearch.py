inputList = list(map(int, input("Enter the list: ").rstrip().split(' ')))
searchElement = int(input("Enter the search element: "))

listLength = len(inputList)

start,end=0,listLength-1

while start<=end:
    mid = (start+end)//2

    if inputList[mid] == searchElement:
        print("Element Found")
        break
    elif inputList[mid] > searchElement:
        end = mid - 1
    else:
        start = mid + 1
if start > end:
    print("Element not found")