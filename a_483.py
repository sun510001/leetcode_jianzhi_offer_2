# -*- coding:utf-8 -*-
"""
483. 最小好进制
对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，则称 k（k>=2）是 n 的一个好进制。
以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。

示例 1：
输入："13"
输出："3"
解释：13 的 3 进制是 111。

示例 2：
输入："4681"
输出："8"
解释：4681 的 8 进制是 11111。

示例 3：
输入："1000000000000000000"
输出："999999999999999999"
解释：1000000000000000000 的 999999999999999999 进制是 11。

提示：
n的取值范围是 [3, 10^18]。
输入总是有效且没有前导 0。
"""


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        """
        k^0+k^1+k^2...
        n > k >= 2
        input = "1000000000000000000" 超时
        :param n:
        :return:
        """
        int_n = int(n)
        for k in range(2, int_n):
            tmp = 0
            i = 0
            while tmp < int_n:
                tmp += k ** i
                i += 1
            if tmp == int_n:
                return str(k)

    def smallestGoodBase(self, n: str) -> str:
        """
        二分查找
        bin()求出n的二进制(-2减去符号), 其他进制都小于二进制的长度
        if tmp > n: r = mid - 1
        if tmp < n: l = mid + 1
        [l,r]是k的范围
        N是n的二进制长度到k进制长度的范围
        :param n:
        :return:
        """
        n = int(n)

        def check(k, len):
            tmp = 0
            for i in range(len):
                tmp += k ** i
            return tmp

        for N in range(len(bin(n)) - 2, 0, -1):
            l = 2
            r = n - 1
            while l <= r:
                mid = (l + r) // 2
                v = check(mid, N)
                if v < n:
                    l = mid + 1
                elif v > n:
                    r = mid - 1
                else:
                    return str(mid)


if __name__ == '__main__':
    input = "13"
    s = Solution()
    out = s.smallestGoodBase(input)
    print(out)
