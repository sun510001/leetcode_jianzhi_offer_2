# -*- coding:utf-8 -*-
"""
237. 删除链表中的节点
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为要被删除的节点 。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:
4->5->1->9

示例 1：
输入：head = [4,5,1,9], node = 5
输出：[4,1,9]
解释：给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

示例 2：
输入：head = [4,5,1,9], node = 1
输出：[4,5,9]
解释：给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.


提示：
链表至少包含两个节点。
链表中所有节点的值都是唯一的。
给定的节点为非末尾节点并且一定是链表中的一个有效节点。
不要从你的函数中返回任何结果。
"""
from my_lib import ListNode


class Solution:
    def deleteNode(self, node):
        """
        当前节点值等于next节点, 删除最后一个节点
        4->5->1->9
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        n = node
        while node.next:
            node.val = node.next.val
            if node.next.next:
                node = node.next
            else:
                node.next = None
        node = n
        return node

    def deleteNode(self, node):
        """
        node.next节点val赋值node,
        删除下一个节点, node连接node.next.next
        :param node:
        :return:
        """
        node.val = node.next.val
        node.next = node.next.next
        return node


if __name__ == '__main__':
    input = [4, 5, 1, 9]
    node = 5
    root = ListNode.create(input)
    tmp = root.search(5)
    s = Solution()
    out = s.deleteNode(tmp)
    print(out.show())
