'''
    关于BFS -> 特点：传播速度快，从当前点开始，直接向四周扩散开
    LeetCode - mid - 79 - 单词搜索
    LeetCode - mid - 994 - 腐烂橘子
    LeetCode - mid - 130 - 被围绕的区域
    LeetCode - mid - 200 - 岛屿数量
    LeetCode - mid - 542 - 0,1矩阵
'''
'''
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
'''

class Solution:
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    def exist(self,board,word):

        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        marked = [[False]*(n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.__bfs(board,word,0,marked,i,j,m,n):
                    return True
        return False

    def __bfs(self,board,word,index,marked,x,y,m,n):
        if index == len(word) - 1:
            return word[index] == board[x][y]
        # 有一个位子匹配开始继续搜索
        if board[x][y] == word[index]:
            marked[x][y] = True
            for direct in self.directions :
                new_x = x + direct[0]
                new_y = y + direct[1]
                # 判断一下
                if(0<=new_x<m and 0<=new_y<n and not marked[new_x][new_y] and self.__bfs(board,word,index+1,marked,new_x,new_y,m,n)):
                    return True

            marked[x][y] = False
        return False
board =[
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ]
w1 = "ABCCED"
w2 = "SEE"
w3 = "ABCB"

s = Solution()
print(s.exist(board,w3))

'''
在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1
输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4
'''
def orangesRotting(grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    n = len(grid)
    m = len(grid[0])
    res = 0
    queue = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append((i,j,res))
    # bfs
    while queue:
        i,j,res = queue.pop(0)
        for x,y in directions:
            if 0<= x+i<n and 0<=y+j<m and grid[i+x][j+y] == 1:
                grid[i+x][j+y] = 2
                queue.append((i+x,j+y,res+1))
    # 是否有 没有被腐蚀的橘子
    for row in grid:
        if 1 in row:
            return -1
    return res
g1 = [[2,1,1],[1,1,0],[0,1,1]]
g2 = [[2,1,1],[0,1,1],[1,0,1]]
print(orangesRotting(g2))

'''
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X
'''
from collections import deque
def solve(board):
    if not board or not board[0]:
        return
    n = len(board)
    m = len(board[0])
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def _bfs(i,j):
        queue = deque()
        queue.appendleft((i,j))
        while queue:
            i,j = queue.pop()
            if 0<=i <n  and 0<= j <m and board[i][j] == "O":
                board[i][j] = 'A'
                for x,y in directions:
                    queue.appendleft((x+i,y+j))
    # 四个边检测一圈
    for j in range(m):
        if board[0][j] == "O":
            _bfs(0,j)
        if board[n-1][j] == "O":
            _bfs(n-1,j)

    for i in range(n):
        if board[i][0] == "O":
            _bfs(i,0)
        if board[i][m-1] == "O":
            _bfs(i,m-1)
    # 最后检测一遍
    for i in range(n):
        for j in range(m):
            if board[i][j] == "O":
                board[i][j] = "X"
            if board[i][j] == 'A':
                board[i][j] = "O"


b1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solve(b1)
print(b1)

'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
输入:
[
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出: 1
'''
class A:
    directions = [(-1,0),(0,-1),(1,0),(0,1)]
    def numIslands(self,grid):
        m = len(grid)
        if m ==0:
            return 0
        n = len(grid[0])
        count = 0
        marked = [[False]*(n) for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not marked[i][j]:
                    count+=1
                    queue =deque()
                    queue.append((i,j))
                    marked[i][j] = True
                    # bfs
                    while queue:
                        x ,y = queue.popleft()
                        for direct in self.directions:
                            new_x = x + direct[0]
                            new_y = y + direct[1]
                            if 0<= new_x<m and 0<= new_y<n and not marked[new_x][new_y]:
                                if grid[new_x][new_y] ==  '1':
                                    queue.append((new_x,new_y))
                                    marked[new_x][new_y] = True
        return count
b2 = [
        ['1','1','1','1','0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','0','0','0']
    ]
a = A()
print(a.numIslands(b2))

'''
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
两个相邻元素间的距离为 1 。
输入:
0 0 0
0 1 0
1 1 1
输出:
0 0 0
0 1 0
1 2 1
'''
def updateMatrix(matrix):
    # 原矩阵上修改
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    row = len(matrix)
    col = len(matrix[0])
    queue = []
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                queue.append([i,j])
            else:
                matrix[i][j] = row + col
    while queue:
        s = queue.pop()
        # 开始搜索
        for direct in directions:
            x = s[0] + direct[0]
            y = s[1] + direct[1]
            if 0<=x<row and 0<=y<col and matrix[x][y] > matrix[s[0]][s[1]] + 1:
                matrix[x][y] = matrix[s[0]][s[1]] + 1
                queue.append([x,y])
    return matrix
g4 = [[0,0,0],[0,1,1],[0,1,1]]
print(updateMatrix(g4))


