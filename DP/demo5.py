'''
    字符串序列问题，子串问题，上升序列问题
    LeetCode - hard - 72
    LeetCode - mid - 300
    LeetCode - hard - 115
    LeetCode - mid - 5
    LeetCode - mid - 718
    LeetCode - mid - 516
'''

'''
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数
输入：word1 = "horse", word2 = "ros"
输出：3
思路：DP 创建二维数组  -> 找到状态转移方程
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
'''

def minDistance(w1,w2):
    n1,n2 = len(w1),len(w2)

    dp = [[0]*(n2+1) for _ in range(n1+1)]

    # 初始化第一行和第一列
    for i in range(1,n2+1):
        dp[0][i] = dp[0][i-1] + 1
    for i in range(1,n1+1):
        dp[i][0] = dp[i-1][0] + 1

    # 处理转移方程,如果出现同样的字母，直接替换
    # 如果不一样，则min（替换，删除，插入）最小值的操作
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if w1[i-1] == w2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
    # print(dp)
    return dp[-1][-1]

s1,s2 = "execution","intention"
print(minDistance(s1,s2))

'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。
思路：一维DP，可以二维浪费空间。
输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
'''


def lengthOfLIS(nums):
    if not nums:
        return 0
    n = len(nums)
    dp = [1]*n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i],dp[j] + 1)
    print(dp)
    return max(dp)

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))

'''
给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数
思路：二维数组，S,T构建二维数组，枚举每个状态就好了
输入：S = "rabbbit", T = "rabbit"
输出：3
解释：

如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)
rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
'''
def numDistinct(s,t):
    n1, n2 = len(s), len(t)
    dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
    # 初始化第一行,默认一个字母变换一个字母时候有任何可能可以得到字符T
    for j in range(n1 + 1):
        dp[0][j] = 1
    for i in range(1, n2 + 1):
        for j in range(1, n1 + 1):
            if t[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
    print(dp)
    return dp[-1][-1]

S ,T = "rabbbit","rabbit"
print(numDistinct(S,T))

'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000
思路：DP/中心扩散算法
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案
'''
def longestPalindrome(s):
    n = len(s)
    if n < 2:
        return s
    # 二维DP，简单的枚举了字符串的每种状态
    dp = [[False]*n for _ in range(n)]
    max_len = 1
    start = 0

    # 初始化对角线，自己和自己肯定是True
    for i in range(n):
        dp[i][i] = True
    for j in range(1,n):
        for i in range(j):
            # 判断是否回文
            if s[i]== s[j] :
                if j-i<3:
                    dp[i][j] = True
                else:
                    # 大于3，可能中间还存不回文的
                    dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = False
            if dp[i][j]:
                cur_len = j - i + 1
                if cur_len > max_len:
                    start = i
                    max_len = cur_len
    print(dp)
    return s[start:start+max_len]
s2 = "babad"
print(longestPalindrome(s2))

'''
输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
思路：二维DP
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。
'''
def findLength(A,B):
    n = len(A)
    m = len(B)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
    # print(dp)
    return max(max(row) for row in dp)
A = [1,2,3,2,1]
B = [3,2,1,4,7]
print(findLength(A,B))

'''
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。
输入: "bbbab"
输出: 4
'''
def longestPalindromeSubseq(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]

    # 对角线初始化
    for i in range(n):
        dp[i][i] = 1
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j-1])
    print(dp)
    return dp[0][-1]

s3 = "bbbab"
print(longestPalindromeSubseq(s3))






