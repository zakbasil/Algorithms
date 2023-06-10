def match(query):
    stack = []
    count = 0
    if(len(query)==0):
        return("Empty input provided.")
    for i in query:
        if(i == '{'):
            stack.append('{')
        elif(i == '['):
            stack.append('[')
        elif(i == '('):
            stack.append('(')
        elif(i == '}' and len(stack) != 0 and stack[-1] == '{'):
            stack.pop(-1)
        elif(i == ')' and len(stack) != 0 and stack[-1] == '('):
            stack.pop(-1)
        elif(i == ']' and len(stack) != 0 and stack[-1] == '['):
            stack.pop(-1)
        else:
            return("Not matching")
        
    return("matching" if len(stack) ==0 else "not matching")


while(True):
    query = str(input("Enter the string: "))
    print(match(query))