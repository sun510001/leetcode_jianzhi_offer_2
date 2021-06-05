# -*- coding:utf-8 -*-
"""
203. 移除链表元素
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。


示例 1：
1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
               |
     1 -> 2 -> 3 -> 4 - >5

输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]
示例 2：

输入：head = [], val = 1
输出：[]
示例 3：

输入：head = [7,7,7,7], val = 7
输出：[]


提示：

列表中的节点在范围 [0, 104] 内
1 <= Node.val <= 50
0 <= k <= 50

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_listnode(input_list):
    if len(input_list) == 0: return None
    node = ListNode(input_list[0])
    temp_node = node
    for i in range(1, len(input_list)):
        temp_node.next = ListNode(input_list[i])
        temp_node = temp_node.next
    return node


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        注意: 1. head为空时
        2. 全部删除时
        3. ListNode类有默认值
        :param head:
        :param val:
        :return:
        """

        def del_element(node):
            """
            A -> B -> C -> ...
            :param node: A
            :param val: B.val
            :return: A->C->..
            """
            tmp_node = node.next.next  # record C
            del node.next  # del B
            node.next = tmp_node  # A -> C
            return node

        while head and head.val == val:
            # head第一个val等于要删除的val
            head = head.next
        if not head:
            # head为空时
            return head
        node = head
        while node:
            if not node.next:
                break
            elif node.next.val == val:
                node = del_element(node)
            else:
                node = node.next
        return head

    def removeElements2(self, head: ListNode, val: int) -> ListNode:
        """
        listnode加一个头结点!
        a->b->c
        0->a->b->c
        :param head:
        :param val:
        :return:
        """
        dump_node = ListNode()
        dump_node.next = head
        tmp_node = dump_node
        while tmp_node.next:
            if tmp_node.next.val == val:
                tmp_node.next = tmp_node.next.next
            else:
                tmp_node = tmp_node.next
        return dump_node.next


if __name__ == '__main__':
    input = [1,7,7,7]
    val = 7
    listnode_out = create_listnode(input)
    s = Solution()
    out = s.removeElements2(listnode_out, val)
    print(out)
