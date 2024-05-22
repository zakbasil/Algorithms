height = [3,0,2,0,4]
stack = []
n = len(height)
ans = 0

for i in range(n):
    while( len(stack)!=0 and height[stack[-1]] < height[i]):
        popH = height[stack[-1]]
        stack.pop()
        if len(stack) == 0:
            break
        distance = i - stack[-1] - 1
        minH = min(height[stack[-1]],height[i])-popH
        ans += distance * minH
        print(ans,popH,minH,distance)
    stack.append(i)
    print(stack)
print(ans)
