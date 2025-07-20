def match(query):
    count = 0
    if(len(query)==0):
        return("Empty input provided.")
    for i in query:
        if(i == '{'):
            count += 1
        elif(i == '}'):
            count -= 1
        else:
            return("Unknown character encountered.")
        
        if(count < 0):
            return("Not matching")
    
    if(count == 0):
        return("Matching")
    else:
        return("Not matching")

while True:
    query = str(input("Enter the string: "))
    print(match(query))