
'''
    DP -> 问题
        1 石子合并问题: 
        input: 4 ,[4,4,5,9]
        output: 43,54
        2 最少硬币问题:
        input:[1,2,5] ,18
        output: 5
'''
'''
    第一题：本质就是子问题的求解，寻找到最小最大的答案.
    输入：4,4,5,9
    输出：43,54
    难点：将环转换切换到直线，状态dp的设计，滑动窗口的大小n。
    环切换到直线：n -> 2*n-1 
        [4,4,5,9] -> [4,4,5,9,4,4,5]
    前缀和数组：
        这样 i - j的sum可以直接被差分表示出来Sum[j] - Sum[i],i->j本身的消耗
        [0, 4, 8, 13, 22, 26, 30, 35, 0, 0, 0]
    状态设计：
        1 dp[i][j] -> 表示从i堆合并到j堆的最小花费/最大花费
            例如：dp[1][3] 从第1个堆到第3个堆的最小花费
                ：dp[3][1] 从第3个堆到,4,5..n,0,1个堆的最小花费
        2 dp[i][j]：i == j 时候 dp[i][j] == 0
        3 dp[i][j]的行列：行就是我们的直线当前且分点，列就是2*n，确保能形成一个滑动窗口。
            4 4 5 9 4 4 5 9
          4 0 8 21 43 ...
          4   0
          5
          9
          4
          4
          5
        dp[1][1] = 0
        dp[1][2] = min(dp[1][2],dp[1][1]+dp[2][2]+sum[2] - sum[0]) = 8
        dp[1][3] = min(dp[1][3],dp[1][1]+dp[2][3] + sum[3] - sum[0]) = inf
                 = min(dp[1][3],dp[1][2]+dp[3][3] + sum[3] - sum[0]) = 8 + 13 = 21
        dp[1][4] = min(dp[1][4],dp[1][1]+dp[2][4] + sum[4] - sum[0]) = inf
                 = min(dp[1][4],dp[1][2] + dp[3][4] + sum[4] - sum[0]) = inf
                 = min(dp[1][4],dp[1][3] + dp[4][4] + sum[4] - sum[0]) = 21 + 22 = 43
        故可以直接推导下来,注意dp的大小设计，主要考虑最后一行延申出去多少
            延申出去 n -2 + 1
        
'''

def stoneMerge(n,nums):
    ans = [0]*(2*n+1)
    for i in range(n):
        ans[i] = nums[i]
        
    for i in range(n,2*n):
        ans[i] = nums[i-n]
    # print(ans)

    Sum = [0]*(3*n-1)
    for i in range(1,2*n):
        Sum[i] = Sum[i-1] + ans[i-1]

    # print("Sum : ",Sum)
    min_dp = [[float("inf")]*(3*n-1) for _ in range(3*n - 1)]
    max_dp = [[0]*(3*n-1) for _ in range(3*n - 1)]

    # 初始化对角线
    for i in range(len(min_dp)):
        min_dp[i][i] = 0
    
    for i in range(1,2*n):
        for j in range(i+1,i+n):
            s = Sum[j] - Sum[i-1]
            for k in range(i,j):
                max_dp[i][j] = max(max_dp[i][j],max_dp[i][k]+max_dp[k+1][j] + s)
                min_dp[i][j] = min(min_dp[i][j],min_dp[i][k]+min_dp[k+1][j] + s)

    # for i in range(len(min_dp[0])):
    #     print(min_dp[i])

    minValue = float("inf")
    maxValue = 0
    for i in range(1,n):
        minValue = min(minValue, min_dp[i][i+n-1])
        maxValue = max(maxValue, max_dp[i][i + n - 1])
    print(minValue,maxValue)

'''
    典型 0 - 1 背包问题：本质就是0-1背包问题，切勿当作贪心去做了。
    输入：1，2，5
    求解问题：18 -> 既然求18 不如选择从17，选择17不如16...,1开始推导，所以我们只需要知道前一个所用最少零钱兑换的方法就可以知道下一个最少的方法
        dp = []*19,dp[0] = 0,dp[18] 最后一个返回值
        dp[0] = 0
        dp[1] = 1 
        dp[2]：注意这个时候coins,可以用1，也可以用2
                = min(dp[2],dp[2 - 1] + 1) = 2
                = min(dp[2],dp[2-2]+1) = 1
                故dp[2] = 1
        dp[3]：同理coins:1,2
                = min(dp[3],dp[3-1]+1) = 2
                = min(dp[3],dp[3-2]+1) = 2
                dp[3] = 2
        dp[4]：...同理 = 2
        dp[5]：这时候coins：可以使用1，2，5
                = min(dp[5],dp[5-1] + 1) = 3
                = min(3,dp[5-2]+1) = 3
                = min(3,dp[5-5]+1) = 1
        ...所以后面同理
        硬币问题比较经典的dp思想，由下往上推导的过程，只需要前面每一步最优，就保证了后面每一步最优。
'''

# dp 时间复杂度为：n*m,m<n
def coinChange(coins,amount):
    dp = [float("inf")]*(amount+1)
    dp[0] = 0

    # 把所用的硬币存储起来,最后和Nums比较
    for i in range(1,amount+1):
        for coin in coins:
            if i - coin>=0 :
                dp[i] = min(dp[i],dp[i-coin] + 1)

    print(dp)
    return dp[-1] if dp[-1]!=float("inf") else -1

# bfs
def coinChange2(coins,amount):
    queue = [amount]
    step = 0
    visited = set()
    while queue:
        n = len(queue)
        for _ in range(n):
            temp = queue.pop(0)
            if temp == 0:
                return step
            for coin in coins:
                if temp>= coin and temp - coin not in visited:
                    visited.add(temp - coin)
                    queue.append(temp - coin)
        step+=1
    return -1

def coinChange3(Coins,amount,T):
    # 数量控制，这点还不太一样
    dp = [float("inf")]*(amount+1)
    dp[0] = 0
    n = len(Coins)

    for i in range(n):
        for j in range(1,T[i]+1):
            # 1 - n个硬币
            for k in range(amount,Coins[i]-1,-1):
                # 每轮递归推算整个dp数组
                dp[k] = min(dp[k],dp[k- Coins[i]]+1)
            print("dp:",dp)
    
    return dp[-1] if dp[-1]!=float("inf") else -1



if __name__ == '__main__':
    nums1 = [4,4,5,9]
    stoneMerge(4,nums1)

    coins1 = [1,2,5]
    nums = [3,3,3]

    coins2 = [1,5,10]
    amount = 18
    print(coinChange3(coins1,18,nums))
    print(coinChange2(coins2,15))


