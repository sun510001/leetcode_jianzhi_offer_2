# -*- coding:utf-8 -*-
"""
149. 直线上最多的点数
给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。
求最多有多少个点在同一条直线上。


示例 1：
输入：points = [[1,1],[2,2],[3,3]]
输出：3

示例 2：
输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出：4

提示
1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
points 中的所有点互不相同
"""
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        三个点, 两次两点斜率相同就算重合
        [[p1],[p2],[p3]]
        y1-y2=a1(x1-x2)
        y1-y3=a2(x1-x3)
        if a1=a2
        -> (y1-y2)(x1-x3)=(y1-y3)(x1-x2)
        三点一线
        T(n^3), S(1)
        :param points:
        :return:
        """
        length = len(points)
        result = 1
        for i in range(0, length):
            p1 = points[i]
            for j in range(i + 1, length):
                p2 = points[j]
                tmp = 2
                for k in range(j + 1, length):
                    p3 = points[k]
                    if (p1[1] - p2[1]) * (p1[0] - p3[0]) == (p1[1] - p3[1]) * (p1[0] - p2[0]):
                        tmp += 1
                result = max(result, tmp)
        return result


if __name__ == '__main__':
    points = [[0,0], [2,2]]
    s = Solution()
    out = s.maxPoints(points)
    print(out)
