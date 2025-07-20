def getWays(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin] 
    return dp[amount]

print(getWays(3,[1,2,3]))

