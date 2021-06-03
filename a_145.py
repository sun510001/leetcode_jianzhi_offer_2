# -*- coding:utf-8 -*-
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @classmethod
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        stack.append(root)
        result = []
        while len(stack) != 0 and root:
            tmp = stack.pop()
            result.append(tmp.val)
            if tmp.left:
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)
        return result[::-1]


if __name__ == '__main__':
    input = [3, 2, 4, None, None, 1]
    n = len(input)

    def rec(root, i):
        if n > 2 * i + 1 and input[2 * i + 1]:
            root.left = TreeNode(input[2 * i + 1])
            rec(root.left, 2 * i + 1)
        if n > 2 * i + 2 and input[2 * i + 2]:
            root.right = TreeNode(input[2 * i + 2])
            rec(root.right, 2 * i + 2)
        print()
    root = TreeNode(input[0])
    rec(root, 0)
    out = Solution.postorderTraversal(root)
    print(out)
