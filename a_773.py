# -*- coding:utf-8 -*-
"""
773. 滑动谜题
在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.
一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.
最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。

示例：
输入：board = [[1,2,3],[4,0,5]]
输出：1
解释：交换 0 和 5 ，1 步完成
输入：board = [[1,2,3],[5,4,0]]
输出：-1
解释：没有办法完成谜板
输入：board = [[4,1,2],[5,0,3]]
输出：5
解释：
最少完成谜板的最少移动次数是 5 ，
一种移动路径:
尚未移动: [[4,1,2],[5,0,3]]
移动 1 次: [[4,1,2],[0,5,3]]
移动 2 次: [[0,1,2],[4,5,3]]
移动 3 次: [[1,0,2],[4,5,3]]
移动 4 次: [[1,2,0],[4,5,3]]
移动 5 次: [[1,2,3],[4,5,0]]
输入：board = [[3,2,4],[1,5,0]]
输出：14
提示：
board 是一个如上所述的 2 x 3 的数组.
board[i][j] 是一个 [0, 1, 2, 3, 4, 5] 的排列.
"""
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
        broad = 4,1,2 (col=len(board[0])=3, row=len(board)=2)
                5,0,3
        只要找到最先使board等于[[1,2,3],[4,5,0]]的路即可
        BFS + 已遇到过的board整体记录
        出现重复就break当前方案
        正确答案中不存在 "012345" 只有 "123450"
        :param board:
        :return:
        """

        def list_to_str(l: List[int]) -> str:
            """
            convert broad list to string
            :param board:
            :return:
            """
            record = ''
            for each in l:
                record += str(each)
            return record

        def str_to_list(s: str) -> List[int]:
            """
            convert string to list
            :param board_str:
            :return:
            """
            l = [0] * len(s)
            for i in range(len(s)):
                l[i] = int(s[i])
            return l

        def simple_list(l):
            """
            二维改一维list
            :param l:
            :return:
            """
            return l[0] + l[1]

        def get_next_step(cur: tuple, cur_board: str):
            """
            cur是空档的位置, 计算下一步可能的走法
            :param cur: (x, y) 的下一步在broad里面
            :return:
            """
            tmp_step = []
            tmp_block = []
            cur_board = str_to_list(cur_board)
            if cur[0] != 0:  # 点cur不在第一行, 可以up
                cur_board[cur[0] * 3 + cur[1]], cur_board[(cur[0] - 1) * 3 + cur[1]] = cur_board[
                                                                                           (cur[0] - 1) * 3 + cur[1]], \
                                                                                       cur_board[cur[0] * 3 + cur[1]]
                str_board = list_to_str(cur_board)
                if str_board not in self.visited:
                    tmp_block.append((cur[0] - 1, cur[1]))
                    tmp_step.append(str_board)
                    self.visited.add(str_board)
                cur_board[cur[0] * 3 + cur[1]], cur_board[(cur[0] - 1) * 3 + cur[1]] = cur_board[
                                                                                           (cur[0] - 1) * 3 + cur[1]], \
                                                                                       cur_board[cur[0] * 3 + cur[1]]
            if cur[0] != 1:  # 不在最后一行, 可以down
                cur_board[cur[0] * 3 + cur[1]], cur_board[(cur[0] + 1) * 3 + cur[1]] = cur_board[
                                                                                           (cur[0] + 1) * 3 + cur[1]], \
                                                                                       cur_board[cur[0] * 3 + cur[1]]
                str_board = list_to_str(cur_board)
                if str_board not in self.visited:
                    tmp_block.append((cur[0] + 1, cur[1]))
                    tmp_step.append(str_board)
                    self.visited.add(str_board)
                cur_board[cur[0] * 3 + cur[1]], cur_board[(cur[0] + 1) * 3 + cur[1]] = cur_board[
                                                                                           (cur[0] + 1) * 3 + cur[1]], \
                                                                                       cur_board[cur[0] * 3 + cur[1]]
            if cur[1] != 0:  # 不在第一列, 可以left
                cur_board[cur[0] * 3 + cur[1]], cur_board[cur[0] * 3 + cur[1] - 1] = cur_board[cur[0] * 3 + cur[1] - 1], \
                                                                                     cur_board[cur[0] * 3 + cur[1]]
                str_board = list_to_str(cur_board)
                if str_board not in self.visited:
                    tmp_block.append((cur[0], cur[1] - 1))
                    tmp_step.append(str_board)
                    self.visited.add(str_board)
                cur_board[cur[0] * 3 + cur[1]], cur_board[cur[0] * 3 + cur[1] - 1] = cur_board[cur[0] * 3 + cur[1] - 1], \
                                                                                     cur_board[cur[0] * 3 + cur[1]]
            if cur[1] != 2:  # 不在最后一列, 可以right
                cur_board[cur[0] * 3 + cur[1]], cur_board[cur[0] * 3 + cur[1] + 1] = cur_board[cur[0] * 3 + cur[1] + 1], \
                                                                                     cur_board[cur[0] * 3 + cur[1]]
                str_board = list_to_str(cur_board)
                if str_board not in self.visited:
                    tmp_block.append((cur[0], cur[1] + 1))
                    tmp_step.append(str_board)
                    self.visited.add(str_board)
                cur_board[cur[0] * 3 + cur[1]], cur_board[cur[0] * 3 + cur[1] + 1] = cur_board[cur[0] * 3 + cur[1] + 1], \
                                                                                     cur_board[cur[0] * 3 + cur[1]]
            return tmp_block, tmp_step

        true_answer = ["123450"]

        # self.visited = [str(board)]  # 记录已经出现过的board的排列.
        self.visited = set()
        board = simple_list(board)
        cur = (0, 0)
        for i in range(len(board)):
            if board[i] == 0:
                cur = (i // 3, i % 3)
        board = list_to_str(board)
        self.visited.add(board)

        # board = list_to_str(board)
        if board in true_answer:
            return 0
        next_step = [board]
        next_block = [cur]
        count = 1
        while next_step:  # 如果没有候选方案, 说明无解
            size = len(next_step)
            for i in range(0, size):
                cur_step = next_step.pop(0)
                cur_block = next_block.pop(0)
                tmp_block, tmp_step = get_next_step(cur_block, cur_step)
                next_step += tmp_step
                next_block += tmp_block
                # print(f'cur_board:{cur_step}; cur_block:{cur_block}; next_step:{next_step}')

            # print()
            # print(self.visited)
            # print()
            if true_answer[0] in self.visited:
                return count
            else:
                count += 1
        return -1


if __name__ == '__main__':
    input = [[4,1,2],[5,0,3]]
    s = Solution()
    print(s.slidingPuzzle(input))
