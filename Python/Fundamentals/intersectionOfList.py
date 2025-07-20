def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

list1 = list(map(int, input().rstrip().split(' ')))
list2 = list(map(int, input().rstrip().split(' ')))

print(intersection(list1, list2))

print(set(list1).intersection(set(list2)))

print(set(list1) & set(list2))