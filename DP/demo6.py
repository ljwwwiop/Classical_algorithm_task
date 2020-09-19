'''
    状态压缩问题
    LeetCode - hard - 174
    LeetCode - hard - 887
'''

'''
编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。

例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。
思路：该题目可以使用二维DP，从左上到右下角进行暴力dp的比较简单，但耗费大
      所以压缩一下状态可以变换为一维dp解决,实质就是每一层的状态一个单元去维护就好了。

'''
def  calculateMinimumHP(dungeon):
    m = len(dungeon)
    n = len(dungeon[0])
    # 构建一维dp
    dp = [float("inf")]*(n+1)

    for i in range(m-1,-1,-1):
        dp[n] = 1 if i == m-1 else float("inf")
        for j in range(n-1,-1,-1):
            dp[j] = max(min(dp[j+1],dp[j]) - dungeon[i][j],1)
    print(dp)
    return dp[0]
d = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(calculateMinimumHP(d))

'''
输入：K = 1, N = 2
输出：2
解释：
鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
如果它没碎，那么我们肯定知道 F = 2 。
因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。

输入：K = 2, N = 6
输出：3
'''

def superEggDrop( K, N):
    '''
        dp[k][m] 的含义是k个鸡蛋 移动m次最多能够确定多少楼层
        这个角度思考
        dp[k][m] 最多能够确定的楼层数为L
        那么我选定第一个扔的楼层之后，我要么碎，要么不碎
        这就是把L分成3段
        左边是碎的那段 长度是dp[k][m - 1]
        右边是没碎的那段 长度是dp[k-1][m - 1] 因为已经碎了一个了
        中间是我选定扔的楼层 是1
        所以递推公式是
        dp[k][m] = dp[k - 1][m - 1] + dp[k][m - 1] + 1
    '''
    # 无压缩空间时候
    # dp = [[0]*(K+1) for _ in range(N+1)]
    # # 初始化
    # for i in range(N+1):
    #     dp[i][1] = i
    # for i in range(1,N+1):
    #     for j in range(2,K+1):
    #         res = float('inf')
    #         for k in range(1,i+1):
    #             res = min(res , max(dp[k-1][j-1], dp[i-k][j]) + 1)
    #         dp[i][j] = res
    # # dp[N][K]
    # print(dp)
    # return dp[-1][-1]

    # 压缩使用一维DP
    dp = [0]*(K+1)
    m = 0
    while dp[K] <N:
        m+=1
        for k in range(K,0,-1):
            dp[k] = dp[k - 1] + dp[k] + 1
    print(dp)
    return m

K,N = 2,6
print(superEggDrop(K,N))





