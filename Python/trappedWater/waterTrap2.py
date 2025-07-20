t= list(map(int,input().rstrip().split(' ')))
n=len(t)
left=[t[0]]
right=[t[-1]]
for i in range(1,n):
    if t[i]>left[-1]:
        left.append(t[i])
    else:
        left.append(left[-1])

for i in range(n-2,-1,-1):
    if t[i]>right[0]:
        right.insert(0,t[i])
    else:
        right.insert(0,right[0])
water=0
for i in range(n):
    water+=min(left[i],right[i])-t[i]
print(water)