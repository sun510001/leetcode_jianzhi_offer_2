# -*- coding:utf-8 -*-

"""
编写一个高效的算法来判断m x n矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false

"""

from typing import List


class Solution:
    @classmethod
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # def search(m_list, target):
        #     for ele in m_list:
        #         if target == ele:
        #             return True
        #     return False
        #
        # for i in range(0, len(matrix)):
        #     if matrix[i][-1] > target:
        #         return search(matrix[i], target)
        #     elif matrix[i][-1] == target:
        #         return True
        # return False

        """binary search"""
        if len(matrix) == 0:
            return False
        row = len(matrix)
        col = len(matrix[0])
        # left = 0
        # right = row * left - 1
        # c_row = i // col  # current index of row
        # c_col = i % col  # current index of column

        left = 0
        right = row * col - 1
        while left <= right:
            mid = (right + left) // 2
            if target == matrix[mid // col][mid % col]:
                return True
            elif target > matrix[mid // col][mid % col]:
                left = mid + 1
            else:
                right = mid - 1
        return False




if __name__ == '__main__':
    matrix = []
    target = 3
    out = Solution.searchMatrix(matrix, target)
    print(out)
