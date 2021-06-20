# -*- coding:utf-8 -*-
"""
剑指 Offer 53 - II. 0～n-1中缺失的数字
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1
输入: [0,1,3]
输出: 2

示例 2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8

限制：
1 <= 数组长度 <= 10000
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if nums[0] == 1:
            return 0
        for i in range(len(nums)):
            if i == 0:
                tmp = nums[i]
            else:
                tmp += 1
                if tmp != nums[i]:
                    return tmp
        if nums[0] != 1:
            return nums[-1] + 1

    def missingNumber(self, nums: List[int]) -> int:
        """
        用下标
        :param nums:
        :return:
        """
        if nums[0] == 1: return 0
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

    def missingNumber(self, nums: List[int]) -> int:
        """
        二分查找
        :param nums:
        :return:
        """
        if nums[0] == 1: return 0
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == mid:
                i = mid + 1  # [0, 1] ->i = 2
            else:
                j = mid - 1
        return i


if __name__ == '__main__':
    input = [0, 1, 2, 3, 4, 5, 6, 7]
    s = Solution()
    print(s.missingNumber(input))
