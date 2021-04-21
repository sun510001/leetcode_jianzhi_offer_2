# -*- coding:utf-8 -*-
"""
102. 二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。



示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

"""
import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_rec(root, l, i):
    if i < len(l):
        if not l[i]:
            return None
        else:
            root = TreeNode(l[i])
            root.left = insert_rec(root, l, 2*i+1)
            root.right = insert_rec(root, l, 2*i+2)
            return root


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        DFS
        """
        # queue = collections.deque()
        # queue.append(root)
        # res = []
        # while queue:
        #     size = len(queue)
        #     level = []
        #     for _ in range(size):
        #         cur = queue.popleft()
        #         if not cur:
        #             continue
        #         level.append(cur.val)
        #         queue.append(cur.left)
        #         queue.append(cur.right)
        #     if level:
        #         res.append(level)
        # return res


        """
        BFS
        """
        def level_rec(root, level, res):
            if not root:
                return
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            if root.left:
                level_rec(root.left, level + 1, res)
            if root.right:
                level_rec(root.right, level + 1, res)

        res = []
        level_rec(root, 0, res)
        return res


if __name__ == '__main__':
    input = [3, 9, 20, None, None, 15, 7]
    tree = insert_rec(None, input, 0)
    s = Solution()
    out = s.levelOrder(tree)
    print(out)