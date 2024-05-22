# n = str(input())
# k = int(input())

n = "aabbcc"
k = 2

n = "aabacbebebe"   
k = 3

str1 = input().rstrip()
k = int(input().rstrip())

i = 0
j = 1
maxLen = 0
while(i<=j and i<len(n) and j<=len(n)):
    print(n[i:j])
    chars = len(set(n[i:j]))
    if (chars == k and maxLen < len(n[i:j])):
        maxLen = len(n[i:j])
    elif(chars < k): 
        j += 1
    elif(chars > k):
        i += 1
    else:
        j+=1
print(maxLen)

