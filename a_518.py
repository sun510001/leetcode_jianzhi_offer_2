# -*- coding:utf-8 -*-
"""
518. 零钱兑换 II
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。

示例 1:
输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

示例 2:
输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。

示例 3:
输入: amount = 10, coins = [10]
输出: 1

注意:
你可以假设：
0 <= amount (总金额) <= 5000
1 <= coin (硬币面额) <= 5000
硬币种类不超过 500 种
结果符合 32 位符号整数
"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        硬币无限
        x = amount
        y = coins
        :param amount:
        :param coins:
        :return:
        """
        # dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
        # for j in range(amount+1):  # 总金额
        #     for i in range(0, len(coins)):  # 硬币数
        #         if j == 0:
        #             dp[i][j] = 1  # 选一种硬币时
        #         else:
        #             dp[i][j] += dp[i-1][j]
        #             if j >= coins[i]:
        #                 dp[i][j] += dp[i][j-coins[i]]
        # return dp[-1][-1]

        dp = [1] + [0] * amount
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[-1]


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    s = Solution()
    out = s.change(amount, coins)
    print(out)