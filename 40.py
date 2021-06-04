# -*- coding:utf-8 -*-
"""
剑指 Offer 40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]


限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000

"""
from typing import List

from my_lib import cal_time


class Solution:
    @cal_time
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        """
        先选arr[0:k], 找最大, 剩下的遍历一次,
        [1,3,5] 2. 最大值和current值对换
        S(1) T(n*k)
        :param arr:
        :param k:
        :return:
        """

        def max_num(arr, k):
            result = 0
            index = 0
            for i in range(k):
                if arr[i] > result:
                    result = arr[i]
                    index = i
            return result, index

        if k == 0:
            return []
        else:
            for i in range(k, len(arr)):
                max_result, index = max_num(arr, k)
                if arr[i] > max_result:
                    continue
                else:
                    arr[i], arr[index] = arr[index], arr[i]
        return arr[:k]

    @cal_time
    def getLeastNumbers2(self, arr: List[int], k: int) -> List[int]:
        """
        哨兵排序
        * 以数组某个元素（一般选取首元素）为 基准数, 将所有小于基准数的元素移动至其左边，大于基准数的元素移动至其右边。
        loop: i < j
            [6] 1 9 7 5 10 8
            i              j
            l              r
            loop: j向左找arr[j]>=6: j左移一格
            loop: i向右找arr[i]<=6: i右移一格
            -> i = 2; j = 4
            两数交换
            [6] 1 5 7 9 10 8
                  i   j
            l              r
            loop: j向左找arr[j]>=6: j左移一格
            loop: i向右找arr[i]<=6: i右移一格
            [6] 1 5 7 9 10 8
                 ij
            l              r
            在5相聚, arr[l]与arr[i]对换, 分成左右两个list->递归
            5 1 6 [7] 9 10 8
            i=j, 所以跳出循环
        递归: list_1 = [5, 1, 6]; list_2 = [9, 10, 8]
        :param arr:
        :param k:
        :return:
        """
        if k == 0:
            return []

        def quick_sort(l, r):
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]:
                    j -= 1
                while i < j and arr[i] <= arr[l]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            if k < i:
                # 代表第 k + 1 小的数字在 左子数组 中，则递归左子数组
                return quick_sort(l, i - 1)
            if k > i:
                # 代表第 k + 1 小的数字在 右子数组 中，则递归右子数组
                return quick_sort(i + 1, r)
            # 若 k = i ，代表此时 arr[k] 即为第 k + 1 小的数字，则直接返回数组前 k 个数字即可
            return arr[:k]

        return quick_sort(0, len(arr) - 1)


if __name__ == '__main__':
    arr = [3, 5, 6, 2, 1]
    k = 4
    s = Solution()
    out = s.getLeastNumbers2(arr, k)
    print(out)
