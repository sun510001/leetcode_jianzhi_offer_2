# -*- coding:utf-8 -*-
"""
剑指 Offer 46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

提示：
0 <= num < 231
"""


class Solution:
    def translateNum(self, num: int) -> int:
        """
        dfs
        :param num:
        :return:
        """
        num = str(num)

        def dfs(i):
            if i > len(num) - 1:
                return 1
            if i == len(num) - 1 or num[i] == '0' or num[i] + num[i + 1] > '25':
                return dfs(i + 1)
            else:
                return dfs(i + 1) + dfs(i + 2)

        s = dfs(0)
        return s


if __name__ == '__main__':
    input = 11
    s = Solution()
    print(s.translateNum(input))
