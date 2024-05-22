fibDict = {1:0, 2:1}
def fibonacci(num):
    if (num<=0):
        print("invalid input ")
        
    elif (num==1):
        return 0
    
    elif (num==2):
        return 1
    
    else:
        if(num in list(fibDict.keys())):
            return(fibDict[num])
        else:
            fibDict[num] = fibonacci(num-1)+fibonacci(num-2)
            return(fibDict[num])

k = int(input("Enter a number:"))
print("kth term is",fibonacci(k))