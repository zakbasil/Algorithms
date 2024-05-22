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


query = str(input("Enter the string: "))
print(match(query))

count = 0
if { count ++
if } count --
    

{ } { }
1 0 1 0

{ } }  {
1 0 -1 0

{ { {
1 2 3

{ } }
1 0 -1

{ { { } } }
1 2 3 2 1 0


