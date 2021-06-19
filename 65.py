# -*- coding:utf-8 -*-
"""
剑指 Offer 65. 不用加减乘除做加法
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

示例:
输入: a = 1, b = 1
输出: 2

提示：
a, b 均可能是负数或 0
结果不会溢出 32 位整数
"""

class Solution:
    def add(self, a: int, b: int) -> int:
        """
        二进制, 位运算
        ~: 全部取反
        ^: 异或
        &: 与
        :param a:
        :param b:
        :return:
        """
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        if a <= 0x7fffffff:
            return a
        else:
            return ~(a ^ x)


if __name__ == '__main__':
    a = -1
    b = 1
    s = Solution()
    print(s.add(a, b))