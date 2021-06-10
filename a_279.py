# -*- coding:utf-8 -*-
"""
279. 完全平方数
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例 1：
输入：n = 12
输出：3
解释：12 = 4 + 4 + 4

示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9

提示：
1 <= n <= 104
"""


class Solution:
    def numSquares(self, n: int) -> int:
        """
        完全背包问题, list内数字可重复选择
        W = squ_list
        N = len(squ_list)
        C = n
        dp记录个数
        :param n:
        :return:
        """
        squ_list = []
        res = 1
        while True:
            res_tmp = res ** 2
            res += 1
            if res_tmp < n:
                squ_list.append(res_tmp)
            else:
                break
        if res_tmp == n:
            return 1
        dp = [x for x in range(0, n+1)]  # 1,2,3,4,5,6  -> 初始状态个数累加(最初都是1累加)
        for i in range(1, len(squ_list)+1):
            for j in range(squ_list[i-1], n+1):
                dp[j] = min(dp[j], dp[j-squ_list[i-1]]+1)
        return dp[-1]


if __name__ == '__main__':
    input = 6
    s = Solution()
    out = s.numSquares(input)
    print(out)