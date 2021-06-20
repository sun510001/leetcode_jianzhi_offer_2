# -*- coding:utf-8 -*-
"""
剑指 Offer 53 - I. 在排序数组中查找数字 I
统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

限制：
0 <= 数组长度 <= 50000
注意：本题与主站 34 题相同（仅返回值不同）：
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        遍历
        :param nums:
        :param target:
        :return:
        """
        tmp = 0
        for ele in nums:
            if ele == target:
                tmp += 1
        return tmp

    def search(self, nums: List[int], target: int) -> int:
        """
        排序树组, 所以可以用两次二分查找, 寻找左边界target-1和右边界target
        如果最后一个数是target,找右边界时 i 必须等于 j, 所以while i<=j

        :param nums: 
        :param target: 
        :return: 
        """

        def find_target(target):
            i, j = 0, len(nums)-1
            while i <= j:
                mid = (i + j) // 2
                if nums[mid] <= target:
                    i = mid + 1
                else:
                    j = mid - 1
            return i
        return find_target(target) - find_target(target-1)


if __name__ == '__main__':
    input = [5, 7, 7, 8]
    t = 7
    s = Solution()
    out = s.search(input, t)
    print(out)
