'''
    并查集： 本质就是检测图中是否存在圆环，或者一棵树是否存在环
    LeetCode - mid - 684 - 冗余连接
    LeetCode - mid - 547 - 朋友圈
    LeetCode - mid - 1319 - 连通网络的操作次数
    LeetCode - mid - 322 - 重新安排行程
'''

'''
在本问题中, 树指的是一个连通且无环的无向图。
输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的无向图为:
  1
 / \
2 - 3

输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]
解释: 给定的无向图为:
5 - 1 - 2
    |   |
    4 - 3
'''
def findRedundantConnection(edges):
    root = [i for i in range(len(edges)+1)]
    def find(i):
        if i != root[i]:
            root[i] == find(root[i])
        return root[i]
    for u,v in edges:
        u_parent = find(u)
        v_parent = find(v)
        if u_parent!= v_parent:
            root[v_parent] = u_parent
        else:
            return [u,v]

e = [[1,2], [2,3], [3,4], [1,4], [1,5]]
print(findRedundantConnection(e))

'''
给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，
表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

输入：
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出：2 
解释：已知学生 0 和学生 1 互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回 2 。
'''
class Union(object):
    def find_root(self,x,parent):
        # 寻找root
        root_x = x
        while parent[root_x] != -1:
            root_x = parent[root_x]
        return root_x

    def union(self,x,y,parent):
        # 合并x,y节点
        root_x = self.find_root(x,parent)
        root_y = self.find_root(y,parent)
        if root_x!= root_y:
            parent[root_y] = root_x
        return parent

    def findCircleNum(self,M):
        n = len(M)
        parent = [-1]*n
        for i in range(n):
            for j in range(n):
                if m[i][j] == 1:
                    parent = self.union(i,j,parent)
        circle = set()
        for i in range(n):
            root = self.find_root(i,parent)
            circle.add(root)
        return len(circle)

m = [[1,1,0],[1,1,0],[0,0,1]]
u = Union()
print(u.findCircleNum(m))

'''
请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。
输入：n = 4, connections = [[0,1],[0,2],[1,2]]
输出：1
解释：拔下计算机 1 和 2 之间的线缆，并将它插到计算机 1 和 3 上。

输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
输出：2
'''
def makeConnected(n,connections):
    p = [-1]*(n)
    for i in range(n):
        p[i] = i

    def find(i):
        if p[i] != i :
            p[i] = find(p[i])
        return p[i]

    res = 0
    for u,v in connections:
        if find(u) == find(v):
            res+=1
        else:
            p[find(v)] = find(u)
            n-=1
    n-=1
    if res <n:return -1
    return n
n = 6
e2 = [[0,1],[0,2],[0,3],[1,2],[1,3]]
print(makeConnected(n,e2))

'''

给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，
对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。
输入：[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出：["JFK", "MUC", "LHR", "SFO", "SJC"]

'''
from collections import defaultdict
def  findItinerary(tickets):
    dic = defaultdict(list)
    for u,v in tickets:
        dic[u].append(v)
    for start in dic:
        dic[start].sort(reverse=True)
    s = []
    def dfs(start):
        while dic[start]:
            dfs(dic[start].pop())
        s.append(start)
    dfs('JFK')
    return s[::-1]

dest = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(findItinerary(dest))






