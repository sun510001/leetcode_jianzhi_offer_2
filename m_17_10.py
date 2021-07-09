# -*- coding:utf-8 -*-
"""
面试题 17.10. 主要元素
数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 -1 。请设计时间复杂度为 O(N) 、空间复杂度为 O(1) 的解决方案。

示例 1：
输入：[1,2,5,9,5,9,5,5,5]
输出：5

示例 2：
输入：[3,2]
输出：-1

示例 3：
输入：[2,2,1,1,1,2,2]
输出：2
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        投票法
        找最多的元素, 有重复元素就+1, 与当前元素不同就-1.
        最后结果>0, 则该数为主要元素
        :param nums:
        :return:
        """
        res = -1  # 记录重复元素
        count = 0  # 记录重复元素出现次数
        for each in nums:
            if count == 0:
                res = each
            if each == res:  # 与当前元素相同count就+1
                count += 1
            else:  # 不同就-1
                count -= 1

        return res if count > 0 and nums.count(res) > len(nums) // 2 else -1  # 得到的主要元素再遍历一遍列表, 确实超过半数就输出.


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    sol = Solution()
    print(sol.majorityElement(nums))
