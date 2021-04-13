# -*- coding:utf-8 -*-

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 

示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
示例 4：

输入：s = "([)]"
输出：false
示例 5：

输入：s = "{[]}"
输出：true
 

提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成
"""
from stack import Stack


class Solution:
    @classmethod
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "]": "[", "}": "{"}
        # stack = Stack()
        # for i in range(0, len(s)):
        #     a = hashmap.get(s[i], None)
        #     b = stack.get_top()
        #     if b == a and a:
        #         stack.pop()
        #     else:
        #         stack.push(s[i])
        # if not stack.get_top():
        #     return True
        # else:
        #     return False
        stack = []
        for i in s:
            if stack and i in hashmap:
                if stack[-1] == hashmap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack


if __name__ == '__main__':
    s = "()[]{}"
    s2 = "([)]"
    s3 = ""
    print(Solution.isValid(s))
