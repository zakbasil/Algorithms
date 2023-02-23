def serachSortedArray(query,searchElement):
    result = None

    start = 0
    end = len(query)

    while(True):
        mid = (start + end)//2
        if(query[mid] == searchElement):
            result = mid
            break
        elif(query[mid] > searchElement):
            end = mid
        else:
            start = mid

    if(result):
        while(True):
            if(query[result] == query[result-1]):
                result -= 1
            else:
                break
    return(result)


query = list(map(int,input("Enter the elements: ").rstrip().split(' ')))
searchElement = int(input("Enter the search element: "))
print(serachSortedArray(query,searchElement))