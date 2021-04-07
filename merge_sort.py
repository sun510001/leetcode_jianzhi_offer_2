# -*- coding:utf-8 -*-
import copy
import random


class MergeSort:
    @classmethod
    def merge(self, li, low, mid, high):
        left = low
        right = mid + 1
        temp_list = []
        while left <= mid and right <= high:
            if li[left] < li[right]:
                temp_list.append(li[left])
                left += 1
            else:
                temp_list.append(li[right])
                right += 1
        # if left <= mid:
        #     temp_list += li[left:mid + 1]
        # else:
        #     temp_list += li[right:len(li)]
        while left <= mid:
            temp_list.append(li[left])
            left += 1
        while right <= high:
            temp_list.append(li[right])
            right += 1

        li[low:high + 1] = temp_list

    @classmethod
    def merge_sort(self, li, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(li, low, mid)
            self.merge_sort(li, mid + 1, high)
            self.merge(li, low, mid, high)

    @classmethod
    def merge_sort_test(self, li, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge_sort_test(li, low, mid)
            self.merge_sort_test(li, mid + 1, high)
            print(li[low:high+1])


if __name__ == '__main__':
    li = [i for i in range(10)]
    random.shuffle(li)
    # li = [2, 4, 5, 7, 1, 3, 6, 8]
    li_temp = copy.deepcopy(li)
    print(li_temp)
    # out = merge(li_temp, 0, 3, 7)
    MergeSort.merge_sort(li_temp, 0, len(li_temp) - 1)
    print(li_temp)
    # print(li_temp[:len(li)])
