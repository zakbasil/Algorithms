def serachSortedArray(query,searchElement):
    result = -1

    start = 0
    end = len(query)

    while(start <= end):
        mid = (start + end)//2
        if(query[mid] == searchElement):
            result = mid
            break
        elif(query[mid] > searchElement):
            end = mid
        else:
            start = mid

    if(result>-1):
        while(True):
            if(query[result] == query[result-1]):
                result -= 1
            else:
                break
    return(result)


query = list(map(int,input("Enter the elements: ").rstrip().split(' ')))
searchElement = int(input("Enter the search element: "))
print(serachSortedArray(query,searchElement))