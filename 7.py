# -*- coding:utf-8 -*-

"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7


限制：

0 <= 节点个数 <= 5000
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Recursion, hashmap
        T(n) = O(n)
        S(n) = O(n)
        :param preorder:
        :param inorder:
        :return:
        """
        def recur(pre_root, in_left, in_right):
            if in_left > in_right:
                return None
            node = TreeNode(preorder[pre_root])
            i = dic[preorder[pre_root]]  # find the situation of root in inorder list.
            node.left = recur(pre_root + 1, in_left, i - 1)
            # i - in_left = the lenght of left leave, preoder: root->left->right
            node.right = recur(pre_root + (i - in_left) + 1, i + 1, in_right)
            return node

        # create a hashmap
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    listnode = Solution.buildTree(preorder, inorder)
    print()
