# -*- coding:utf-8 -*-

"""
剑指 Offer 29. 顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。



示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]


限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
"""

"""
分析
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
1, 2, 3, 4
5, 6, 7, 8
9,10,11,12
[1,2,3,4,8,12,11,10,9,5,6,7]
顺时针螺旋向内

T(n), S(1)
扫描一次, 扫描过的置空.(限制没说数字是否为负数,不能置-1)
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        初见
        :param matrix:
        :return:
        """
        result = []
        if len(matrix) == 0: return []
        len_row = len(matrix[0])
        len_col = len(matrix)
        cur_status = 3
        cur_x = 0
        cur_y = 0
        break_out = 1

        def right(cur_x, cur_y):
            break_out = 0
            for i in range(cur_y, len_row):  # 从当前节点开始扫描, 跳过之前的None
                if matrix[cur_x][i] == None:
                    break  # 跳过之后的None
                else:
                    result.append(matrix[cur_x][i])
                    matrix[cur_x][i] = None  # 扫描过的节点置空
                    cur_y = i
                    break_out = 1  # 1表示有更新, 返回0说明已经达到中心点.
            cur_status = 0
            return cur_y, cur_status, break_out

        def left(cur_x, cur_y):
            break_out = 0
            for i in range(cur_y, -1, -1):
                if matrix[cur_x][i] == None:
                    break
                else:
                    result.append(matrix[cur_x][i])
                    matrix[cur_x][i] = None
                    cur_y = i
                    break_out = 1
            cur_status = 2
            return cur_y, cur_status, break_out

        def down(cur_x, cur_y):
            break_out = 0
            for i in range(cur_x, len_col):
                if matrix[i][cur_y] == None:
                    break
                else:
                    result.append(matrix[i][cur_y])
                    matrix[i][cur_y] = None
                    cur_x = i
                    break_out = 1
            cur_status = 1
            return cur_x, cur_status, break_out

        def up(cur_x, cur_y):
            break_out = 0
            for i in range(cur_x, -1, -1):
                if matrix[i][cur_y] == None:
                    break
                else:
                    result.append(matrix[i][cur_y])
                    matrix[i][cur_y] = None
                    cur_x = i
                    break_out = 1
            cur_status = 3
            return cur_x, cur_status, break_out

        while break_out != 0:
            if cur_status == 3:
                cur_y, cur_status, break_out = right(cur_x, cur_y)
                cur_x += 1
            elif cur_status == 0:
                cur_x, cur_status, break_out = down(cur_x, cur_y)
                cur_y -= 1
            elif cur_status == 1:
                cur_y, cur_status, break_out = left(cur_x, cur_y)
                cur_x -= 1
            elif cur_status == 2:
                cur_x, cur_status, break_out = up(cur_x, cur_y)
                cur_y += 1

        return result

    def spiralOrder_2(self, matrix: List[List[int]]) -> List[int]:
        """
        简单方法
        动态规划, 不撞墙方法, 每次遍历完就减一和改方向
        规定边界
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
                t
             1, 2, 3, 4
         l   5, 6, 7, 8 r
             9,10,11,12
                b
        [1,2,3,4,8,12,11,10,9,5,6,7]
        :param matrix:
        :return:
        """
        if len(matrix) == 0: return []
        l = 0
        r = len(matrix[0]) - 1
        b = len(matrix) - 1
        t = 0
        result = []
        while True:
            for i in range(l, r + 1):  # left -> right
                result.append(matrix[t][i])
            t += 1
            if t > b: break
            for i in range(t, b + 1):  # up -> down
                result.append(matrix[i][r])
            r -= 1
            if r < l: break
            for i in range(r, l - 1, -1):  # right -> left
                result.append(matrix[b][i])
            b -= 1
            if b < t: break
            for i in range(b, t - 1, -1):  # down -> up
                result.append(matrix[i][l])
            l += 1
            if l > r: break

        return result


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    s = Solution()
    out = s.spiralOrder_2(matrix)
    print(out)
