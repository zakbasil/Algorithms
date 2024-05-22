s1 = 'dcab'
s2 = 'abcd'

def counter(s):
    dictCounter = {}
    for i in s:
        if i not in dictCounter.keys():
            dictCounter[i] = 1
        else:
            dictCounter[i] += 1
    return(dictCounter)


if counter(s1) == counter(s2):
    print('Anagram')
else:
    print('Not anagram')