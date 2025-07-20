height = [3,0,0,5,0,4]
stack = []
n = len(height)
ans = 0

for i in range(n):
    while( len(stack)!=0 and height[stack[-1]] < height[i]):
        poppedHeight = height[stack[-1]]
        stack.pop()
        if len(stack) == 0:
            break
        distance = i - stack[-1] - 1 
        minHeight = min(height[stack[-1]],height[i])-poppedHeight
        ans += distance * minHeight
    stack.append(i)

print(ans)
