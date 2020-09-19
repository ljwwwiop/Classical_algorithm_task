'''
    22
    回溯算法/dfs ->  本质就是 递归  +  剪枝（万能算法，非常好用）
    LeetCode - mid - 46 - 全排列
    LeetCode - mid - 47 - 全排列II
    LeetCode - mid - 77 - 组合
    LeetCode - mid - 695 - 岛屿的最大面积
    LeetCode - mid - 1254 - 统计封闭岛屿的数目
    LeetCode - mid - 面试题 - 水域大小
    LeetCode - mid - 886 - 可能的二分法（DFS+染色）
    LeetCode - mid - 841 - 钥匙和房间
    LeetCode - hard - 55 - N皇后  (回溯经典题目)
'''

'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

def permute(nums):
    res = []
    def dfs(nums,tmp):
        if not nums:
            res.append(tmp)
            return
        for i in range(len(nums)):
            dfs(nums[:i]+nums[i+1:],tmp + [nums[i]])
    dfs(nums,[])
    return res

t = [1,2,3]
print(permute(t))

'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。
不能有重复。
'''
def permuteUnique(nums):
    res = []
    def dfs(nums,tmp):
        if not nums:
            res.append(tmp)
            return
        mark = set()
        for i in range(len(nums)):
            if nums[i] in mark:
                continue
            dfs(nums[:i]+nums[i+1:],tmp + [nums[i]])
            mark.add(nums[i])
    dfs(nums,[])
    return res

t2 = [1,3,2]
print(permuteUnique(t2))

'''
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
def combine(n,k):
    res = []
    def dfs(s,path):
        if k == len(path):
            res.append(path)
            return
        for i in range(s+1,n+1):
            if n -i + 1<k - len(path):
                return
            dfs(i,path+[i])
    dfs(0,[])
    return res
print(combine(4,2))


'''
一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。
你可以假设 grid 的四个边缘都被 0（代表水）包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
返回：6
'''
def maxAreaOfIsland(grid):
    if not grid:
        return 0
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            res = max(res,_dfs(grid,i,j))
    return res

def _dfs(grid,i,j):
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) :
        return 0
    if(grid[i][j] == 0): return 0
    grid[i][j] = 0
    s = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for x,y in directions:
        new_x = x + i
        new_y = y + j
        s+= _dfs(grid,new_x,new_y)
    return s

g1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(g1))

'''
有一个二维矩阵 grid ，每个位置要么是陆地（记号为 0 ）要么是水域（记号为 1 ）。
我们从一块陆地出发，每次可以往上下左右 4 个方向相邻区域走，能走到的所有陆地区域，我们将其称为一座「岛屿」。
如果一座岛屿 完全 由水域包围，即陆地边缘上下左右所有相邻区域都是水域，那么我们将其称为 「封闭岛屿」。
请返回封闭岛屿的数目。

输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
输出：2
解释：
灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
'''
class Solution(object):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def closedIsland(self, grid):
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 0):
                    self.val = 1
                    self.dfs(grid, i, j)
                    # print(self.val)
                    res += self.val
        return res

    def dfs(self, grid, i, j):
        if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])):
            self.val = 0
            return
        if (grid[i][j] == 1):
            return
        grid[i][j] = 1
        for direction in self.directions:
            new_x = direction[0] + i
            new_y = direction[1] + j
            self.dfs(grid, new_x, new_y)

g2 = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]

s = Solution()
print(s.closedIsland(g2))

'''
你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。
由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。
编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。
输入：
[
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
输出： [1,2,4]
'''
def pondSizes(land):
    res = []
    board = land
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 0:
                size = _dfs_3(land,i,j)
                print("size",size)
                res.append(size)
    res.sort()
    return res

def _dfs_3(land,i,j):
    if(i<0 or i >= len(land) or j<0 or j>= len(land[0])):
        return 0
    if(land[i][j] != 0):
        return 0
    land[i][j] = 1
    size = 1
    # 8个方向
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),(1,1),(1,-1),(-1,1),(1,1)]
    for direct in directions:
        x = i + direct[0]
        y = j + direct[1]
        size += _dfs_3(land,x,y)
    return size

g3 = [[0,2,1,0],[0,1,0,1],[1,1,0,1],[0,1,0,1]]
print(pondSizes(g3))

'''
给定一组 N 人（编号为 1, 2, ..., N）， 我们想把每个人分进任意大小的两组。
每个人都可能不喜欢其他人，那么他们不应该属于同一组。
形式上，如果 dislikes[i] = [a, b]，表示不允许将编号为 a 和 b 的人归入同一组。
当可以用这种方法将每个人分进两组时，返回 true；否则返回 false。
输入：N = 4, dislikes = [[1,2],[1,3],[2,4]]
思路：DFS+染色（不用考虑是否有环的并查集）
输出：true
解释：group1 [1,4], group2 [2,3]
'''
from collections import defaultdict
def possibleBipartition(N,dis):
    graph = defaultdict(list)
    for d in dis:
        graph[d[0]].append(d[1])
        graph[d[1]].append(d[0])

    color = dict()
    def dfs(i,c = 1):
        if i in color:
            return c== color[i]
        # 节点未染色，和i相邻的节点也未染色，故默认染色都为1
        color[i] = c
        # 将节点i的所有相邻节点染色为-1，都不存在染色冲突则返回True
        return all(dfs(j, -1 * c) for j in graph[i])
    return all(dfs(i) for i in range(1,N+1) if i not in color)

N = 4
dislikes = [[1,2],[1,3],[2,4]]
print(possibleBipartition(N,dislikes))

'''
最初，除 0 号房间外的其余所有房间都被锁住。
你可以自由地在房间之间来回走动。
如果能进入每个房间返回 true，否则返回 false。
输入：[[1,3],[3,0,1],[2],[0]]
输出：false
解释：我们不能进入 2 号房间。
'''
def canVisitAllRooms(rooms):
    res = [0]*(len(rooms))
    def dfs(key,rooms,res):
        if(res[key]):
            return
        res[key] = 1
        ans = rooms[key]
        for k in ans:
            dfs(k,rooms,res)

    dfs(0,rooms,res)
    for i in res:
        if i==0:
            return False
    return True
g5 =[[1,3],[3,0,1],[2],[0]]
print(canVisitAllRooms(g5))

'''
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
输入：4
输出：[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
'''

def solveNQueens(n):
    res = []
    # 初始化一个棋盘
    board = [['.']*(n) for _ in range(n)]
    # 回溯 ，棋盘，行 row
    backtrace(res,board,0)
    return

def backtrace(res,board,row):
    # 结束条件
    if row == len(board):
        print(board)
        for b in board:
            res.append(b)
        return
    n = len(board[row])
    for col in range(n):
        # 遍历列col
        if not isValid(board,row,col):
            continue
        # 可以的话就回溯
        board[row][col] = 'Q'
        backtrace(res,board,row+1)
        board[row][col] = '.'

def isValid(board,row,col):
    n = len(board)
    # 三个方向遍历
    for i in range(n):
        if board[i][col] == 'Q':
            return False

    x,y = row-1,col+1
    while x >=0 and y<n:
        if board[x][y] == 'Q':
            return False
        x-=1
        y+=1

    x,y = row-1,col-1
    while x >=0 and y>=0 :
        if board[x][y] == 'Q':
            return False
        x-=1
        y-=1
    return True

solveNQueens(6)





