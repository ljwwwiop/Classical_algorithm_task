'''
    动态规划
    爬楼梯 --> easy --> 力扣.70
'''
'''
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
'''
def func(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    dp = list()
    dp.append(1)
    dp.append(2)

    for i in range(2,n):
        dp.append(dp[i-1] + dp[i-2])
    return dp[-1]

# 测试 10 - 89
print(func(10))


