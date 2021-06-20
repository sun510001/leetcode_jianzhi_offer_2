# -*- coding:utf-8 -*-
"""
剑指 Offer 58 - I. 翻转单词顺序
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

示例 1：
输入: "the sky is blue"
输出: "blue is sky the"

示例 2：
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

示例 3：
输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

说明：
无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
注意：本题与主站 151 题相同：https://leetcode-cn.com/problems/reverse-words-in-a-string/
注意：此题对比原题有改动
"""
from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        有空格split不能用
        双指针逆序
        :param s:
        :return:
        """

        def str_to_list(s: str) -> List:
            s_list = []
            tmp_s = ''
            blank_flag = 1
            for ele in s:
                if ele != ' ':
                    tmp_s += ele
                    blank_flag = 0
                elif blank_flag == 0:
                    blank_flag = 1
                    s_list.append(tmp_s)
                    tmp_s = ''
            if tmp_s != '':
                s_list.append(tmp_s)
            return s_list

        s_list = str_to_list(s)
        i, j = 0, len(s_list) - 1
        while i < j:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1
        return ' '.join(s_list)

    def reverseWords(self, s: str) -> str:
        s = s.strip()  # 删除首尾空格
        strs = s.split()  # 分割字符串
        strs.reverse()  # 翻转单词列表
        return ' '.join(strs)  # 拼接为字符串并返回

    def reverseWords(self, s: str) -> str:
        """
        双指针, 倒过来搜索
        扫完一个单词就保存
        遇到空格j=i; 跳过
        :param s:
        :return:
        """
        s = s.strip()
        i = j = len(s) - 1
        result = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1
            result.append(s[i + 1:j + 1])
            while s[i] == ' ':
                i -= 1
            j = i
        return ' '.join(result)


if __name__ == '__main__':
    input = "  hello   world!  "
    s = Solution()
    print(s.reverseWords(input))
