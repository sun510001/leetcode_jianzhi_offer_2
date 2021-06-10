# -*- coding:utf-8 -*-

class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution():
    def reverse_nodelist(self, node_list):
        """
        pre<-A B->C->None
        """
        pre = None
        cur = node_list
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
s = Solution()
out = s.reverse_nodelist(a)
