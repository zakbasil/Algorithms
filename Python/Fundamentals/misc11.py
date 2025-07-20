s = "{}[()](){}"
stack = []
def match(s):
    for i in s:
        if i in '({[':
            stack.append(i)
        elif i == '}' and len(stack)!=0 and stack[-1] == '{':
            stack.pop()
        elif i == ')' and len(stack)!=0 and stack[-1] == '(':
            stack.pop()
        elif i == ']' and len(stack)!=0 and stack[-1] == '[':
            stack.pop()
        else:
            return("Mismatch")
    return("Matching" if len(stack)==0 else "Not Matching")

print(match(s))