# -*- coding:utf-8 -*-
"""
剑指 Offer 61. 扑克牌中的顺子
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为0，可以看成任意数字。A 不能视为 14。

示例 1:
输入: [1,2,3,4,5]
输出: True

示例 2:
输入: [0,0,1,2,5]
输出: True

限制
数组长度为 5
数组的数取值为 [0, 13] .
"""
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        """
        先排序, 0的个数
        max - min < 5
        lucky_count = min_index
        :param nums:
        :return:
        """
        nums.sort()
        lucky_count = 0
        for i in range(4):
            if nums[i] == 0:
                lucky_count += 1
            elif nums[i] == nums[i+1]:
                return False
        return nums[4] - nums[lucky_count] < 5


if __name__ == '__main__':
    input = [1, 2, 3, 4, 5]
    s = Solution()
    print(s.isStraight(input))
