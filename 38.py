# -*- coding:utf-8 -*-
"""
剑指 Offer 38. 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

限制：
1 <= s 的长度 <= 8
"""
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        """
        dp
        len s | list
         1  a  [a]
         2  ab [ab, ba]
         3 abc [a(bc), b(ac), c(ab)]
         n ... for ele in n: f(n without ele)
         T(n!)
        :param s:
        :return:
        """
        list_s = list(s)
        result = []

        def rec(j):
            if j == len(list_s) - 1:
                result.append(''.join(list_s))
                return
            tmp = []
            for i in range(j, len(list_s)):
                if list_s[i] in tmp:
                    continue  # input有重复字母时
                tmp.append(list_s[i])
                list_s[i], list_s[j] = list_s[j], list_s[i]
                rec(j+1)
                list_s[i], list_s[j] = list_s[j], list_s[i]

        rec(0)
        return result


if __name__ == '__main__':
    input = "abcb"
    s = Solution()
    print(s.permutation(input))
