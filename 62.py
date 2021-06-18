# -*- coding:utf-8 -*-
"""
剑指 Offer 62. 圆圈中最后剩下的数字
0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。
求出这个圆圈里剩下的最后一个数字。
例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，
则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

示例 1：
输入: n = 5, m = 3
输出: 3

示例 2：
输入: n = 10, m = 17
输出: 2

限制：
1 <= n <= 10^5
1 <= m <= 10^6
"""


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        """
        T(n), S(n*m)
        加一个hashmap
        :param n:
        :param m:
        :return:
        """
        dic = {}
        tmp = -1
        if n == 1: return 1
        for i in range(0, n):
            dic[i] = 0
        for j in range(n):
            count = 0
            while count != m:
                tmp = (tmp + 1) % n
                if dic[tmp] != 1:
                    count += 1
            dic[tmp] = 1
            # print(dic)
        return tmp

    def lastRemaining(self, n: int, m: int) -> int:
        """
        状态转移, 约瑟夫环问题
        0 1 [2] 3 4 | 0 1 2 3 4 (除2, 并右移3位: 0)
        3 4 [0] 1 | 3 4 0 1 (删除0, 并右移3位: 4)
        1 3 [4] | 1 3 4 (删除4, 并右移3位: 1)
        1 3 | [1] 3 (删除1, 并右移3位: 3)
        反推
        [1,3]: f(1) = 0 数组长度为1, 最后剩下的那个数位置为0.
        [2,3]: f(2) = (f(1)+m)%2 = 1 数组大小为2, 位置为1.
        [3,3]: f(3) = (f(2)+m)%3 = 1 数组大小为3, 位置为1.
        [4,3]: f(4) = (f(3)+m)%4 = 0 数组大小为4, 位置为0.
        [5,3]: f(5) = (f(4)+m)%5 = 3 数组大小为5, 位置为3.
        下标为3 -> 3
        :param n:
        :param m:
        :return:
        """
        res = 0
        for i in range(2, n + 1):
            res = (res + m) % i
        return res


if __name__ == '__main__':
    n = 4
    m = 3

    s = Solution()
    print(s.lastRemaining(n, m))
