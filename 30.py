# -*- coding:utf-8 -*-
"""
剑指 Offer 30. 包含min函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
调用 min、push 及 pop 的时间复杂度都是 O(1)。

示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.

提示：
各函数的调用总次数不超过 20000 次
注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.storage = []

    def push(self, x: int) -> None:
        self.storage.append(x)

    def pop(self) -> None:
        self.storage.pop()

    def top(self) -> int:
        if len(self.storage) == 0: return None
        return self.storage[-1]

    def min(self) -> int:
        if len(self.storage) == 0: return None
        if len(self.storage) == 1: return self.storage[0]
        tmp = self.storage[0]
        for ele in self.storage:
            if tmp > ele:
                tmp = ele
        return tmp


class MinStack2:

    def __init__(self):
        """
        initialize your data structure here.
        建立第二个链表记录最小值
        """
        self.s_a = []
        self.s_b = []

    def push(self, x: int) -> None:
        self.s_a.append(x)
        if not self.s_b or self.s_b[-1] >= x:
            self.s_b.append(x)

    def pop(self) -> None:
        if len(self.s_a) == 0:
            pass
        else:
            tmp = self.s_a[:-1]
            if self.s_b[-1] == tmp:
                self.s_b = self.s_b[:-1]

    def top(self) -> int:
        if len(self.s_a) == 0: return None
        return self.s_a[-1]

    def min(self) -> int:
        if len(self.s_b) == 0: return None
        return  self.s_b[-1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()