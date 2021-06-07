# -*- coding:utf-8 -*-
"""
494. 目标和
给你一个整数数组 nums 和一个整数 target 。
向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

示例 1：
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

示例 2：
输入：nums = [1], target = 1
输出：1

提示：
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 100
"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        dfs
        :param nums:
        :param target:
        :return:
        """
        d = {}

        def dfs(cur, i, d):
            if i < len(nums) and (cur, i) not in d:  # 搜索周围节点
                d[(cur, i)] = dfs(cur + nums[i], i + 1, d) + dfs(cur - nums[i], i + 1, d)
            return d.get((cur, i), int(cur == target))

        return dfs(0, 0, d)

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        """
        使用一个 dp 数组，其中 dp[i][j] 表示到第 i 个数字且和为j的情况总数
        dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]
        length = (2 * target) + 1
        dp Table
          -5 -4 -3 -2 -1  0  1  2  3  4  5
        1  0  0  0  0  1  0  1  0  0  0  0
        1  0  0  0  1  0  2  0  1  0  0  0
        1  .......
        1
        1

        """
        n = len(nums)
        sumation = 0
        for num in nums:
            sumation += num
        if abs(sumation) < abs(target): return 0
        length = (2 * sumation) + 1
        dp = [[0 for _ in range(length)] for _ in range(n)]
        dp[0][sumation + nums[0]] = 1
        dp[0][sumation - nums[0]] += 1
        for i in range(1, n):
            for j in range(length):
                l = dp[i - 1][j - nums[i]] if 0 <= j - nums[i] < length else 0
                r = dp[i - 1][j + nums[i]] if 0 <= j + nums[i] < length else 0
                dp[i][j] = l + r
        return dp[n - 1][sumation + target]


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    target = 3
    s = Solution()
    out = s.findTargetSumWays2(nums, target)
    print(out)
