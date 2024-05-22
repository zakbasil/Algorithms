#Buy and sell a stock once based on prices given in a List.
#Find the difference between the lowest traversed value and store the max profit value
def purchase(stockData):
    temp = stockData[0]
    result = 0
    for i in stockData:
        if(i<temp):
            temp = i
        if(result<(i-temp)):
            result = i-temp
    return(result)


stockData = [310,315,275,260,270,290,230,255,250]
print(purchase(stockData))