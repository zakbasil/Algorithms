def checkRange(targets, drops,radius):
    lenDrops = len(drops)
    for target in targets:
        undestroyed = 0
        for drop in drops:
            if (abs(target - drop)>radius):
                 undestroyed += 1
            else:
                undestroyed -= 1
        if undestroyed==lenDrops:
            return(False)
    return(True)

def calculate(targets, drops):
    maxRad = 100000000
    minRad = 0
    lastTrueRadius = maxRad
    while maxRad >= minRad:
        mid = (minRad + maxRad)//2
        if checkRange(targets, drops, mid):
            lastTrueRadius = mid
            maxRad = mid - 1
        else:
            minRad = mid + 1
    return(lastTrueRadius)


targets = [2, 5, 10]
drops = [3, 7]
print(calculate(targets, drops))