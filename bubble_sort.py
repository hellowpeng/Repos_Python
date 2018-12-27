#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import datetime

def random_list(start,stop,length):
    if length >= 0:
        length=int(length)
        start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
        r_list = []
        print("正在构造随机数组，数组长度：",length)
        s_time = datetime.datetime.now()
        for i in range(length):
            r_list.append(random.randint(start, stop))
        print("数组构造完成，耗时：",(datetime.datetime.now() - s_time).microseconds/1000,"ms")
        return r_list

def Bubble_Sort(alist):
    count = 0 # 初始化排序轮数
    flag = 1 # 初始化排序标志，1 表示可能需要下一轮排序 0 表示不需要
    for j in range(len(alist)):
        if flag != 0:
            flag = 0 # 每一轮排序开始之前，将排序标志重置为0
            # 计数
            count += 1
            for i in range(len(alist)-1):
                if alist[i] > alist[i+1]:
                    alist[i],alist[i+1] = alist[i+1],alist[i]
                    flag = 1
        else:
            break
    return count-1


if __name__=="__main__":
    list1 = random_list(1, 2000, 1000)
    print("排序前：",list1)
    start_time = datetime.datetime.now()
    Sort_Count = Bubble_Sort(list1)
    print("排序后：",list1)
    print("排序次数：",Sort_Count)
    print("耗时：",(datetime.datetime.now() - start_time).microseconds/1000,"ms")
