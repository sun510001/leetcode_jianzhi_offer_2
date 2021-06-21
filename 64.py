# -*- coding:utf-8 -*-
"""
剑指 Offer 64. 求1+2+…+n
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：
输入: n = 3
输出: 6

示例 2：
输入: n = 9
输出: 45

限制：
1 <= n <= 10000
"""


class Solution:
    def sumNums(self, n: int) -> int:
        """
        短路逻辑
        python的 and 操作如果最后结果为真，返回最后一个表达式的值，
        or 操作如果结果为真，返回第一个结果为真的表达式的值
        :param n:
        :return:
        """
        return n > 0 and n + self.sumNums(n - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.sumNums(5))
