# -*- coding:utf-8 -*-
"""
剑指 Offer 03. 数组中重复的数字
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3


限制：

2 <= n <= 100000
"""
from typing import List


class Solution:
    def findRepeatNumber(nums: List[int]) -> int:
        """hashmap T(n)=O(n); S(n)=O(n)"""
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return num
            hashmap[num] = 1

    def findRepeatNumber_2(nums: List[int]) -> int:
        """replace T(n)=O(n); S(n)=O(1)"""
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp


if __name__ == '__main__':
    input = [4, 3, 1, 0, 2, 5, 3]
    output = Solution.findRepeatNumber_2(input)
    print(output)