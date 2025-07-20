from collections import Counter
N = input()
C = Counter(N)
OddChar = 0

for i in C.values():
    if i%2 == 1:
        OddChar += 1

if OddChar > 1:
    print('False')
else:
    print('True')