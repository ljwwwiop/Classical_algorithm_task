'''
    经典硬币问题
    LeetCode - mid - 322
    LeetCode - mid - 518
'''
'''
    输入: coins = [1, 2, 5], amount = 11
    输出: 3 
    解释: 11 = 5 + 5 + 1
'''
def coinChange(coins,amount):
    # 可以DP/DFS
    dp = [float("INF")] * (amount+1)
    dp[0] = 0
    for i in range(1,amount+1):
        for coin in coins:
            if i>= coin:
                dp[i] = min(dp[i],dp[i-coin] + 1)
    return dp[-1] if dp[-1] != float("INF") else -1
coins = [1, 2, 5]
amount = 24
print(coinChange(coins,amount))

'''
    经典 0 - 1问题
    输入: amount = 5, coins = [1, 2, 5]
    输出: 4
    解释: 有四种方式可以凑成总金额:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1
'''
# 二维数组解决
# dp[i][j] -> 一个代表硬币，一个代表当前硬币最少的数量
def change(amount,coins):
    n = len(coins)
    dp = [[0]*(amount+1) for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(1,n+1):
        dp[i][0] = 1
        for j in range(1,amount+1):
            if j - coins[i-1] >= 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)
    return dp[-1][-1]

amount2 = 8
coins2 = [1,2,5]
print(change(amount2,coins2))





