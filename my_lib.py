# -*- coding:utf-8 -*-
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def create(input):
        """create the linked list"""
        for i in range(len(input)):
            if i == 0:
                listnode = ListNode(input[i])
                result = listnode
            else:
                result.next = ListNode(input[i])
                result = result.next
        return listnode