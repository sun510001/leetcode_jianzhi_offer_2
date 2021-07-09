# -*- coding:utf-8 -*-
"""
LCP 07. 传递信息
小朋友 A 在和 ta 的小伙伴们玩传信息游戏，游戏规则如下：

有 n 名玩家，所有玩家编号分别为 0 ～ n-1，其中小朋友 A 的编号为 0
每个玩家都有固定的若干个可传信息的其他玩家（也可能没有）。传信息的关系是单向的（比如 A 可以向 B 传信息，但 B 不能向 A 传信息）。
每轮信息必须需要传递给另一个人，且信息可重复经过同一个人
给定总玩家数 n，以及按 [玩家编号,对应可传递玩家编号] 关系组成的二维数组 relation。
返回信息从小 A (编号 0 ) 经过 k 轮传递到编号为 n-1 的小伙伴处的方案数；若不能到达，返回 0。

示例 1：
输入：n = 5, relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], k = 3
输出：3
解释：信息从小 A 编号 0 处开始，经 3 轮传递，到达编号 4。共有 3 种方案，分别是 0->2->0->4， 0->2->1->4， 0->2->3->4。

示例 2：
输入：n = 3, relation = [[0,2],[2,1]], k = 2
输出：0
解释：信息不能从小 A 处经过 2 轮传递到编号 2

限制：
2 <= n <= 10
1 <= k <= 5
1 <= relation.length <= 90, 且 relation[i].length == 2
0 <= relation[i][0],relation[i][1] < n 且 relation[i][0] != relation[i][1]
"""
from collections import deque
from typing import List


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        """
        创建表, dfs
        最大的编号为n-1, 经过k轮
        :param n:
        :param relation:
        :param k:
        :return:
        """
        dic = {}
        for i in range(n):
            dic[i] = set()  # 创建字典, 字典的元素是set类型
        for each in relation:
            dic[each[0]].add(each[1])  # 遍历relation列表, 当前编号作为索引, 目标编号加入set

        def dfs(d, j):
            """
            :param d: 深度
            :param j: 当前索引
            :return:
            """
            if d == k:  # 到达深度k
                if n - 1 == j:  # 如果目标编号等于结果
                    return 1  # 返回1
                else:
                    return 0
            tmp = 0
            for each_j in dic[j]:
                tmp += dfs(d + 1, each_j)  # 父节点累加子节点的结果
            return tmp

        return dfs(0, 0)

    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        """
        创建表, bfs
        最大的编号为n-1, 经过k轮
        :param n:
        :param relation:
        :param k:
        :return:
        """
        dic = {}
        for i in range(n):
            dic[i] = set()  # 创建字典, 字典的元素是set类型
        for each in relation:
            dic[each[0]].add(each[1])  # 遍历relation列表, 当前编号作为索引, 目标编号加入set

        queue = deque([0])  # 队列存放起始节点
        tmp_k = 0
        while queue and tmp_k < k:
            for i in range(len(queue)):  # 循环当前长度的queue, 循环结束后剩下这次循环中添加的项
                val = queue.popleft()  # 队列最左边元素出队, 当前编号
                to = dic[val]  # 目标编号
                for next_num in to:
                    queue.append(next_num)  # 目标编号入队
            tmp_k += 1
        result = 0
        for ele in queue:  # 结果中找答案为n-1的结果
            if ele == n - 1:
                result += 1
        return result

    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        """
        dp, 假设当前已经走了i步, 所在位置为j, 那么问题就变成了走k-i步, 能否到达n-1.
        就可以反推, 从走0步, 到达0.成立
        这就是 无后效性 问题
        定义f[i][j]=y, 走了i步, 位置为j的方案数为y,
        那么最终答案为f[k][n-1]=y_t,
        f[0][0]=1为起点.
        所以f[i][j]=能达到位置j的点p的f[i-1][p]的方案数总和.

        :param n:
        :param relation:
        :param k:
        :return:
        """
        dic = {}
        for i in range(n):
            dic[i] = set()  # 创建字典, 字典的元素是set类型
        for each in relation:
            dic[each[0]].add(each[1])  # 遍历relation列表, 当前编号作为索引, 目标编号加入set

        dp = [[0 for _ in range(n)] for _ in range(k + 1)]
        dp[0][0] = 1
        for i in range(1, k + 1):
            for p in range(n):
                for j in dic[p]:
                    dp[i][j] += dp[i - 1][p]
        return dp[k][n - 1]


if __name__ == '__main__':
    n = 5
    relation = [[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]]
    k = 3
    s = Solution()
    print(s.numWays(n, relation, k))
