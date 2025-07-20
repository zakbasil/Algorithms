#Buy and sell a stock once based on prices given in a List.
#Find the difference between the lowest traversed value and store the max profit value
def purchase(stockData):
    currMin = stockData[0] #230
    maxProfit = 0 # 30
    for i in stockData: #i = 250
        if(i<currMin):
            currMin = i
        if(maxProfit<(i-currMin)):
            maxProfit = i-currMin
    return(maxProfit) 


stockData = [215, 265, 250, 200, 240, 260, 230]
print(purchase(stockData))