# -*- coding:utf-8 -*-
"""
剑指 Offer 57 - II. 和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：
输入：target = 9
输出：[[2,3,4],[4,5]]

示例 2：
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]

限制：
1 <= target <= 10^5
"""
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        """
        滑动窗口
        if
        窗口中元素和 < target:
            r += 1
        窗口元素和 > target:
            l += 1
        窗口元素和 = target:
            l += 1
            return list
        if l = r:
            return result
        :param target:
        :return:
        """
        l, r, s, result = 1, 2, 3, []
        while l != r:
            window_sum = sum(range(l, r + 1))
            if window_sum < target:
                r += 1
            elif window_sum > target:
                l += 1
            else:
                result.append([x for x in range(l, r + 1)])
                l += 1
        return result

    def findContinuousSequence(self, target: int) -> List[List[int]]:
        """
        求和公式
        窗口sum = 0.5*((i+j)*(j-i+1)) = target
        j_p = 0.5*(-1+(1+4*(i**2 - i + 2 * target))**0.5)
        x = (-b+-(b^2-4ac)^0.5)/2a
        1. j_p 正整数
        2. i < j
        :param target:
        :return:
        """
        result = []
        for i in range(1, target + 1):
            j = 0.5 * (-1 + (1 + 4 * (i ** 2 - i + 2 * target)) ** 0.5)
            if i < j and j == int(j):
                result.append(list(range(i, int(j) + 1)))
        return result


if __name__ == '__main__':
    input = 9
    s = Solution()
    out = s.findContinuousSequence(input)
    print(out)
