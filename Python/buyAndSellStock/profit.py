a=[1,7,6,5,4]
profit=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if profit<a[j]-a[i]:
            profit=a[j]-a[i]
print(profit)

