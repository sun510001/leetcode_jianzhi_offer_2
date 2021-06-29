# -*- coding:utf-8 -*-
"""
168. Excel表列名称
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
示例 1:
输入: 1
输出: "A"
示例 2:
输入: 28
输出: "AB"
示例 3:
输入: 701
输出: "ZY"
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        26进制
        28->AB
        A-26 B-2
        a1*26^0+a2*26^1+a3*26^2
        2*26^0+1*26^1=28
        先取模得到当前位的信息: 28%26=2 -> B
        处理更高位: 28//26=1
        loop
        先取模得到当前位的信息: 1%26=1 -> A
        处理更高位: 1//26=0
        break
        正常的26进制本应该满26进1，然后低位补0, 这里是满27进1, 低位补1.
        :param columnNumber:
        :return:
        """
        result = ''  # 记录数字26进制后的每一位
        n = columnNumber
        while n > 0:  # 每次循环取模
            n -= 1  # 把 从1开始满27进位 变回 从0开始满26进位
            tmp = chr(n % 26 + 65)  # A 的ASCII码是65
            result = tmp + result
            n //= 26  # 处理更高位数
        return result


if __name__ == '__main__':
    input = 0
    s = Solution()
    print(s.convertToTitle(input))
