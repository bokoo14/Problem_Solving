def getWays(n, c):
    dp = [0] * (n+1)
    for coin in c:
        print(coin)
        for i in range(1, n+1):
            if coin == i:
                dp[i] += 1
            elif i-coin >= 0:
                dp[i] += dp[i-coin]
        print(*dp)

    print(*dp)
    return dp[-1]

print(getWays(10, [2, 5, 3, 6]))
