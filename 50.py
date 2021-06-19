# -*- coding:utf-8 -*-
"""
剑指 Offer 50. 第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。
如果没有，返回一个单空格。
s只包含小写字母。

示例:
s = "abaccdeff"
返回 "b"

s = ""
返回 " "

限制：
0 <= s 的长度 <= 50000
"""


class Solution:
    def firstUniqChar(self, s: str) -> str:
        """
        list记录重复
        T(n^2); S(n)
        超时
        :param s:
        :return:
        """
        l = len(s)
        if l == 0: return ' '
        if l == 1: return s[0]
        tmp_list = [0]*l
        for i in range(l):
            for j in range(i+1, l):
                if s[j] == 1:
                    continue
                elif s[i] == s[j]:
                    tmp_list[j] = 1
                    tmp_list[i] = 1
            if tmp_list[i] == 0:
                return s[i]
        return ' '

    def firstUniqChar(self, s: str) -> str:
        """
        hashmap
        T(n); S(n)
        遍历s, 如果没有找到当前ele, ele: true else false
        再遍历一次s, 找true的ele
        :param s:
        :return:
        """
        dic = {}
        for ele in s:
            dic[ele] = not ele in dic
        for ele in s:
            if dic[ele]:
                return ele
        return ' '


if __name__ == '__main__':
    input = "dddccdbba"
    s = Solution()
    print(s.firstUniqChar(input))
