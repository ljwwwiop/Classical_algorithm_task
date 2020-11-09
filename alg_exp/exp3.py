
'''
    现在进来一个mid
    找到mid左边界
    找到mid右边界
    如果返回的 r == p == mid说明 这个数只有一个,
    [1,2,3,3,3,4,5]
    mid = 3
    p = 2,r = 4
'''

def pos(nums,left,right,mid,p,r):
    i = left
    while(i<=right):
        if nums[i] == nums[mid]:
            break
        i+=1
    
    p = i
    i = p+1
    while(i<=right):
        if(nums[i] != nums[mid]):
            break
        i+=1
    r = i-1
    return p,r

def test1(nums,left,right,cnt,num):
    mid = (left +right)//2
    p = 0 
    r = 0
    p,r = pos(nums,left,right,mid,p,r)
    # print(p,r)
    mid_count = r - p + 1
    if(mid_count > cnt):
        num = nums[mid]
        cnt = mid_count
    if(p-left > cnt):
        # 说明左边可能还有一样的继续二分找一下
        test1(nums,left,p-1,cnt,num)
    if(right - r - 1>cnt):
        test1(nums,p+1,right,cnt,num)
    
    return cnt,num

'''
    集合划分问题 -> 蓝桥杯
'''
def dfs(n,i):
    if(i == 1 or n==i):
        return 1
    else:
        return dfs(n-1,i-1)+i*dfs(n-1,i) 

def test2(n):
    s = 0
    for i in range(1,n+1):
        # 使用1个子集情况
        # 2个..3..n个
        s += dfs(n,i)
    print(s)




if __name__ == '__main__':
    nums = [1,2,2,2,3,5]
    nums2 = [1,1,2,2,2,3,3,3,3,3,4,4,5,6,7,7,7]
    n = 6
    n2 = 17
    cnt = 0
    num = 0
    cnt,num = test1(nums2,0,n2-1,cnt,num)
    print(num,cnt)
    test2(4)




