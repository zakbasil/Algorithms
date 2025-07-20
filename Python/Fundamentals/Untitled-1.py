def chk(lst1,lst2):
    intrs = set(lst1) & set(lst2)
    uniq = list(intrs)
    return intrs, uniq

l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]
print(chk(l1,l2))