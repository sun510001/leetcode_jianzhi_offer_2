# -*- coding:utf-8 -*-
"""
剑指 Offer 68 - II. 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
        3
     5      1
   6   2   0  8
      7 4

示例 1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

示例 2:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。


说明:
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。
注意：本题与主站 236 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""
from tree import create_tree, TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        递归
        :param root:
        :param p:
        :param q:
        :return:
        """

        def dfs(node: TreeNode, target: TreeNode):
            if node.left and self.stop_flag != 1:
                dfs(node.left, target)
            if node.right and self.stop_flag != 1:
                dfs(node.right, target)
            if node.val == target.val or self.stop_flag == 1:
                self.result_list.append(node)
                self.stop_flag = 1
                return

        target = [p, q]
        result = []
        for each in target:
            self.stop_flag = 0
            self.result_list = []
            dfs(root, each)
            result.append(self.result_list)
        print(result)
        for i in result[0]:
            for j in result[1]:
                if i == j:
                    return i

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        简化递归
        https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/mian-shi-ti-68-ii-er-cha-shu-de-zui-jin-gong-gon-7/
        :param root:
        :param p:
        :param q:
        :return:
        """
        if not root or p.val == root.val or q.val == root.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # if not left and not right:
        #     return
        if not left:
            return right
        if not right:
            return left
        return root


if __name__ == '__main__':
    input = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = TreeNode(5)
    q = TreeNode(1)
    tree = create_tree(input)
    s = Solution()
    out = s.lowestCommonAncestor(tree, p, q)
    print(out)
