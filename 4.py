# -*- coding:utf-8 -*-
"""
剑指 Offer 04. 二维数组中的查找
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。



示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。



限制：

0 <= n <= 1000

0 <= m <= 1000
"""
from typing import List


class Solution:
    def findNumberIn2DArray(matrix: List[List[int]], target: int) -> bool:
        """
        T(n) = O(n)
        S(n) = O(n)
        :param target:
        :return:
        """
        i = len(matrix) - 1  # the max index of row
        j = 0
        while i >= 0 and j < len(matrix[0]):  # len(matrix[0]): the length of column
            if matrix[i][j] > target:  # reduce by a column
                i -= 1
            elif matrix[i][j] < target:  # increase by a row
                j += 1
            else:
                return True
        return False


if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    input = 31
    output = Solution.findNumberIn2DArray(matrix, input)
    print(output)
