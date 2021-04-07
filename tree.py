# -*- coding:utf-8 -*-

import copy
import heapq
import random

from my_lib import cal_time


class heap:
    @classmethod
    def sift(self, li, low, high):
        """
        heap creating and sorting(ascending)
        :param li: list
        :param low: root
        :param high: the highest child node
        :return:
        """
        i = low
        j = 2 * i + 1  # the child of root
        tmp = li[low]
        while j <= high:
            if j + 1 <= high and li[j + 1] > li[j]:
                j = j + 1
            if li[j] > tmp:
                li[i] = li[j]
                i = j
                j = 2 * i + 1
            else:
                break
        li[i] = tmp

    @classmethod
    def sift_descend(self, li, low, high):
        """
        heap creating and sorting(descending)
        :param li: list
        :param low: root
        :param high: the highest child node
        :return:
        """
        i = low
        j = 2 * i + 1  # the child of root
        tmp = li[low]
        while j <= high:
            if j + 1 <= high and li[j + 1] < li[j]:
                j = j + 1
            if li[j] < tmp:
                li[i] = li[j]
                i = j
                j = 2 * i + 1
            else:
                break
        li[i] = tmp

    @classmethod
    @cal_time
    def heap_sort(self, li):
        n = len(li)
        for i in range(n // 2 - 1, -1, -1):
            self.sift(li, i, n - 1)  # creat the heap
        # print(li)
        for i in range(n - 1, -1, -1):
            li[0], li[i] = li[i], li[0]
            self.sift(li, 0, i - 1)
        return li

    @cal_time
    def heap_lib(li):
        heapq.heapify(li)
        heapq_out = []
        for i in range(len(li)):
            heapq_out.append(heapq.heappop(li))
        return heapq_out

    @classmethod
    @cal_time
    def heap_topk(self, li, k):
        k_list = li[:k]
        for i in range(k // 2 - 1, -1, -1):
            self.sift_descend(k_list, i, k - 1)  # create the heap
        for i in range(k, len(li) - 1):
            if li[i] > k_list[0]:
                k_list[0] = li[i]
                self.sift_descend(k_list, 0, k - 1)  # sort
        for i in range(k - 1, -1, -1):
            k_list[0], k_list[i] = k_list[i], k_list[0]
            self.sift_descend(k_list, 0, i - 1)
        return k_list


if __name__ == '__main__':
    li = [i for i in range(100)]
    random.shuffle(li)
    li_temp = copy.deepcopy(li)
    out = heap.heap_sort(li_temp)
    print(out)

    """use heapq"""
    li_temp = copy.deepcopy(li)
    out = heap.heap_lib(li_temp)
    print(out)

    """topk"""
    li_temp = copy.deepcopy(li)
    out = heap.heap_topk(li_temp, 10)
    print(out)
