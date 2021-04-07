# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def minimumTotal(triangle: List[List[int]]) -> int:
        for r in range(len(triangle) - 2, -1, -1):
            for c in range(len(triangle[r])):
                triangle[r][c] += min(triangle[r + 1][c:c + 2])
        return triangle[0][0]


if __name__ == '__main__':
    input = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    listnode = Solution.minimumTotal(input)
    print(listnode)
