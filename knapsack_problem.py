# -*- coding:utf-8 -*-
"""
0/1背包问题
给定n个
重量为w1、w2、w3、…、wn，
价值为v1、 v2、v3、 …、vn
的物品
和
容量为C的背包，

求这个物品中一个最有价值的子集，使得在满足背包的容量的前提下，包内的总价值最大.

"""
from typing import List

import numpy as np


class Solution:
    def knapsack_01(self, w_list: List[int], v_list: List[int], c: int) -> int:
        """
        建立价值和重量表
        不放i-1: dp[i][j] = dp[i-1][w]
        放i-1: dp[i][j] = dp[i-1][j-w[i]] + v[i]
        在“上一个结果价值”和“把当前第i个物品装入背包里所得到价值”二者里选价值较大的
        :param w:
        :param v:
        :param c:
        :return:
        """
        dp = [[0 for _ in range(c+1)] for _ in range(len(w_list))]
        for i in range(1, len(w_list)):  # 跳过0
            for j in range(1, c+1):
                if w_list[i] > j:  # 外层循环i,如果第i个物品质量大于当前背包容量
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w_list[i]] + v_list[i])
        return dp[-1][-1]


if __name__ == '__main__':
    v = [0, 60, 100, 120]
    w = [0, 10, 20, 30]
    c = 50  # 最重不超过50
    s = Solution()
    print(s.knapsack_01(w, v, c))

