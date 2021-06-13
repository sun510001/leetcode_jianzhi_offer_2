# -*- coding:utf-8 -*-
"""
剑指 Offer 54. 二叉搜索树的第k大节点
给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4

限制：
1 ≤ k ≤ 二叉搜索树元素个数
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_tree(l):
    def rec(i):
        node = TreeNode(l[i])
        if 2 * i + 1 < len(l):
            node.left = rec(2 * i + 1)
        if 2 * i + 2 < len(l):
            node.right = rec(2 * i + 2)
        return node

    root = rec(0)
    return root


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """
        倒过来的中序遍历
        :param root:
        :param k:
        :return:
        """

        def rec(node: TreeNode):
            if node.right:
                rec(node.right)
            res.append(node.val)
            if node.left:
                rec(node.left)

        res = []
        rec(root)
        return res[k-1]


    def kthLargest(self, root: TreeNode, k: int) -> int:
        """
        不递归
        :param root:
        :param k:
        :return:
        """
        stack = []
        p = root
        count = 0
        while stack or p:
            while p:
                stack.append(p)
                p = p.right

            cur = stack.pop()
            count += 1
            if count == k:
                return cur.val
            p = cur.left


if __name__ == '__main__':
    input_list = [3, 1, 4, None, 2]
    k = 4
    tree = create_tree(input_list)
    s = Solution()
    out = s.kthLargest(tree, k)
    print(out)
