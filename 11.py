# -*- coding:utf-8 -*-
"""
剑指 Offer 11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

示例 1：
输入：[3,4,5,1,2]
输出：1

示例 2：
输入：[2,2,2,0,1]
输出：0

注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
"""
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        """
        原数组递增, 所以旋转之后, 最大的数之后必然是最小的数
        遇到后边的数小, 就输出. 没有就输出第一个.
        :param numbers:
        :return:
        """
        for i in range(1, len(numbers)):
            if numbers[i - 1] > numbers[i]:
                return numbers[i]
        return numbers[0]

    def minArray2(self, numbers: List[int]) -> int:
        """
        二分查找
        :param numbers:
        :return:
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                return min(numbers[i:j])
        return numbers[i]


if __name__ == '__main__':
    # input = [3, 1, 2]
    # input = [2, 2, 2, 0, 1]
    # input = [1]
    input = [3, 4, 5, 1, 2, 3]
    s = Solution()
    out = s.minArray2(input)
    print(out)
