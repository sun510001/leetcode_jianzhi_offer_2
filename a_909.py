# -*- coding:utf-8 -*-
"""
909. 蛇梯棋
N x N 的棋盘 board 上，按从 1 到 N*N 的数字给方格编号，编号 从左下角开始，每一行交替方向。

例如，一块 6 x 6 大小的棋盘，编号如下：
https://leetcode-cn.com/problems/snakes-and-ladders/
r 行 c 列的棋盘，按前述方法编号，棋盘格中可能存在 “蛇” 或 “梯子”；如果 board[r][c] != -1，那个蛇或梯子的目的地将会是 board[r][c]。
玩家从棋盘上的方格 1 （总是在最后一行、第一列）开始出发。

每一回合，玩家需要从当前方格 x 开始出发，按下述要求前进：
选定目标方格：选择从编号 x+1，x+2，x+3，x+4，x+5，或者 x+6 的方格中选出一个目标方格 s ，目标方格的编号 <= N*N。
该选择模拟了掷骰子的情景，无论棋盘大小如何，你的目的地范围也只能处于区间 [x+1, x+6] 之间。
传送玩家：如果目标方格 S 处存在蛇或梯子，那么玩家会传送到蛇或梯子的目的地。否则，玩家传送到目标方格 S。
注意，玩家在每回合的前进过程中最多只能爬过蛇或梯子一次：就算目的地是另一条蛇或梯子的起点，你也不会继续移动。
返回达到方格 N*N 所需的最少移动次数，如果不可能，则返回 -1。

示例：
输入：[
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
输出：4
解释：
首先，从方格 1 [第 5 行，第 0 列] 开始。
你决定移动到方格 2，并必须爬过梯子移动到到方格 15。
然后你决定移动到方格 17 [第 3 行，第 5 列]，必须爬过蛇到方格 13。
然后你决定移动到方格 14，且必须通过梯子移动到方格 35。
然后你决定移动到方格 36, 游戏结束。
可以证明你需要至少 4 次移动才能到达第 N*N 个方格，所以答案是 4。

提示：
2 <= board.length = board[0].length <= 20
board[i][j] 介于 1 和 N*N 之间或者等于 -1。
编号为 1 的方格上没有蛇或梯子。
编号为 N*N 的方格上没有蛇或梯子。
"""
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        解释:
        梯子和蛇不就是space warp嘛.
        中间的数字不是-1就是warp的index. index范围[1,n*n]
        走一步的步长范围[1,6]
        思路:
        不warp的话, 矩阵中走路的方向只有固定一个方向, 所以矩阵可以降维成列表.
        每个step, 走路的步数种类固定6种, 能warp就必须warp.
        记录走到的位置index, str格式
        BFS, 记录step数.
        :param board:
        :return:
        """

        def dimension_reduce(matrix: List[List[int]]) -> List[int]:
            result = []
            switch = 0  # 前进方向
            for i in range(len(matrix) - 1, -1, -1):
                if switch == 0:
                    result += matrix[i]
                    switch = 1
                else:
                    result += reversed(matrix[i])
                    switch = 0
            return result

        if board[len(board)-1][0] == len(board) * len(board):
            # 如果起点就能warp到goal, 直接return
            return 0
        map = dimension_reduce(board)
        cur_point = 1  # 当前位置
        stack = [cur_point]  # 当前step的走动位置选择
        visited = set()  # 已走过的位置
        visited.add(cur_point)
        step = 0
        goal = len(map)  # 目标位置
        while stack:
            size = len(stack)
            for i in range(size):
                point = stack.pop(0)
                for j in range(1, 7):  # 每一个step有6种走法
                    tmp_cur_point = point + j  # 当前位置
                    if tmp_cur_point <= goal:
                        if map[tmp_cur_point - 1] != -1:  # warp
                            tmp_cur_point = map[tmp_cur_point - 1]
                        if tmp_cur_point not in visited:
                            visited.add(tmp_cur_point)  # 记录走过的点
                            stack.append(tmp_cur_point)  # 保存下一个step的点
            if goal in stack:
                return step + 1
            else:
                step += 1
            print(stack)
        return -1


if __name__ == '__main__':
    input = [[-1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, 35, -1, -1, 13, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1]]
    s = Solution()
    print(s.snakesAndLadders(input))
