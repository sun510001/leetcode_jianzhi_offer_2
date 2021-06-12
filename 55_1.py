# -*- coding:utf-8 -*-
"""
剑指 Offer 55 - I. 二叉树的深度
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

提示：
节点总数 <= 10000
注意：本题与主站 104 题相同：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_tree(l):
    if not l: return TreeNode(None)

    def rec_tree(i):
        node = TreeNode(l[i])
        if 2 * i + 1 < len(l): node.left = rec_tree(2 * i + 1)
        if 2 * i + 2 < len(l): node.right = rec_tree(2 * i + 2)
        return node

    return rec_tree(0)


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        递归
        :param root:
        :return:
        """

        def rec_max_d(node, i):
            j, k = 0, 0
            if node.left: j = rec_max_d(node.left, i + 1)
            if node.right: k = rec_max_d(node.right, i + 1)
            return max(j, k, i)

        if not root:
            return 0
        return rec_max_d(root, 0) + 1

    def maxDepth(self, root: TreeNode) -> int:
        """
        非递归
        :param root:
        :return:
        """
        if not root: return 0
        stack = [root]
        rec = 0
        while stack:
            tmp = []
            for node in stack:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            stack = tmp
            rec += 1
        return rec


if __name__ == '__main__':
    input = [3,9,20,None,None,15,7]
    root = create_tree(input)
    s = Solution()
    out = s.maxDepth(root)
    print(out)

 #   3
 # 9  20
 #   15 7