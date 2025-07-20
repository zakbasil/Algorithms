def merge(a, b):
    n1 = len(a)
    n2 = len(b)
    res = []
    i = 0
    j = 0
    while i < n1 and j < n2:
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    if i < n1:
        res.extend(a[i:])
    
    if j < n2:
        res.extend(b[j:])
    
    return(res)

A = list(map(int, input("A: ").rstrip().split(' ')))
B = list(map(int, input("B: ").rstrip().split(' ')))
print(merge(A, B))

