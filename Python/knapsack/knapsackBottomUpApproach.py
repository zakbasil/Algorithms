def knapSack(W, wt, val, n):
    dp = [0 for i in range(W+1)]
    for i in range(0, n):      
        for w in range(W, 0, -1):
            print(dp)
            if wt[i] <= w:                
                dp[w] = max(dp[w], dp[w-wt[i]]+val[i])
    return dp[W]


if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
    print(knapSack(W, weight, profit, n))