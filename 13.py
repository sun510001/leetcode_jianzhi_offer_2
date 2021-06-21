# -*- coding:utf-8 -*-
"""
剑指 Offer 13. 机器人的运动范围

地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，
因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
输入：m = 2, n = 3, k = 1
输出：3

示例 2：
输入：m = 3, n = 1, k = 0
输出：1

提示：
1 <= n,m <= 100
0 <= k <= 20
"""


class Solution:
    # def movingCount(self, m: int, n: int, k: int) -> int:
    #     """
    #     机器人只能连续运动
    #     dfs
    #     :param m:
    #     :param n:
    #     :param k:
    #     :return:
    #     """
    #     self.visited = [[0 for _ in range(n)] for _ in range(m)]
    #
    #     def bitsum(n: int) -> int:
    #         sum = 0
    #         while n > 0:
    #             sum += n % 10
    #             n //= 10
    #         return sum
    #
    #     def dfs(i, j):
    #         if i >= m or j >= n or bitsum(i) + bitsum(j) > k or self.visited[i][j] == 1:
    #             return 0
    #         self.visited[i][j] = 1
    #         return 1 + dfs(i, j + 1) + dfs(i + 1, j)
    #
    #     return dfs(0, 0)

        def movingCount(self, m: int, n: int, k: int) -> int:
            """
            bfs
            :param m:
            :param n:
            :param k:
            :return:
            """
            self.visited = [[0 for _ in range(n)] for _ in range(m)]
            self.result = 0
            queue = [(0, 0)]

            def bitsum(n: int) -> int:
                sum = 0
                while n > 0:
                    sum += n % 10
                    n //= 10
                return sum

            while queue:
                i, j = queue.pop()
                if i >= m or j >= n or bitsum(i) + bitsum(j) > k or self.visited[i][j] == 1:
                    continue
                self.visited[i][j] = 1
                self.result += 1
                queue.append((i, j + 1))
                queue.append((i + 1, j))

            return self.result


if __name__ == '__main__':
    m = 1
    n = 2
    k = 0
    s = Solution()
    out = s.movingCount(m, n, k)
    print(out)
