#Buy and sell a stock twice based on prices given in a List.
def purchase(stockData):
    minSoFar = stockData[0]
    Forward = [0]
    for i in stockData:
        if(i<minSoFar):
            minSoFar = i
        Forward.append(max(i-minSoFar,Forward[-1]))
    maxProfit = max(Forward)
    print(Forward)

    maxSoFar = -float('inf')
    for i in range(len(stockData)-1,-1,-1):
        maxSoFar = max(maxSoFar, stockData[i])
        maxProfit = max(maxProfit, maxSoFar-stockData[i]+Forward[i])
    return(maxProfit)


stockData =  [310,337,275,260,270,290,230,255,250]
print(purchase(stockData))