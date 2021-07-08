# -*- coding:utf-8 -*-
"""
930. 和相同的二元子数组
给你一个二元数组 nums ，和一个整数 goal ，
请你统计并返回有多少个和为 goal 的 非空 子数组。
子数组 是数组的一段连续部分。


示例 1:
输入：nums = [1,0,1,0,1], goal = 2
输出：4
解释：
如下面所示，有 4 个满足题目要求的子数组：
[[1,0,1],0,1]
[[1,0,1,0],1]
[1,[0,1,0,1]]
[1,0,[1,0,1]]

示例 2：
输入：nums = [0,0,0,0,0], goal = 0
输出：15

提示：
1 <= nums.length <= 3 * 10^4
nums[i] 不是 0 就是 1
0 <= goal <= nums.length
"""
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        双指针
        超时
        :param nums:
        :param goal:
        :return:
        """
        count = 0
        for i in range(len(nums) - 1):
            for j in range(1, len(nums)):
                tmp = sum(nums[i:j + 1]) - goal
                if tmp < 0:
                    continue
                elif tmp == 0:
                    count += 1
                else:
                    break
        return count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        双指针
        :param nums:
        :param goal:
        :return:
        """
        n = len(nums)
        ans = l1 = l2 = s1 = s2 = 0
        for r in range(n):  # r为右边界
            s1 += nums[r]
            s2 += nums[r]
            while l1 <= r and s1 > goal:
                s1 -= nums[l1]
                l1 += 1
            while l2 <= r and s2 >= goal:
                s2 -= nums[l2]
                l2 += 1
            ans += l2 - l1  # s2>=goal时, l2向右走; s1>goal时, l1向右走; l2 - l1是左边界间隔0的数量
        return ans


if __name__ == '__main__':
    nums = [1, 0, 1, 0, 1]
    goal = 2
    sol = Solution()
    print(sol.numSubarraysWithSum(nums, goal))
