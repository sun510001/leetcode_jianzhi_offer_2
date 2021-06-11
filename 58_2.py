# -*- coding:utf-8 -*-
"""
剑指 Offer 58 - II. 左旋转字符串
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：
输入: s = "abcdefg", k = 2
输出: "cdefgab"

示例 2：
输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"

限制：
1 <= k < s.length <= 10000
"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        """
        切片
        :param s:
        :param n:
        :return:
        """
        return s[n:] + s[:n]

    def reverseLeftWords(self, s: str, n: int) -> str:
        """
        不切片, 用余数减少一个for循环
        for n -> len(s) + n
            i % len(s)
        eg:
        [0, 1, 2, 3, 4]
        n = 2
        len(s) = 5
        for 2 -> 7:
            2%5=2 3 4 0 1
        :param s:
        :param n:
        :return:
        """
        result = []
        for i in range(n, len(s) + n):
            result.append(s[i % len(s)])
        return ''.join(result)

    def reverseLeftWords(self, s: str, n: int) -> str:
        """
        不使用join
        :param s:
        :param n:
        :return:
        """
        result = ''
        for i in range(n, len(s) + n):
            result += s[i % len(s)]
        return result


if __name__ == '__main__':
    s = "abcdefg"
    n = 0
    sol = Solution()
    print(sol.reverseLeftWords(s, n))
