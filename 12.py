# -*- coding:utf-8 -*-
"""
剑指 Offer 12. 矩阵中的路径
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。
https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/

示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false

提示：
1 <= board.length <= 200
1 <= board[i].length <= 200
board 和 word 仅由大小写英文字母组成

注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/
"""
import copy
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        不能用BFS, 同一个step中走过的路径可能会交叉, 记录历史路径的hashmap使部分可能性失效
        而DFS是固定深度探测完了就把之前走过的一条路填回去.
        用DFS
        if x,y超出边界或board[x][y]!=word[num] return
        :param board:
        :param word:
        :return:
        """

        def dfs(x, y, k) -> bool:
            if not 0 <= x < len(board) or not 0 <= y < len(board[0]) or board[x][y] != word[k]: return False
            if k == len(word) - 1: return True
            board[x][y] = ''
            res = dfs(x + 1, y, k + 1) or dfs(x - 1, y, k + 1) or dfs(x, y + 1, k + 1) or dfs(x, y - 1, k + 1)
            board[x][y] = word[k]
            return res

        for i in range(len(board)):  # 为了寻找第一项
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    input = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    words = "ABCESEEEFS"
    s = Solution()
    print(s.exist(input, words))
