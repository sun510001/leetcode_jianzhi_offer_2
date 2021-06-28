# -*- coding:utf-8 -*-
"""
815. 公交路线
给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。
例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... 这样的车站路线行驶。
现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。
求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。

示例 1：
输入：routes = [[1,2,7],[3,6,7]], source = 1, target = 6
输出：2
解释：最优策略是先乘坐第一辆公交车到达车站 7 , 然后换乘第二辆公交车到车站 6 。
示例 2：
输入：routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
输出：-1

提示：
1 <= routes.length <= 500.
1 <= routes[i].length <= 105
routes[i] 中的所有值 互不相同
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106
"""
from collections import defaultdict
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        每个route都可以循环: index = i % len(route)
        能换车的站点可换可不换
        每个step: 每乘一辆车, step内:换乘: 记录可能的换乘线的除当前站点外的所有站点, 不换乘: 当前线的所有站(除当前站)
        记录: 乘坐过的站点
        count: 坐上车或换乘就加1
        BFS
        超时
        :param routes:
        :param source:
        :param target:
        :return:
        """

        def ride_or_change(cur: int) -> set:
            """
            根据当前站计算出可能的下一站.
            :param cur:
            :return:
            """
            result = set()
            for i, value in enumerate(routes):
                if cur in value:
                    for stop in value:
                        if stop != cur and stop not in self.visited:
                            result.add(stop)
                            self.visited.add(stop)
            return result

        if source == target: return 0  # 起点就在目标站时直接返回0
        self.visited = set()
        self.visited.add(source)  # 记录乘坐过的站点
        stack = [source]  # 保存可能乘坐的站点
        step = 0

        while stack:
            size = len(stack)
            for i in range(size):
                current = stack.pop(0)
                stack += ride_or_change(current)
            print(stack)
            if target in stack:  # 如果可能的下一站中存在目标站点
                return step + 1
            else:
                step += 1
        return -1

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        建图

        :param routes:
        :param source:
        :param target:
        :return:
        """
        if source == target: return 0
        s2r = defaultdict(list)
        for index, value in enumerate(routes):
            for id in value:
                s2r[id].append(index)  # 记录
        graph = [set() for _ in range(len(routes))]
        for adj_routes in filter(lambda l: len(l) > 1, s2r.values()):  # 遍历每个站点经过的线路（筛选至少有两条线路的站点）
            for i, route_i in enumerate(adj_routes):  # 相邻线路之间构造邻接表
                graph[route_i] |= set(adj_routes[:i] + adj_routes[i + 1:])  # python的set类， | 代表并集运算

        step = 0
        target_route = set(s2r[target])
        queue = set(s2r[source])
        visited = set()
        while queue:
            step += 1
            if len(queue & target_route) > 0: return step
            queue2 = set()
            for route_i in queue:
                queue2 |= graph[route_i]
            visited |= queue
            queue = queue2 - visited
        return -1


if __name__ == '__main__':
    route = [[1,2,7],[3,6,7]]
    source = 1
    target = 6
    s = Solution()
    print(s.numBusesToDestination(route, source, target))
