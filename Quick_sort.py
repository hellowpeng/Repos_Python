#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import random
import time


def random_list(start,stop,length):
    if length >= 0:
        length=int(length)
        start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
        r_list = []
        print("正在构造随机数组，数组长度：",length)
        # s_time = datetime.datetime.now()
        s_time = time.time()
        for i in range(length):
            r_list.append(random.randint(start, stop))
        # print("数组构造完成，耗时：",(datetime.datetime.now() - s_time).microseconds/1000,"ms")
        print("数组构造完成，耗时：",round(time.time() - s_time,3),"s")
        return r_list

def QuickSort(list,start,end):
    if start >= end:
        return
    pivot_index = start
    pivot = list[pivot_index]
    l_index = start
    r_index = end

    while r_index > l_index:
        # from right to left, search smaller than pivot
        while r_index > l_index:
            if list[r_index] < pivot:
                list[r_index],list[pivot_index] = list[pivot_index],list[r_index]
                pivot_index = r_index
                break
            r_index -= 1
        # from right to left, search bigger than pivot
        while r_index > l_index:
            if list[l_index] > pivot:
                list[l_index],list[pivot_index] = list[pivot_index],list[l_index]
                pivot_index = l_index
                break
            l_index += 1

    # recursive
    QuickSort(list,start,pivot_index-1)
    QuickSort(list,pivot_index+1,end)

def QuickSort2(list,start,end):

    if start >= end:
        return

    #取第一位作为基准值
    pivot_index = start
    pivot = list[pivot_index]
    l_index = start+1
    while l_index <= end:
        if list[l_index] < pivot:
            tmp = list[l_index]
            del list[l_index]
            list.insert(pivot_index,tmp)
            pivot_index += 1
        l_index += 1

    # 以上循环完成后，生成两段list，以pivot_index为分界点
    # 递归对这两段list做排序
    QuickSort2(list,start,pivot_index-1)
    QuickSort2(list,pivot_index+1,end)



# 验证一个数组是否有序
def check(list):
    l_index = 0
    while l_index <= len(list)-2:
        if list[l_index] > list[l_index+1]:
            return '验证失败'
        l_index += 1
    return '验证成功'

if __name__=="__main__":
    list1 = random_list(1, 1000000, 100000)
    # print("排序前：", list1)
    start_time = time.time()
    QuickSort(list1,0,len(list1)-1)
    # print("排序后：", list1)
    print("耗时：",round(time.time()-start_time,3),"s")
    print("结果：",check(list1))





