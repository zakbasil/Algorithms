target=[1,5,10]
drops=[3,7]

devastation=[max(abs(max(drops)-min(target)),abs(max(target)-min(drops)))]*len(target)
for i in drops:
    for j in range(0,len(target)):
        if devastation[j]> abs(i-target[j]):
            devastation[j]=abs(i-target[j])
print(max(devastation))