# -*- coding:utf-8 -*-
"""
剑指 Offer 57. 和为s的两个数字
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]

示例 2：
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]

限制：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        暴力循环, 已经加过的丢弃
        T(n^2)
        S(1)
        超时
        :param nums:
        :param target:
        :return:
        """
        if len(nums) == 1:
            return []
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [nums[i], nums[j]]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        二分排序
        T(nlogn)
        :param nums:
        :param target:
        :return:
        """
        if len(nums) == 1:
            return []
        for i in range(0, len(nums) - 1):
            l = i + 1
            r = len(nums)
            while l < r:
                mid = (l + r) // 2
                if target > nums[mid] + nums[i]:
                    l = mid + 1
                elif target < nums[mid] + nums[i]:
                    r = mid
                else:
                    return [nums[i], nums[mid]]
        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        双指针, 向中间逼近
        T(n)
        :param nums:
        :param target:
        :return:
        """
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if target > s:
                i += 1
            elif target < s:
                j -= 1
            else:
                return [nums[i], nums[j]]
        return []


if __name__ == '__main__':
    input = [16, 16, 18, 24, 30, 32]
    t = 48
    s = Solution()
    out = s.twoSum(input, t)
    print(out)
