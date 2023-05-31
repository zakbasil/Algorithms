#Buy and sell a stock twice based on prices given in a List.
def purchase(stockData):
    temp = stockData[0]
    result = [0]
    for i in stockData:
        if(i<temp):
            temp = i
        result.append(max(i-temp,result[-1]))
    maxProfit = max(result)

    maxSoFar = -10000
    for i in range(len(stockData)-1,-1,-1):
        maxSoFar = max(maxSoFar, stockData[i])
        print(maxSoFar)
        finalResult = max(maxProfit, maxSoFar-stockData[i]+result[i-1])

    return(finalResult)


stockData = [12,11,13,9,12,8,14,13,15]
print(purchase(stockData))