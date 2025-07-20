def perform(n, pegs,frompeg, topeg, usepeg):
    if n > 0:
        perform(n-1, pegs,frompeg, usepeg, topeg)
        pegs[topeg].append(pegs[frompeg][-1])
        pegs[frompeg].pop()
        print("Move from", frompeg, "to peg", topeg)
        # print(pegs)
        perform(n-1, pegs, usepeg, topeg, frompeg)

pegs = [[],[],[]]
n = int(input("number of rings: "))
pegs[0] = [i for i in range(n,0,-1)]
print(pegs)
perform(n, pegs, 0,1,2)
