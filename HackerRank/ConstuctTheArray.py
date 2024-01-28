def countArray(n, k, x):
    dp = [0, 0] * (n-1)
    dp[0][0], dp[1][0] = 1, 1
    
    for i in range(1, n-1):
        if x!=1: 
            if i == n-1: 
                dp[i][0] = dp[i-1][0]*(k-2)
            else: # 끝이 아닌 값
                dp[i][0] = dp[i-1]*(k-1)
        else: #맨끝 1이라면
            if i == n-1:
                dp[1][i] = dp[i-1]*(k-2)
            else:
                dp[1][i] = dp[i-1]*(k-1)
    
    return dp[-1] % (10**9+7)

print(countArray(4, 3, 2))