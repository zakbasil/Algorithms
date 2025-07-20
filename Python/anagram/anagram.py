s1 = 'dcabd'
s2 = 'abcdd'

# from collections import Counter
# if Counter(s1) == Counter(s2):
#     print('Anagram')
# else:
#     print('Not anagram')


def counter(s):
    dictCounter = {}
    for i in set(s):
        dictCounter[i] = 0
    
    for i in s:
        dictCounter[i] += 1
    return(dictCounter)


if counter(s1) == counter(s2):
    print('Anagram')
else:
    print('Not anagram')

print(counter(s1))
print(counter(s2))