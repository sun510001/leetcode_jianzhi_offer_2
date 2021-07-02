# -*- coding:utf-8 -*-
"""
1833. 雪糕的最大数量
夏日炎炎，小男孩 Tony 想买一些雪糕消消暑。
商店中新到 n 支雪糕，用长度为 n 的数组 costs 表示雪糕的定价，其中 costs[i] 表示第 i 支雪糕的现金价格。
Tony 一共有 coins 现金可以用于消费，他想要买尽可能多的雪糕。
给你价格数组 costs 和现金量 coins ，请你计算并返回 Tony 用 coins 现金能够买到的雪糕的 最大数量 。
注意：Tony 可以按任意顺序购买雪糕。

示例 1：
输入：costs = [1,3,2,4,1], coins = 7
输出：4
解释：Tony 可以买下标为 0、1、2、4 的雪糕，总价为 1 + 3 + 2 + 1 = 7
示例 2：
输入：costs = [10,6,8,7,7,8], coins = 5
输出：0
解释：Tony 没有足够的钱买任何一支雪糕。
示例 3：
输入：costs = [1,6,3,1,2,5], coins = 20
输出：6
解释：Tony 可以买下所有的雪糕，总价为 1 + 6 + 3 + 1 + 2 + 5 = 18 。

提示：
costs.length == n
1 <= n <= 105
1 <= costs[i] <= 105
1 <= coins <= 108
"""
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """
        不能重复购买
        先排序costs
        优先从便宜的购买
        :param costs: 雪糕价格表
        :param coins: 手头的现金
        :return: 能买到的最多雪糕数
        """
        cost_s = sorted(costs)
        ans = 0
        for i in range(len(cost_s)):
            if coins >= cost_s[i]:
                coins -= cost_s[i]
                ans += 1
        return ans

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """
        二分排序
        :param costs:
        :param coins:
        :return:
        """

        def select_sort(l):
            """

            :param l: 需要排序的列
            :return: 有序列
            """
            for i in range(len(l) - 1):
                min_index = i
                for j in range(i + 1, len(l)):
                    if l[min_index] > l[j]:
                        min_index = j
                        l[i], l[min_index] = l[min_index], l[i]
            return l

        cost_s = select_sort(costs)
        ans = 0
        for i in range(len(cost_s)):
            if coins >= cost_s[i]:
                coins -= cost_s[i]
                ans += 1
        return ans


if __name__ == '__main__':
    input = [1, 3, 2, 4, 1]
    coin = 7
    s = Solution()
    print(s.maxIceCream(input, coin))
