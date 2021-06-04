# -*- coding:utf-8 -*-
"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

图示两个链表在节点 c1 开始相交：
A a1->a2-----
             ->c1->c2->c3
B b1->b2->b3-
题目数据 保证 整个链式结构中不存在环。
注意，函数返回结果后，链表必须 保持其原始结构 。

eg:1
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

eg:2
输入：intersectVal= 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

eg:3
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。

提示：

listA 中节点数目为 m
listB 中节点数目为 n
0 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
如果 listA 和 listB 没有交点，intersectVal 为 0
如果 listA 和 listB 有交点，intersectVal == listA[skipA + 1] == listB[skipB + 1]

进阶：你能否设计一个时间复杂度 O(n) 、仅用 O(1) 内存的解决方案？
"""
import copy


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_node(list_a, list_b, skip_a, skip_b):
    root_a = ListNode(list_a[0])
    node_a = root_a
    root_b = ListNode(list_b[0])
    node_b = root_b
    for i in range(1, skip_a):
        node_a.next = ListNode(list_a[i])
        node_a = node_a.next
    for j in range(1, skip_b):
        node_b.next = ListNode(list_b[j])
        node_b = node_b.next
    for k in range(skip_a, len(list_a)):
        node_a.next = ListNode(list_a[k])
        node_a = node_a.next
        if k == skip_a:
            node_b.next = node_a

    return root_a, root_b


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        1. 最简单
        双循环
        超时
        :param headA:
        :param headB:
        :return:
        """

        node_a = headA
        node_b = headB
        while node_a:
            while node_b:
                if node_a == node_b:
                    return node_a.val
                else:
                    node_b = node_b.next
            node_b = headB
            node_a = node_a.next

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        2.
        x逆序列
        x一个个对比直到不同
        x不能破坏原结构: copy.deepcopy
        x不行, 内存地址不对了.
        ---
        双指针:
        headA独立部分长度: a
        headB独立部分长度: b
        共同部分长度: c
        长度: a链表走完再走b链表=b链表走完再走a链表
        没有交点的时候 tmp_a tmp_b都是null, 相等.
        """
        tmp_a, tmp_b = headA, headB
        while tmp_a != tmp_b:
            if tmp_a:
                tmp_a = tmp_a.next
            else:
                tmp_a = headB
            if tmp_b:
                tmp_b = tmp_b.next
            else:
                tmp_b = headA
        return tmp_a


if __name__ == '__main__':
    intersectVal = 0
    list_a = [4, 1, 8, 4, 5]
    list_b = [5, 6, 1, 8, 4, 5]
    skip_a = 2
    skip_b = 3
    heada, headb = create_node(list_a, list_b, skip_a, skip_b)
    s = Solution()
    out = s.getIntersectionNode2(heada, headb)
    print(out)
