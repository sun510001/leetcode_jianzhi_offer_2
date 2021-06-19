# -*- coding:utf-8 -*-
"""
剑指 Offer 18. 删除链表的节点
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
返回删除后的链表的头节点。
注意：此题对比原题有改动

示例 1:
输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

示例 2:
输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.

说明：
题目保证链表中节点的值互不相同
若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点
"""
from my_lib import ListNode


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        """
        4 -> 5 -> 1 -> 9
        4 -> 1 break
        要考虑头节点是val的情况
        :param head:
        :param val:
        :return:
        """
        node = head
        if head.val == val:
            return head.next
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
                return head
            else:
                node = node.next
        return head


if __name__ == '__main__':
    input = [4, 5]
    value = 4
    listnode = ListNode.create(input)
    s = Solution()
    out = s.deleteNode(listnode, value)
    print()