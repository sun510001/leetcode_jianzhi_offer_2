# -*- coding:utf-8 -*-
"""
剑指 Offer 05. 替换空格
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。



示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."


限制：

0 <= s 的长度 <= 10000
"""

class Solution:
    def replaceSpace(s: str) -> str:
        """
        T(n) = O(n)
        S(n) = O(n)
        :return:
        """
        result = []
        for ele in s:
            if ele == ' ':
                result.append('%20')
            else:
                result.append(ele)
        return ''.join(result)


if __name__ == '__main__':
    input = "We are happy."
    output = Solution.replaceSpace(input)
    print(output)
