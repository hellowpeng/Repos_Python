#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import random

tup1 = (6,9,4,2,5,1,3,8)
list1 = [6,9,4,2,5,1,3,8]
flag = 1 #初始化排序标志，1 标识可能需要继续下一轮排序 0 标识不需要
count = 0
#print("tup1[0]: ",tup1[0])

#快排的主函数，传入参数为一个列表，左右两端的下标



def random_list(start,stop,length):
    if length>=0:
        length=int(length)
        start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
        r_list = []
        print("正在构造随机数组，数组长度：",length)
        s_time = time.time()
        for i in range(length):
            r_list.append(random.randint(start, stop))
        print("数组构造完成，耗时：",time.time() - s_time,"s")
        return r_list


def QuickSort(alist, start, end):
    print("---1: ",alist,start,"~",end)
    if start >= end:
        # 退出递归
        return
    # 选取首位元素作为基准值
    pivot = alist[start]
    r_index = end
    l_index = start+1

    flag = 0
    # 问题：在左指针已经指向大于基准值的当前为止时，右指针
    # 双指针同步走
    while l_index < r_index:
        if alist[l_index] > pivot: # 如果左指针指向的值大于基准值，此时左指针不动
            flag = 1 # 存在大于基准值的值
            while l_index < r_index:
                if alist[r_index] < pivot: # 如果右指针指向的值小于基准值
                    alist[l_index],alist[r_index] = alist[r_index],alist[l_index] # 交换左右指针指向的值
                    print("---2: ",alist)
                    l_index += 1 # 左指针右移
                    break # 交换完毕，退出子循环，进入主循环
                else:
                    r_index -= 1 # 如不满足，右指针左移，直到满足为止
        l_index += 1 # 左指针右移

    # 左右指针碰头的地方，插入基准值
    print("l_index: ",l_index," flag: ",flag," r_index: ",r_index)
    del alist[start]
    if flag == 1:
        alist.insert(l_index-1,pivot)
    else:
        alist.insert(l_index,pivot)
    print("---3: ",alist)


    # # 控制right -= 1不满足条件交换
    # while left < right:
    #     while left < right and alist[right] > pivot:
    #         right -= 1
    #     else:
    #         # 交换
    #         alist[left] = alist[right]
    #     # 控制 left += 1 , 不满足条件交换
    #     while left < right and alist[left] < pivot:
    #         left += 1
    #     else:
    #         alist[right] = alist[left]
    #
    # # 退出循环 left = right
    # # left 或者 right 对应的位置 赋值为基准值
    # alist[left] = pivot

    # 递归自己调用自己
    QuickSort(alist, start, l_index - 2)  # 对左边排序
    QuickSort(alist, l_index, end)  # 对右边排序

def QuickSort2(list,start,end):

    # print(list)

    if start >= end:
        return

    #随机基准值
    pivot_index = random.randint(start, end)
    # print("pivot_index: ",pivot_index)
    pivot = list[pivot_index]
    l_index = start
    end_index = end
    while l_index <= end_index:
        if list[l_index] > pivot and l_index < pivot_index:
            tmp = list[l_index]
            del list[l_index]
            list.insert(pivot_index+1,tmp)
            pivot_index -= 1 #大于基准值并且在基准值前面的，移动到基准值后面，基准值位置前移,指针位置不变
            l_index -= 1 # 这里需要指针位置保持不变，所以要-1以抵消指针的例行加1
        if list[l_index] < pivot and l_index > pivot_index:
            tmp = list[l_index]
            del list[l_index]
            list.insert(pivot_index,tmp)
            pivot_index += 1 #小于基准值并且在基准值后面的，移动到基准值前面，基准值位置后移

        l_index += 1 # 指针前移

    # 以上循环完成后，生成两段list，以pivot_index为分界点
    # 递归对这两段list做排序
    # print("QuickSort2(list,", start, ",", pivot_index - 1, ")")
    # print("QuickSort2(list,", pivot_index + 1, ",", end, ")")
    QuickSort2(list,start,pivot_index-1)
    QuickSort2(list,pivot_index+1,end)


if __name__=="__main__":
    list1 = random_list(1, 100, 10)
    #list1 = [95,55, 34, 57]
    # print(list1)
    start_time = time.time()
    # QuickSort2(list1,0,len(list1)-1)
    QuickSort(list1,0,len(list1)-1)

    print(list1)

    end_time = time.time()
    #print("total numbers: ",len(list1))
    #print("sort times: ",count-1)
    print("time elapsed: ",end_time - start_time,"s")





