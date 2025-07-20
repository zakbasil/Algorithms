
def profit(stockData):
    minVal, maxProfit = float('inf'),0
    forwardProfit = [0]
    for i in stockData:
        minVal = min(minVal, i)
        maxProfit = max(maxProfit, i - minVal)
        forwardProfit.append(max(forwardProfit[-1], maxProfit))
    
    maxSoFar = -float('inf')
    for i in range(len(stockData)-1,-1,-1):
        maxSoFar = max(maxSoFar, stockData[i])
        maxProfit = max(maxProfit, maxSoFar-stockData[i]+forwardProfit[i])
        print(maxProfit)
    return(maxProfit)




stocks = [310,315,275,260,270,290,230,255,250]
print(profit(stocks))