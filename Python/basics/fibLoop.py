n = int(input())
a,b = 0,1
for _ in range(n):
    res = a+b
    a = b
    b = res

print(res)