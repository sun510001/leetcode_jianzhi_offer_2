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
        arr[0]作为目标, 之后的ele, if ele<arr[0]就放
        :param arr:
        :param k:
        :return:
        """

if __name__ == '__main__':
    arr = [3, 5, 6, 2, 1]
    k = 4
    s = Solution()
    out = s.getLeastNumbers2(arr, k)
    print(out)
