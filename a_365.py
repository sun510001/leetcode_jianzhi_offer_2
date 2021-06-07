# -*- coding:utf-8 -*-
"""
365. 水壶问题
有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

你允许：

装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空
示例 1: (From the famous "Die Hard" example)

输入: x = 3, y = 5, z = 4
输出: True
示例 2:

输入: x = 2, y = 6, z = 5
输出: False
"""


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        """
        求两数的最大公约数, 看target能不能整除它.
        能整除就是True
        :param jug1Capacity:
        :param jug2Capacity:
        :param targetCapacity:
        :return:
        """
        if (jug1Capacity + jug2Capacity) < targetCapacity:
            return False
        if targetCapacity == 0:
            return True
        if jug1Capacity == 0:
            return jug2Capacity == targetCapacity
        if jug2Capacity == 0:
            return jug1Capacity == targetCapacity

        # def GCD(a, b):
        #     smaller = min(a, b)
        #     while smaller:
        #         if a % smaller == 0 and b % smaller == 0:
        #             print(smaller)
        #             return smaller
        #         smaller -= 1

        # def GCD(a, b):
        #     """
        #     辗转相除法
        #     :param a:
        #     :param b:
        #     :return:
        #     """
        #     while (b):
        #         tmp = b
        #         b = a % b
        #         a = tmp
        #     print(a)
        #     return a

        # def GCD(a, b):
        #     """
        #     更相减损法
        #     :param a:
        #     :param b:
        #     :return:
        #     """
        #     if a > b:
        #         return GCD(a - b, b)
        #     elif a < b:
        #         return GCD(b - a, a)
        #     else:
        #         return a


        def GCD(a, b):
            """
            更相减损法
            优化:
            当a和b均为偶数，gcb(a,b) = 2*gcb(a/2, b/2) = 2*gcb(a>>1, b>>1)
            当a为偶数，b为奇数，gcb(a,b) = gcb(a/2, b) = gcb(a>>1, b)
            当a为奇数，b为偶数，gcb(a,b) = gcb(a, b/2) = gcb(a, b>>1)
            当a和b均为奇数，利用更相减损术运算一次，gcb(a,b) = gcb(b, a-b)， 此时a-b必然是偶数，又可以继续进行移位运算。

            1.暴力枚举法：时间复杂度是O(min(a, b)))
            2.辗转相除法：时间复杂度不太好计算，可以近似为O(log(max(a, b)))，但是取模运算(求余数)性能较差。
            3.更相减损术：避免了取模运算，但是算法性能不稳定，最坏时间复杂度为O(max(a, b)))
            4.更相减损术与移位结合：不但避免了取模运算，而且算法性能稳定，时间复杂度为O(log(max(a, b)))

            :param a:
            :param b:
            :return:
            """

            def odd(num):
                """
                判断是否为奇数
                &: 位运算 与
                也可以直接写if判断里
                eg: n=10转换二进制为0000 1010，1的二进制为0000 0001
                    与之后, 看是0000 0000还是0000 0001
                :param num:
                :return:
                """
                if num & 1 == 1:
                    return True
                else:
                    return False

            if a == b:
                return a
            if a < b:
                return GCD(b, a)
            else:
                if not odd(a) and not odd(b):  # 双偶数的时候都除2再GCD, 其结果乘2
                    return GCD(a >> 1, b >> 1) << 1
                elif not odd(a) and odd(b):  # 单偶数时偶数除2
                    return GCD(a >> 1, b)
                elif odd(a) and not odd(b):
                    return GCD(a, b >> 1)
                else:
                    return GCD(b, a - b)

        return targetCapacity % GCD(jug1Capacity, jug2Capacity) == 0


if __name__ == '__main__':
    a = 3
    b = 5
    c = 4
    s = Solution()
    print(s.canMeasureWater(a, b, c))

