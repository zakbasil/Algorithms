def minmax(l):
    largest = l[0]
    smallest = l[0]

    for i in l:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
    return(smallest, largest)


def secondLargest(l):
    largest = 0
    sl = 0
    for i in l:
       if i > largest:
           sl = largest
           largest = i
    return(sl)


listInput = list(map(int, input().rstrip().split(' ')))
print(secondLargest(listInput))
# print(minmax(listInput))