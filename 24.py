# -*- coding:utf-8 -*-
"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

限制：

0 <= 节点个数 <= 5000

"""
from my_lib import ListNode


class Solution:
    def reverseList(head: ListNode) -> ListNode:
        """
        Iteration
        T(n) = O(n)
        S(n) = O(n)
        :param head:
        :return:
        """
        cur, pre = head, None
        while cur:
            tmp = cur.next  # 暂存后继节点 cur.next
            cur.next = pre  # 修改 next 引用指向
            pre = cur  # pre 暂存 cur
            cur = tmp  # cur 访问下一节点
        return pre

    def reverseList2(head: ListNode) -> ListNode:
        """
        Recursion
        T(n) = O(n)
        S(n) = O(n)
        :param head:
        :return:
        """
        def recur(cur, pre):
            if not cur:
                return pre  # 终止条件
            res = recur(cur.next, cur)  # 递归后继节点
            cur.next = pre  # 修改节点引用指向
            return res  # 返回反转链表的头节点

        return recur(head, None)  # 调用递归并返回


if __name__ == '__main__':
    input = [1, 2, 3, 4, 5]
    result = ListNode.create(input)
    output = Solution.reverseList2(result)
    print(output)
