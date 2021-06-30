# -*- coding:utf-8 -*-
"""
剑指 Offer 37. 序列化二叉树
请实现两个函数，分别用来序列化和反序列化二叉树。
你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，
你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。
你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。


示例：
输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]

注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
"""
from collections import deque

from tree import TreeNode, create_tree, show_tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return '[]'  # root为空时, 直接返回
        queue = deque([root])  # 双向队列中放入根结点
        result = []
        while queue:
            size = len(queue)  # 记录队列长度, for循环时只循环上一次循环的队列部分
            for _ in range(size):
                node = queue.popleft()  # 队列最左端出队
                if node:
                    result.append(str(node.val))  # 结果list中添加node值
                    queue.append(node.left)  # 左节点入队
                    queue.append(node.right)  # 右节点入队
                else:
                    result.append('null')  # 当前节点为空时, list中加入空节点
        while result[-1] == 'null':
            result.pop()  # 删除列表中末尾的空节点
        return '['+','.join(result)+']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]': return None
        list_tree = data[1:-1].split(',')
        root = TreeNode(int(list_tree[0]))
        queue = deque([root])
        i = 1
        while queue and i < len(list_tree):
            node = queue.popleft()
            if i < len(list_tree) and list_tree[i] != 'null':
                node.left = TreeNode(int(list_tree[i]))
                queue.append(node.left)
            i += 1
            if i < len(list_tree) and list_tree[i] != 'null':
                node.right = TreeNode(int(list_tree[i]))
                queue.append(node.right)
            i += 1

        return root


if __name__ == '__main__':
    input = [10, 9, 11, 8, None, None, 12, 7, None, None, 13, 6, None, None, 14, 5, None, None, 15, 4, None, None, 16,
             3, None, None, 17, 2, None, None, 18, 1, None, None, 19, 0]
    tree = create_tree(input)
    s = Codec()
    string_list = s.serialize(tree)
    print(string_list)
    strings = s.deserialize(string_list)
    print(show_tree(strings))
