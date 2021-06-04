# -*- coding:utf-8 -*-
"""
剑指 Offer 20. 表示数值的字符串
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。

数值（按顺序）可以分成以下几个部分：
1. 若干空格
2. 一个 小数 或者 整数
3. （可选）一个 'e' 或 'E' ，后面跟着一个 整数
4. 若干空格

小数（按顺序）可以分成以下几个部分：
1. （可选）一个符号字符（'+' 或 '-'）
2. 下述格式之一：
    1. 至少一位数字，后面跟着一个点 '.'
    2. 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
    3. 一个点 '.' ，后面跟着至少一位数字

整数（按顺序）可以分成以下几个部分：
1. （可选）一个符号字符（'+' 或 '-'）
2. 至少一位数字

部分数值列举如下：
["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]

部分非数值列举如下：
["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]

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
输入：s = "    .1  "
输出：true

提示：
1 <= s.length <= 20
s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，空格 ' ' 或者点 '.' 。
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        """
        isdigit() 判断是否为数字
        :param s:
        :return:
        """
        transTable = [[1, 2, 7, -1, 0, -1], [-1, 2, 7, -1, -1, -1], [-1, 2, 3, 4, 9, -1], [-1, 3, -1, 4, 9, -1],
                      [6, 5, -1, -1, -1, -1], [-1, 5, -1, -1, 9, -1], [-1, 5, -1, -1, -1, -1], [-1, 8, -1, -1, -1, -1],
                      [-1, 8, -1, 4, 9, -1], [-1, -1, -1, -1, 9, -1]]
        cols = {
            'sign': 0,
            'num': 1,
            'dot': 2,
            'e': 3,
            'blank': 4,
            'other': 5
        }

        def get_col(c):
            if c.isdigit(): return 'num'
            elif c in ['+','-']: return 'sign'
            elif c == '.': return 'dot'
            elif c in ['e', 'E']: return 'e'
            elif c == ' ': return 'blank'
            else: return 'other'


        end_status = [2, 3, 5, 8, 9]
        status = 0
        for each in s:
            status = transTable[status][cols[get_col(each)]]
            if status == -1: return False
        if status in end_status:
            return True
        else:
            return False


if __name__ == '__main__':
    input = "0"
    s = Solution()
    out = s.isNumber(input)
    print(out)
