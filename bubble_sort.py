#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import time
tup1 = (6,9,4,2,5,1,3,8)
flag = 1 #初始化排序标志，1 标识可能需要继续下一轮排序 0 标识不需要
count = 0
#print("tup1[0]: ",tup1[0])

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




if __name__=="__main__":
    list1 = random_list(1, 1000, 500)
    # print(list1)
    start_time = time.time()
    for j in range(len(list1)-1):
        # 根据上一趟的排序结果判断是否有必要进行下一趟排序
        if flag != 0 :
            # 开始计数
            count = count + 1
            # 每趟开始前，将排序标志重置为0
            flag = 0
            for i in range(len(list1)-1):
                if list1[i] > list1[i+1]:
                    list1[i],list1[i+1] = list1[i+1],list1[i]
                    flag = 1 #标识可能需要进行下一趟排序
                else:
                    # print("do nothing")
                    continue
        else:
            break

    # for i in list1:
    #     print(i)

    end_time = time.time()

    # print(list1)
    #print("total numbers: ",len(list1))
    #print("sort times: ",count-1)
    print("time elapsed: ",end_time - start_time,"s")



