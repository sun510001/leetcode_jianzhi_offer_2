# -*- coding:utf-8 -*-
"""
剑指 Offer 10- I. 斐波那契数列

写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。



示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5


提示：

0 <= n <= 100
"""


class Solution:
    def fib(self, n: int) -> int:
        """
        递归就完事了
        会超时
        :param n:
        :return:
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    def fib(self, n: int) -> int:
        """
        非递归
        二叉树形式可以画出来, F(5) = F(4) + F(3); F(4) = F(3) + F(2);
        树形结构问题复杂可以倒过来想.
        有很多重复计算可以省略: 建立一个hashmap做记录
        从0开始增加直到n为止
        答案需要取模 1e9+7(1000000007) -> n%1000000007
        T(n) S(n)
        :param n:
        :return:
        """
        dic = {}
        dic[0] = 0
        dic[1] = 1
        for i in range(0, n + 1):
            if dic.get(i) != None:
                continue
            else:
                dic[i] = dic[i - 1] + dic[i - 2]
        return dic[n] % 1000000007

    def fib(self, n):
        """
        动态规划 S = 1
        循环求余法
        结果取余1000000007, 使结果不会超过范围 int32(2^32)
        T(n) S(1)
        首几个斐波那契数是: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
        """
        if n == 0:
            return 0
        else:
            a, b = 1, 1
            for _ in range(n-1):
                a, b = b, a + b
            return a % 1000000007

    def fib(self, n):
        def fibon(n):
            a, b = 1, 1
            for _ in range(n):
                yield a
                a, b = b, a + b

        if n == 0:
            return 0
        else:
            tmp = 0
            for x in fibon(n):
                if x:
                    print(x)
                    tmp = x
            return tmp % 1000000007


if __name__ == '__main__':
    input = 5
    s = Solution()
    out = s.fib(input)
    print(out)
