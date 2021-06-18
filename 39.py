# -*- coding:utf-8 -*-
"""
剑指 Offer 39. 数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

限制：
1 <= 数组长度 <= 50000
注意：本题与主站 169 题相同：https://leetcode-cn.com/problems/majority-element/
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        N > len(nums) // 2
        hashmap
        :param nums:
        :return:
        """
        dic = {}
        for i in range(0, len(nums)):
            if dic.get(nums[i]):
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
            if dic[nums[i]] >= (len(nums) // 2) + 1:
                return nums[i]

    def majorityElement(self, nums: List[int]) -> int:
        """
        摩尔投票法
        假定一个众数, 遇到非众数的-1, 遇到众数+1
        超过半数的那个数一定会剩下 => 结果一定>0
        :param nums:
        :return:
        """
        vote = 0
        rec = 0
        for x in nums:
            if vote == 0:
                rec = x
            if rec != x:
                vote -= 1
            else:
                vote += 1
        return rec


if __name__ == '__main__':
    input = [3, 3, 4]
    s = Solution()
    out = s.majorityElement(input)
    print(out)
