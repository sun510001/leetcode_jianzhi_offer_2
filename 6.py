# -*- coding:utf-8 -*-

"""
剑指 Offer 06. 从尾到头打印链表
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。



示例 1：

输入：head = [1,3,2]
输出：[2,3,1]


限制：

0 <= 链表长度 <= 10000
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        """
        Recursion
        T(n) = O(n)
        S(n) = O(n)
        :param head:
        :return:
        """
        result = []
        if head:
            result += self.reversePrint(head.next) + [head.val]
        else:
            result += []
        return result
        # return self.reversePrint(head.next) + [head.val] if head else []

    def reversePrint2(self, head: ListNode) -> List[int]:
        """
        Stack
        T(n) = O(n)
        S(n) = O(n)
        :param head:
        :return:
        """
        stack = []
        result_show = head
        while result_show:
            stack.append(result_show.val)
            result_show = result_show.next
        return stack[::-1]


if __name__ == '__main__':
    input = [1, 3, 2]

    """create the linked list"""
    for i in range(len(input)):
        if i == 0:
            listnode = ListNode(input[i])
            result = listnode
        else:
            result.next = ListNode(input[i])
            result = result.next

    """show the linked list"""
    result_show = listnode
    while result_show:
        print(result_show.val)
        result_show = result_show.next

    solution = Solution()
    output = solution.reversePrint2(listnode)
    print(output)
