# -*- coding:utf-8 -*-
"""
剑指 Offer 52. 两个链表的第一个公共节点
输入两个链表，找出它们的第一个公共节点。
https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
"""
# Definition for singly-linked list.

from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_listnode_sp(l: List) -> ListNode:
    if len(l) == 0: return None
    for i in range(len(l)):
        if i == 0:
            root = ListNode(l[i])
            node = root
        else:
            node.next = ListNode(l[i])
            node = node.next
    return root, node


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        a = headA长度
        b = headB长度
        c = 公共部分长度
        a + b - c = b + a - c
        遍历完headA+headB独立部分长度 = 遍历完headB+headA独立部分长度
        :param headA:
        :param headB:
        :return:
        """
        a, b = headA, headB
        while a != b:
            if a:
                a = a.next
            else:
                a = headB
            if b:
                b = b.next
            else:
                b = headA
        return a


if __name__ == '__main__':
    a = [4, 1, 8, 4, 5]
    b = [5, 0, 1, 8, 4, 5]
    a_p = 2
    b_p = 3
    node_a, end_node_a = create_listnode_sp(a[:a_p])
    node_b, end_node_b = create_listnode_sp(b[:b_p])
    node_c, _ = create_listnode_sp(a[a_p:])
    end_node_a.next = node_c
    end_node_b.next = node_c

    s = Solution()
    print(s.getIntersectionNode(node_a, node_b))
