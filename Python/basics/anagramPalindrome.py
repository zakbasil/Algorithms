from collections import Counter
def checkPal(inpStr):
    countDict = dict(Counter(inpStr))
    print(countDict)
    summaryList = ['even' if i%2==0 else 'odd' for i in countDict.values()]
    if summaryList.count('odd')>1:
        return(False)
    return(True)

while(True):
    strInput = str(input("Enter a String: "))
    print(checkPal(strInput))