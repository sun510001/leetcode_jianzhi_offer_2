# -*- coding:utf-8 -*-
"""
416. 分割等和子集
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。

提示:
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        pos - neg = 0
        (sum - neg) - neg = 0
        neg = sum//2 整除
        :param nums:
        :return:
        """
        sums = sum(nums)
        if sums & 1 == 1:
            return False
        else:
            dp = [0 for _ in range(sums // 2 + 1)]
            for num in nums:
                for i in range(sums // 2, num - 1, -1):
                    dp[i] = max(dp[i], dp[i - num] + num)
        return True if sums-2*dp[-1] == 0 else False


if __name__ == '__main__':
    input = [2,2,1,2]
    s = Solution()
    out = s.canPartition(input)
    print(out)
