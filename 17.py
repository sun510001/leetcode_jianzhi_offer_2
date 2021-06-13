# -*- coding:utf-8 -*-
"""
剑指 Offer 17. 打印从1到最大的n位数
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]

说明：
用返回一个整数列表来代替打印
n 为正整数
"""
from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        """
        不考虑大数
        :param n:
        :return:
        """
        res = []
        i = 0
        while i < 10 ** n - 1:
            i += 1
            res.append(i)
        return res

    def printNumbers(self, n: int) -> List[int]:
        """
        不考虑大数, 简化
        :param n:
        :return:
        """
        return list(range(1, 10 ** n))

    def printNumbers(self, n: int) -> List[int]:
        """
        大数
        dfs
        :param n:
        :return:
        """

        def dfs(x):
            if x == n:
                s = ''.join(num[self.start:])
                if s != '0': res.append(int(s))  # 列表中第一位是1
                if n - self.start == self.nine: self.start -= 1  # 3 - start == nine: start - 1
                return
            for i in range(10):
                if i == 9:
                    self.nine += 1
                num[x] = str(i)
                dfs(x + 1)  # 进入递归
            self.nine -= 1

        num = ['0'] * n  # 第一个元素 000 if n = 3
        res = []
        self.nine = 0  # 统计 nine 的方法：
                       # 固定第 x 位时, 当 i = 9 则执行 nine = nine + 1,
                       # 并在回溯前恢复 nine = nine - 1.
        self.start = n - 1  # 从右数, 第一位开始 [0,0,0,0,0,1] if n == 6: start = 5
        dfs(0)
        return res


if __name__ == '__main__':
    input = 3
    s = Solution()
    print(s.printNumbers(input))
