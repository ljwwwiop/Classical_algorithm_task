'''
input: 7 km, 7 个加油站
7 7
1 2 3 4 5 1 6 6
output
4
解题：
    转换到贪心路程问题
    3 - 1
    4 - 1
    6 - 1
    6 - 1
类似：134 加油站 -> 华为一面算法题
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
output:3 
'''
import os

def test1(n,k,gas):
    res = 0
    ans = n
    stop = [0]*(k+1)
    for i in range(k+1):
        if ans >= gas[i]:
            # 够的话直接走算出剩下多少
            ans -= gas[i]
        else:
            # 不够，就把油加满再走
            ans = n -  gas[i]
            res+=1
    print(res)

def test2(n,k,gas):
    res = 0
    ans = n
    stop = [0]*(k+1)
    if ans < gas[0]: return -1

    flag = 0
    for i in range(len(gas)):
        if ans < gas[i]:
            # 汽油不够下一波
            ans = n - gas[i]
            res+=1
            stop.append(i)
        else:
            # 汽油够下一波直接走
            ans -= gas[i]
    print(stop)
    return -1 if res>k else res


'''
input:
4
5 12 11 2
output:
78 52
思路：
最小时候：从小到大比较
    1 2 3 4
    -2 0 1 2 
最大时候：从大到小比较
    
'''
def test3_get_max(k,nums):
    res = 0
    nums.sort(reverse=True)
    # 12 11 5 2
    # m + n - 1
    # 12 + 11 - 1 = 22 -> 22
    # 23 + 5 - 1 = 27 -> 49
    # 28 + 2 -1 = 29 -> 78
    while(len(nums) > 1):
        t = 0
        t += nums[0] + nums[1]
        nums[1] = t
        t-=1
        res+=t
        nums = nums[1:]
    print(res)

def test3_get_min(k,nums):
    # 2 5 11 12
    # m + n - 1
    res = 0
    nums.sort()
    while len(nums) > 1:
        t = 0
        t += nums[0] + nums[1]
        nums.append(t)
        res += t - 1
        nums = nums[2:]
        nums.sort()
    print(res)

def get_gas_txt_info(path):
    for root,dirs,filenames in os.walk(path):
        for filename in filenames:
            file_path = root + '/'+filename
            with open(file_path,'r') as fp:
                data = fp.readlines()
                temp,nums = data[0],data[1].replace('\n','')
                temp = temp.split(' ')
                temp[1] = temp[1].replace('\n','')
                n,k = int(temp[0]),int(temp[1])
                nums = nums.split(' ')
                if nums[-1] == '':
                    nums.remove('')
                nums = list(map(int,nums))
                print("%s :"%filename)
                print(test2(n, k, nums))
                fp.close()

def get_merge_txt_info(path):
    for root,dirs,filenames in os.walk(path):
        print(filenames)
        for filename in filenames:
            file_path = root + '/'+filename
            with open(file_path,'r') as fp:
                data = fp.readlines()
                temp,nums = data[0],data[1].replace('\n','')
                temp = temp.split(' ')
                temp[0] = temp[0].replace('\n','')
                n = int(temp[0])
                nums = nums.split(' ')
                if nums[-1] == '':
                    nums.remove('')
                nums = list(map(int,nums))
                nums2 = nums.copy()
                print("%s :"%filename)
                test3_get_min(n,nums)
                test3_get_max(n,nums2)
                fp.close()

if __name__ == "__main__":
    # path1 = './TEST1'
    # path2 = './TEST2'
    # get_gas_txt_info(path1)
    # get_merge_txt_info(path2)


    n,k = 7 ,7
    gas = [1,2,3,4,5,1,6,6]

    k2 = 4
    num1 = [5,12,11,2]
    num2 = [5,12,11,2]
    test3_get_min(k2,num1)
    test3_get_max(k2,num2)

    print(test2(n,k,gas))

