# -*- coding:utf-8 -*-
"""
剑指 Offer 27. 二叉树的镜像
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：
     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1

示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

限制：
0 <= 节点个数 <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_tree(l):
    """
    l_child = 2*i+1
    r_child = 2*i+2
    :param l:
    :return:
    """
    def rec_insert_tree(i):
        n = TreeNode(l[i])
        if 2*i+1 < len(l):
            n.left = rec_insert_tree(2*i+1)
        if 2*i+2 < len(l):
            n.right = rec_insert_tree(2*i+2)
        return n

    if not l:
        return TreeNode(None)
    return rec_insert_tree(0)


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return TreeNode(None)
        node = root
        def rec_reverse_tree(n):
            n.left, n.right = n.right, n.left
            if n.left:
                n.left = rec_reverse_tree(n.left)
            if n.right:
                n.right = rec_reverse_tree(n.right)

            return n

        root = rec_reverse_tree(node)
        return root

    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return TreeNode(None)
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root

if __name__ == '__main__':
    input = [4,2,7,1,3,6,9]
    tree = create_tree(input)
    s = Solution()
    out = s.mirrorTree(tree)
    print(out)
