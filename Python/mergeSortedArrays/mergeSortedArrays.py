def merge(query1,query2):
    result = []
    len1 = len(query1)
    len2 = len(query2)
    i,j = 0,0
    while(i<len1 and j<len2):
        if(query1[i]<=query2[j]):
            result.append(query1[i])
            i += 1
        else:
            result.append(query2[j])
            j += 1
    if(j<len2):
        result += query2[j:]
    if(i<len1):
        result += query1[i:]
    
    return(result)


query1 = list(map(int,input("Enter the Data: ").rstrip().split(' ')))
query2 = list(map(int,input("Enter the Data: ").rstrip().split(' ')))
print(merge(query1,query2))