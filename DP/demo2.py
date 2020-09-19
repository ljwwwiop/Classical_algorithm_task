'''
    小偷/打家劫舍 系列问题
'''

'''
    LeetCode - easy - 198
    输入：[1,2,3,1]  [2,7,9,3,1]
    输出：4          12
'''
def rob1(nums):
   '''
   :type nums: List[int]
    :rtype: int
   '''
   if len(nums) == 0:
       return 0
   if len(nums) == 1:
       return nums[-1]
   dp = [0 *i for i in range(len(nums))]
   dp[0] = nums[0]
   dp[1] = max(nums[0],nums[1])
   for i in range(2,len(nums)):
       dp[i] = max(dp[i-1],dp[i-2] + nums[i])
   return dp[-1]

num = [2,7,9,3,1]
print("rob1 :",rob1(num))

'''
    LeetCode - mid - 213
    输入: [2,3,2]  [1,2,3,1]
    输出: 3        4
'''
def rob2(num):
    '''
    思路：
        三种情况 哪个最大
        [1,n-1] dp1
        [2,n-1] - > 交集
        [2,n] dp2
    '''
    n = len(num)
    if n ==0 :
        return 0
    if n== 1:
        return num[1]
    dp1 = [0]*n
    dp2 = [0]*n
    dp1[0],dp2[0] = 0,0
    dp1[1],dp2[1] = num[0],num[1]
    for i in range(2,n):
        dp1[i] = max(dp1[i-1],dp1[i-2]+num[i])
    for i in range(2,n):
        dp2[i] = max(dp2[i-1],dp2[i-2] + num[i])
    return max(dp1[-1],dp2[-1])

print("rob2 :",rob2(num))

'''
    LeetCode - mid - 337
    输入: [3,2,3,null,3,null,1]
         3
        / \
       2   3
        \   \ 
         3   1
    输出: 7 
'''

def rob3(root):
    '''
        输入是一颗树root节点
    '''
    if not root:
        return 0
    res = DP(root)
    return max(res)

def DP(root):
    if root is None:
        return [0,0]
    left = DP(root.left)
    right = DP(root.right)
    # 抢根节点的最大值多少
    rob = root.val + left[1] + right[1]
    # 不抢根节点的最大值是多少
    skip = max(left) + max(right)
    return [rob,skip]
