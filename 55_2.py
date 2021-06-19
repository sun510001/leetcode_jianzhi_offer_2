# -*- coding:utf-8 -*-
"""
剑指 Offer 55 - II. 平衡二叉树
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

限制：
0 <= 树的结点个数 <= 10000
注意：本题与主站 110 题相同：https://leetcode-cn.com/problems/balanced-binary-tree/
"""
from tree import TreeNode, create_tree


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        后序遍历 + 剪枝 （从底至顶）
        对二叉树做后序遍历，从底至顶返回子树深度，
        若判定某子树不是平衡树则 “剪枝” ，直接向上返回。
        :param root:
        :return:
        """
        def rec(root):
            if not root: return 0
            left = rec(root.left)
            if left == -1: return -1
            right = rec(root.right)
            if right == -1: return -1
            if abs(left-right) <= 1:
                return max(left, right) + 1  # 当前node最深的深度
            else:
                return -1
        return rec(root) != -1


if __name__ == '__main__':
    input = [3, 9, 20, None, None, 15, 7]
    tree = create_tree(input)
    s = Solution()
    out = s.isBalanced(tree)
    print(out)
