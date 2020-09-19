'''
    二位矩阵上面的问题
    LeetCode - mid - 64
    LeetCode - mid - 62
    LeetCode - mid - 63
    LeetCode - hard - 980
'''
'''
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''
def minPathSum(grid):
    # DP解决
    dp = [[0]*len(grid[0]) for _ in range(len(grid)) ]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i==0 and j==0:
                dp[i][j] = grid[0][0]
            elif i ==0 and j!=0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
            elif i!=0 and j==0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
    return dp[-1][-1]
grid = [
  [1,3,1],
  [1,0,8],
  [4,2,1]
]
print(minPathSum(grid))

'''
    一个机器人从(0,0)出发到(m,n)有多少种不同路径
'''
def uniquePaths(m,n):
    # 这题多种解法，可以直接数学解法，也可以DP，也可以简单递归
    if m == 0 or n == 0:
        return 1
    dp = [1]*n
    for i in range(1,m):
        for j in range(1,n):
            dp[j] += dp[j-1]
    return dp[-1]
print(uniquePaths(3,7))

'''
输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
'''
def uniquePathsWithObstacles(obstacleGrid):
    # grid 中存在障碍物
    n = len(obstacleGrid)
    m = len(obstacleGrid[0])
    if n<1 or m<1 or obstacleGrid[0][0] == 1:
        return 0
    dp = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                dp[i][j] = 1
            elif i==0 and j !=0:
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i][j-1]
            elif i!=0 and j==0:
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j]
            else:
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] +dp[i][j-1]
    return dp[-1][-1]
grid2 = [
  [0,1,0],
  [0,0,0],
  [0,0,0]
]
print(uniquePathsWithObstacles(grid2))

'''
DFS 解法
1 起点 ，2 结束点， 0 可以通过的路径， -1 无法跨越的障碍
输入：[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
输出：2
解释：我们有以下两条路径：
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
'''

direction = [(-1,0),(1,0),(0,1),(0,-1)]
def uniquePathsIII(grid):
    # 记录总共能通过的路径数
    rest = 1
    # 记录起点的x,y
    r,c =0,0
    n,m =len(grid),len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                r,c = i,j
            elif grid[i][j] == 0:
                rest+=1
            else:
                pass
    return dfs(grid,r,c,rest)

def dfs(grid,x,y,rest):
    if( x<0 or y >=len(grid[0]) or x>= len(grid) or y <0 or grid[x][y] == -1):
        return 0
    if(grid[x][y] == 2):
        return 1 if rest ==0 else 0
    # 回溯开始
    num = 0
    grid[x][y] = -1
    for direct in direction:
        num += dfs(grid,x + direct[0],y+direct[1],rest-1)
    grid[x][y] = 0
    return num

grid3 = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
print(uniquePathsIII(grid3))


