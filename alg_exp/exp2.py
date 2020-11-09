'''
    author: By@Lian
    基本排序: 选择排序 直接排序 折半排序 希尔排序 冒泡排序 快速排序 堆排序 归并排序
    选择类：选择排序
    插入类：直接，折半，希尔排序
    交换类：冒泡，快速排序
    堆排序: 二叉树
    归并排序: 和快排类似
    桶排：基于 hash /set 一种计数排序
    2020/1/9    
'''

def portition(num,left,right):
    povit = num[left]
    while(left < right):
        while(left<right and num[right] >=povit):    
            right-=1
        num[left] = num[right]
        while(left < right and num[left] <= povit):
            left+=1
        num[right] = num[left]
    num[left] = povit
    return left

def quick_sort(num,left,right):
    if left<right:
        p = portition(num,left,right)
        quick_sort(num,left,p-1)
        quick_sort(num,p+1,right)

def Binary_sort(List):
    for i in range(1,len(List)-1):
        index = List[i]
        low = 0
        high = i-1
        while(low<high):
            mid = (low+high)//2
            if List[mid] >index:
                high = mid - 1
            else:
                low = mid +1
        for j in range(i,low,-1):
            List[j] = index
    return List

def shell_sort(List):
    d = len(List)//2
    while(d>=1):
        for i in range(d,len(List)):
            temp = List[i]
            j = i-d
            while(j>=0 and List[j]>temp):
                List[j+d] = List[j]
                j = j - d
            List[j+d] = temp
        d = d//2
    return List

def mergeSort(nums):
    if(len(nums) < 2):
        return nums
    mid = len(nums)//2
    left,right = nums[0:mid],nums[mid:]
    return merge(mergeSort(left),mergeSort(right))

def merge(left,right):
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    
    while right:
        res.append(right.pop(0))
    while left:
        res.append(left.pop(0))
    return res

# 冒泡
def Bubble_sort(nums):
    x = len(nums)
    for i in range(1,x):
        for j in range(0,x-i):
            if(nums[j] > nums[j+1]):
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

# 选择
def Select_sort(nums):
    for i in range(0,len(nums) - 1):
        min = i
        for j in range(i+1,len(nums)):
            if(nums[j] < nums[min]):
                min,j = j,min
        if min!= i:
            nums[min],nums[i] = nums[i],nums[min]
    return nums

# 插入
def Insert_sort(nums):
    for i in range(1,len(nums) - 1):
        temp = nums[i]
        j = i -1
        while j>=0 and nums[j] > temp:
            nums[j+1] = nums[j]
            --j
        nums[j+1] = temp
    return nums

if __name__ == '__main__':
    num = [4,2,6,5,1]
    num2 = [2,-1,6,4,0]

    # 快速排序
    quick_sort(num,0,4)
    print("快速排序 -->",num)
    print("二分排序 -->",Binary_sort(num2))
    print("希尔排序 -->",shell_sort(num2))
    print("归并排序 -->",mergeSort(num2))
    print("冒泡排序 -->",Bubble_sort(num2))
    print("选择排序 -->",Select_sort(num2))
    print("直接排序 -->",Insert_sort(num2))




