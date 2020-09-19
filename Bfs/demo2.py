'''
    BFS非类似二维矩阵的应用
    LeetCode - hard - 126 - 单词接龙II
'''
from collections import deque,defaultdict
'''
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。
转换需遵循如下规则：
每次转换只能改变一个字母。
转换后得到的单词必须是字典中的单词。
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
'''
def findLadders(beginWord,endWord,wordList):
    wordList = set(wordList)
    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return []
    dic = defaultdict(list)
    n = len(beginWord)
    for w in wordList:
        for i in range(n):
            dic[w[:i] + '*' + w[i + 1:]].append(w)
    q, s = deque([(beginWord, [beginWord])]), deque()
    # print(dic)
    visited = set()
    res = []
    while q:
        while q:
            w,path = q.popleft()
            visited.add(w)
            for i in range(n):
                for v in dic[w[:i] + '*' + w[i + 1:]]:
                    # print(v, dic[w[:i] + '*' + w[i + 1:]],w[:i] + '*' + w[i + 1:])
                    if v == endWord:res.append(path + [v])
                    if v not in visited:
                        s.append((v,path+[v]))
        if res: return res
        q,s = s,q
    return []


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(findLadders(beginWord,endWord,wordList))

'''
二叉树的层次遍历/以及平均值/右视图 都是类似算法
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
输出：
[
  [3],
  [20,9],
  [15,7]
]
'''
# Root 是 TreeNode
def zigzagLevelOrder(root):
    if not root:
        return []
    res = []
    q = [root]
    level = 0
    while q:
        size = len(q)
        ans = deque()
        for i in range(size):
            temp = q.pop(0)
            if(level%2==0):
                ans.appendleft(temp.val)
            else:
                ans.append(temp.val)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        res.append(ans)
        level+=1
    return res








