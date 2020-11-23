# test6 回溯算法实验

signs = ['+', '-', '*', '/']
def test1(n,m,nums):
    res = [0]*n
    S = [0]*n
    min_Value = []
    dfs(nums,res,S,m,min_Value)
    # print(min_Value)
    index = float("inf")
    tmp = ""
    for value in min_Value:
        if index >= value[0]:
            print(" min operator :",value[0],"\n","function :",value[1] )
            index = value[0]
'''
number - res
count - S
nums - figure
ans - figures
'''
def dfs(nums,res,S,m,min_Value):
    # 长度到达了
    if getNumberNumber(res) == len(res):
        return
    # 如果nums中数字，都已经使用，则判断后，返回
    if getNumberNumber(res) == 0:
        for i in range(0,len(nums)):
            res[0] = nums[i]
            dfs(nums,res,S,m,min_Value)
    else:
        # 5 已经进入了，那么开始进入符号
        for i in range(len(signs)):
            # 获取之前的操作数和操作结果，进行叠加
            oldCal = getOldCalculateResult(res,S)
            # 将新的操作符存入数组
            addS(S,signs[i])

            # 获得一个
            ans = getAvailableFigures(res,nums)

            for j in range(getNumberNumber(ans)):
                nextNum = ans[j]
                # 将操作数存入数组
                addNumber(res,nextNum)
                # 获得新得运算结果
                newCal = getNewCalculateResult(oldCal,nextNum,signs[i])
                if newCal == m:
                    # print("newCal", newCal)
                    printResult(res,S,m,min_Value)
                # 本次内容调取完毕，继续试探
                dfs(nums,res,S,m,min_Value)
                # 递归结束，取消试探
                removeNumber(res);
            removeCount(S);

def getNumberNumber(res):
    n = 0
    for i in range(len(res)):
        if(res[i] !=0):
            n+=1
        else:
            return n
    return n

def getCountNumber(S):
    n = 0
    for i in range(len(S)):
        if(S[i] != 0):
            n+=1
        else:
            return n
    return n

def getNewCalculateResult(oldcal,num,sign):
    ans = oldcal
    # print("num",num)
    # print("ans",ans)
    if sign == '+':
        ans += num
    elif sign == '-':
        ans -= num
    elif sign == '*':
        ans *= num
    elif sign == '/':
        ans /= num
    return ans

def getOldCalculateResult(res,S):
    ans = res[0]
    for i in range(getCountNumber(S)):
        if S[i] == 0:
            return ans
        if S[i] == '+':
            ans += res[i+1]
        elif S[i] == '-':
            ans -= res[i+1]
        elif S[i] == '*':
            ans *= res[i+1]
        elif S[i] == '/':
            ans /= res[i+1]
    return ans

def getAvailableFigures(res,nums):
    ans = [0]*len(nums)
    index = [True]*len(nums)

    for i in range(getNumberNumber(res)):
        for j in range(len(nums)):
            if res[i] == nums[j] and index[j]:
                index[j] = False
                break

    j = 0
    for i in range(len(nums)):
        if(index[i]):
            ans[j] = nums[i]
            j+=1
    return ans

def addNumber(res,nextNum):
    for i in range(len(res)):
        if(res[i] == 0):
            res[i] = nextNum
            return

def addS(S,ch):
    for i in range(len(S)):
        if(S[i] == 0):
            S[i] = ch
            return

def removeNumber(res):
    res[getNumberNumber(res) - 1] = 0

def removeCount(S):
    S[getCountNumber(S) - 1] = 0

def printResult(res,S,m,min_value):
    # print("res",res,"S",S)
    temp = ""
    ans = float("inf")
    for i in range(getNumberNumber(res)):
        # print(res[i],end="")
        temp += str(res[i])
        if( i == getCountNumber(S)):
            if ans >= i:
                ans = i
                temp += " = " + str(m)
                # print("i ",i)
                # print("temp ",temp)
                min_value.append((i,temp))
            # print("= ",m)
        else:
            temp += S[i]
            # print(S[i],end="")

'''
    稍微简单一点点 
    15 4 , f(i) = 3*i,g(i) = [i/2]
    深度受限制，直接根据深度暴力解
    f , g两个分支
'''
def test2(n,m):
    level = 1
    ch = ""
    def dfs(n,tmp,m):
        nonlocal ch
        if(tmp > level):
            return False
        sum = n
        for i in range(2):
            sum = n*3 if i == 0 else n//2
            if(sum == m ) or (dfs(sum,tmp+1,m)):
                ch += "f" if i == 0 else "g"
                return True
        return False

    while not dfs(n,1,m):
        level+=1
    print(level)
    print(ch)

def test3(m,n):
    '''15 - 4 '''
    q = [m]
    visited = []
    s = ""
    level = 0
    while q:
        for i in range(len(q)):
            temp = q.pop()
            if temp == n:
                print(level)
            for i in range(2):
                if i == 0:
                    temp = temp*3
                    q.append(temp)
                elif i == 1:
                    temp = temp/2
                    q.append(temp)
        level+=1

if __name__ == "__main__":
    n = 5
    m = 25
    nums = [5,2,3,6,7]

    test1(n,m,nums)

    n2 = 4
    m2 = 15
    test2(m2,n2)
    test3(m2,n2)



