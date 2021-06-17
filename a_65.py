# -*- coding:utf-8 -*-
"""
65. 有效数字
有效数字（按顺序）可以分成以下几个部分：
    1. 一个 小数 或者 整数
    2. （可选）一个 'e' 或 'E' ，后面跟着一个 整数

小数（按顺序）可以分成以下几个部分：
    1. （可选）一个符号字符（'+' 或 '-'）
    2. 下述格式之一：
        1. 至少一位数字，后面跟着一个点 '.'
        2. 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
        3. 一个点 '.' ，后面跟着至少一位数字

整数（按顺序）可以分成以下几个部分：
    1. （可选）一个符号字符（'+' 或 '-'）
    2. 至少一位数字

部分有效数字列举如下：
["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]

部分无效数字列举如下：
["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

给你一个字符串 s ，如果 s 是一个有效数字 ，请返回 true 。

示例 1：
输入：s = "0"
输出：true

示例 2：
输入：s = "e"
输出：false

示例 3：
输入：s = "."
输出：false

示例 4：
输入：s = ".1"
输出：true

提示：
1 <= s.length <= 20
s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.' 。
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        """
        画状态图, 简历状态表
        https://leetcode-cn.com/problems/valid-number/solution/biao-qu-dong-fa-by-user8973/
        :param s:
        :return:
        """
        status = [[4, 3, -1, 1, -1, -1],
                  [2, 3, -1, -1, -1, -1],
                  [-1, 3, -1, -1, -1, -1],
                  [7, 3, 5, -1, 9, -1],
                  [-1, 7, -1, -1, -1, -1],
                  [-1, 6, -1, 8, -1, -1],
                  [-1, 6, -1, -1, 9, -1],
                  [-1, 7, 5, -1, 9, -1],
                  [-1, 6, -1, -1, -1, -1]
                  ]

        def match_ele(ele):
            if ele == '.':
                return 'dot'
            elif ele in ['+', '-']:
                return '+-'
            elif ele in ['e', 'E']:
                return 'e'
            elif ele.isdigit():
                return 'num'
            else:
                return 'other'

        dic = {
            'dot': 0,
            'num': 1,
            'e': 2,
            '+-': 3,
            'end': 9,
            'other': 5
        }

        current = 0
        for ele in s:
            doing = dic.get(match_ele(ele))
            current = status[current][doing]
            if doing == 5:
                return False
            if current == -1:
                return False
        if status[current][4] == 9:
            return True
        else:
            return False


if __name__ == '__main__':
    input = "4e+"
    s = Solution()
    out = s.isNumber(input)
    print(out)
