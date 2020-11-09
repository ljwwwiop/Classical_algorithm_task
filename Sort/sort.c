#include<stdio.h>
#include<stdlib.h>

/*  
    author:By@Lian
    基本排序: 选择排序 直接排序 折半排序 希尔排序 冒泡排序 快速排序 堆排序 归并排序
    选择类：选择排序
    插入类：直接，折半，希尔排序
    交换类：冒泡，快速排序
    堆排序: 二叉树
    归并排序: 和快排类似
    桶排：基于 hash /set 一种计数排序
    2020/1/9    
*/

// 快速排序
int Portition(int A[],int low,int high)
{
    int povit = A[low];
    while(low<high)
    {
        while(low<high && A[high]>povit)
            --high;
        A[low] = A[high];
        while(low<high && A[low]<povit)
            ++low;
        A[high] = A[low];
    }
    A[low] = povit;
    return low;
}


int QuickSort(int A[],int low,int high)
{
    if(low<high)
    {
        int p = Portition(A,low,high);
        QuickSort(A,low,p-1);
        QuickSort(A,p+1,high);
    }

}

// 冒泡排序
void BubbleSort(int A[],int n)
{
    int i,j,temp,flag;
    for(i=0;i<n-1;i++)
    {
        flag = 0;
        for(j=0;j<n-i-1;j++)
            if(A[j+1]<A[j])
            {
                temp = A[j];
                A[j] = A[j+1];
                A[j+1] = temp;
                flag = 1;
            }
        if(flag==0)
            return ;
    }
}

// 选择排序
void SelectSort(int A[],int n)
{
    int i,j,min,temp;
    for(i=0;i<n-1;i++)
    {
        min = i;
        for(j=i+1;j<n;j++)
            if(A[min]>A[j])
                min = j;
        if(min!=i)
        {
            temp = A[min];
            A[min] = A[i];
            A[i] = temp;
        }
    }
}

// 直接排序
void InsertSort(int A[],int n)
{
    int i,j,temp;
    for(i=1;i<n;i++)
    {
        temp = A[i];
        j = i-1;
        while(j>=0 && A[j] >temp)
        {
            A[j+1] = A[j];
            --j;
        }
        A[j+1] = temp;
    }
}

// 折半排序 - > 折半查找
void BinarySort(int A[],int n)
{
    int low,high,mid,i,j,temp;
    for(i=1;i<n;i++)
    {
        low = 0,high=i-1;
        while(low<=high)
        {
            mid = (low+high)/2;
            if(A[mid]>A[i])
                high = mid-1;
            else
                low = mid + 1;
        }

        temp = A[i];
        for(j=i-1;j>=high+1;--j)
            A[j+1] = A[j];
        A[high+1] = temp;
    }
}

// 折半查找 -> 查值 -> 下标  没有-> -1
int BinarySearch(int* A,int n,int key)
{
    int low,high,mid;
    low = 0;
    high = n-1;
    while(low<high)
    {
        mid = (low + high)/2;
        if(A[mid] == key)
            return mid;
        else if(A[mid] <key)
            low = mid+1;
        else 
            high = mid -1;
    }
    return -1;
}

// 折半的原理 实现sqrt() 平方根 ->牛顿迭代法
int Sqrt(int key)
{
    int left = 0;
    int right = key;
    while(left<right)
    {
        int mid =0,res;
        mid = (left + right +1)/2;
        res = mid*mid;
        if(res >key)
            right = mid -1;
        else 
            left = mid ;
    }
    return left;
}


// 希尔排序 缩小增量排序
void ShellSort(int A[],int n)
{
    int i,j,temp,d;
    for(d=n/2;d>=1;d=d/2)
    {
        for(int i =d;i<n;i++){
            temp = A[i];
            for(int j=i-d;j>=0 && A[j] > temp;j = j-d)
                A[j+d] = A[j];
            A[j+d] = temp;
        }
    }
}

// 打印函数
void Print( int A[],int n)
{
    for(int i=0;i<n;i++)
        printf("%d ",A[i]);
    printf("\n");
}

// test
void test()
{
    long A[1000000];
    for(long i = 0;i<1000000;i++)
        A[i] = 1;
    A[987] = 7;
    for(long i = 0;i<1000000;i++)
        printf("%d ",A[i]);
}

int main()
{   
    // [3,34,-4,12,5,2]
    //int A[6] = {3,34,-4,12,5,2};
    //int B[5] = {3,-4,12,5,2};

    //QuickSort(A,0,5);
    //BubbleSort(A,6);
    //InsertSort(A,6);
    //SelectSort(A,6);
    //BinarySort(A,6);
    //ShellSort(A,6);
    //Print(A,6);
    // printf("%d\n",Sqrt(8));
    test();

    system("pause \n");
    return 0;
}






