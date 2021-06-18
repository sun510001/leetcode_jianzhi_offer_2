# -*- coding:utf-8 -*-
"""
剑指 Offer 32 - II. 从上到下打印二叉树 II
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]

提示：
节点总数 <= 1000
注意：本题与主站 102 题相同：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
"""
from typing import List

from tree import create_tree, TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        递归
        :param root:
        :return:
        """

        def rec(node, i):
            if len(self.record) < i + 1:
                self.record.append([])
            self.record[i] += [node.val]
            if node.left:
                rec(node.left, i + 1)
            if node.right:
                rec(node.right, i + 1)

        self.record = []
        if not root:
            return []
        rec(root, 0)
        return self.record

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        非递归
        :param root:
        :return:
        """
        if not root:
            return []

        stack = [root]
        layer = []
        while stack:
            record = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                record.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            layer.append(record)
        return layer


if __name__ == '__main__':
    input = [1, 2, 3, 4, 5]
    tree = create_tree(input)
    s = Solution()
    out = s.levelOrder(tree)
    print(out)
#
#    1
#  2   3
# 4 5
