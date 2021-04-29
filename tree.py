# -*- coding:utf-8 -*-

import copy
import heapq
import random
from my_lib import cal_time

class heap:
    @classmethod
    def sift(self, li, low, high):
        """
        heap creating and sorting(ascending)
        :param li: list
        :param low: root
        :param high: the highest child node
        :return:
        """
        i = low
        j = 2 * i + 1  # the child of root
        tmp = li[low]
        while j <= high:
            if j + 1 <= high and li[j + 1] > li[j]:
                j = j + 1
            if li[j] > tmp:
                li[i] = li[j]
                i = j
                j = 2 * i + 1
            else:
                break
        li[i] = tmp

    @classmethod
    def sift_descend(self, li, low, high):
        """
        heap creating and sorting(descending)
        :param li: list
        :param low: root
        :param high: the highest child node
        :return:
        """
        i = low
        j = 2 * i + 1  # the child of root
        tmp = li[low]
        while j <= high:
            if j + 1 <= high and li[j + 1] < li[j]:
                j = j + 1
            if li[j] < tmp:
                li[i] = li[j]
                i = j
                j = 2 * i + 1
            else:
                break
        li[i] = tmp

    @classmethod
    @cal_time
    def heap_sort(self, li):
        n = len(li)
        for i in range(n // 2 - 1, -1, -1):
            self.sift(li, i, n - 1)  # creat the heap
        # print(li)
        for i in range(n - 1, -1, -1):
            li[0], li[i] = li[i], li[0]
            self.sift(li, 0, i - 1)
        return li

    @cal_time
    def heap_lib(li):
        heapq.heapify(li)
        heapq_out = []
        for i in range(len(li)):
            heapq_out.append(heapq.heappop(li))
        return heapq_out

    @classmethod
    @cal_time
    def heap_topk(self, li, k):
        k_list = li[:k]
        for i in range(k // 2 - 1, -1, -1):
            self.sift_descend(k_list, i, k - 1)  # create the heap
        for i in range(k, len(li) - 1):
            if li[i] > k_list[0]:
                k_list[0] = li[i]
                self.sift_descend(k_list, 0, k - 1)  # sort
        for i in range(k - 1, -1, -1):
            k_list[0], k_list[i] = k_list[i], k_list[0]
            self.sift_descend(k_list, 0, i - 1)
        return k_list


class Node:
    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None


class FileSystemTree:
    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self, name):
        if name[-1] != "/":
            name += "/"
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        return [x.name for x in self.now.children]

    def cd(self, name):
        if not name:
            self.now = self.root
        else:
            if name[-1] != "/":
                name += "/"
            elif name == "../":
                self.now = self.now.parent
                return
            for child in self.now.children:
                if child.name == name:
                    self.now = child
                    return
            raise ValueError('{} not exist.'.format(name))


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None

    def pre_order(self):
        print(self.data, end=' ')
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()

    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        print(self.data, end=' ')
        if self.rchild:
            self.rchild.in_order()

    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.data, end=' ')

    def level_order(self):
        node_list = [self]
        node_list2 = [self]
        while node_list:
            tmp = []
            for node in node_list:
                if node.lchild:
                    tmp.append(node.lchild)
                if node.rchild:
                    tmp.append(node.rchild)
            node_list = tmp
            node_list2 += tmp
        for ele in node_list2:
            print(ele.data, end=' ')


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.root = self.insert_rec(self.root, val)  # for function insert
                # self.insert(val)  # for function insert_rec

    def insert_rec(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert_rec(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert_rec(node.rchild, val)
            node.rchild.parent = node
        return node

    def insert(self, val):
        node = self.root
        if not node:
            self.root = BiTreeNode(val)
            return
        while True:
            if val < node.data:
                if node.lchild:
                    node = node.lchild
                else:
                    node.lchild = BiTreeNode(val)
                    node.lchild.parent = node
                    return
            elif val > node.data:
                if node.rchild:
                    node = node.rchild
                else:
                    node.rchild = BiTreeNode(val)
                    node.rchild.parent = node
                    return
            else:
                return

    def query(self, val):
        node = self.root
        while node:
            if val < node.data:
                node = node.lchild
            elif val > node.data:
                node = node.rchild
            else:
                return node
        return None

    def query_rec(self, node, val):
        if not node:
            return None
        elif val < node.data:
            return self.query_rec(node.lchild, val)
        elif val > node.data:
            return self.query_rec(node.rchild, val)
        else:
            return node

    def delete(self, val):
        if self.root:
            target_node = self.query(val)
            if target_node:
                if target_node.lchild and not target_node.rchild:
                    # have left child, but no right child
                    if target_node.data > target_node.parent.data:  # right leaf
                        target_node.lchild.parent = target_node.parent
                        target_node.parent.rchild = target_node.lchild
                    else:
                        target_node.lchild.parent = target_node.parent
                        target_node.parent.lchild = target_node.lchild
                elif target_node.rchild and not target_node.lchild:
                    # have right child, but no left child
                    if target_node.data > target_node.parent.data:  # right leaf
                        target_node.rchild.parent = target_node.parent
                        target_node.parent.rchild = target_node.rchild
                    else:
                        target_node.rchild.parent = target_node.parent
                        target_node.parent.lchild = target_node.rchild
                elif target_node.rchild and target_node.lchild:
                    # have two child
                    # 1. find the smallest node under the right child
                    tmp_node = target_node.rchild
                    while tmp_node.lchild:
                        tmp_node = tmp_node.lchild

                    # 2. replace it's value to target value
                    tmp_value = tmp_node.data

                    # 3. delete the tmp_node
                    self.delete(tmp_value)
                    target_node.data = tmp_value

                else:
                    # no child
                    if not target_node.parent:  # not root node
                        self.root = None
                    elif target_node.data > target_node.parent.data:  # right leaf
                        target_node.parent.rchild = None
                    else:  # left leaf
                        target_node.parent.lchild = None
                del target_node
                return

    def pre_order(self, root):
        if root:
            print(root.data, end=' ')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self, root):
        if root:
            self.pre_order(root.lchild)
            print(root.data, end=' ')
            self.pre_order(root.rchild)

    def post_order(self, root):
        if root:
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)
            print(root.data, end=' ')


if __name__ == '__main__':
    # li = [i for i in range(100)]
    # random.shuffle(li)
    # li_temp = copy.deepcopy(li)
    # out = heap.heap_sort(li_temp)
    # print(out)
    #
    # """use heapq"""
    # li_temp = copy.deepcopy(li)
    # out = heap.heap_lib(li_temp)
    # print(out)
    #
    # """topk"""
    # li_temp = copy.deepcopy(li)
    # out = heap.heap_topk(li_temp, 10)
    # print(out)

    """
    file tree
    """
    # n=Node("hello")
    # m=Node("world")
    # n.children.append(m)
    # m.parent = n
    # print()
    #
    # tree = FileSystemTree()
    # tree.mkdir("var/")
    # tree.mkdir("data/")
    # tree.mkdir("user/")
    # print(tree.ls())
    # tree.cd("var/")
    # tree.mkdir("xxx")
    # tree.cd("../")
    # print(tree.ls())
    # print(tree.root.children)

    """
    binary tree
    """
    # a = BiTreeNode("A")
    # b = BiTreeNode("B")
    # c = BiTreeNode("C")
    # d = BiTreeNode("D")
    # e = BiTreeNode("E")
    # f = BiTreeNode("F")
    # g = BiTreeNode("G")
    #
    # e.lchild = a
    # e.rchild = g
    # a.rchild = c
    # c.lchild = b
    # c.rchild = d
    # g.rchild = f
    #
    # root = e
    # root.pre_order()
    # print()
    # root.in_order()
    # print()
    # root.post_order()
    # print()
    # root.level_order()
    # print()
    # # print(root.lchild.rchild.data)

    """
    binary search tree
    """
    tree = BST([4, 6, 7, 9, 2, 1, 3, 5, 8])
    print("\npre_order:")
    tree.pre_order(tree.root)
    print("\nin_order:")
    tree.in_order(tree.root)
    print("\npost_order:")
    tree.post_order(tree.root)
    print()
    # print()
    # out1 = tree.query(2)
    # out1.pre_order()
    # print()
    # out2 = tree.query(12)
    # print(out2)
    # out3 = tree.query(8)
    # out3.pre_order()

    # tree.delete(8)
    # print("\n8 :")
    # tree.pre_order(tree.root)
    # print()
    # tree.insert(8)
    # tree.pre_order(tree.root)
    #
    # tree.delete(7)
    # print("\n7 :")
    # tree.pre_order(tree.root)
    # print()
    # tree.insert(7)
    # tree.pre_order(tree.root)

    # tree.delete(2)
    # print("\n2 :")
    # tree.pre_order(tree.root)
    # print()
    # tree.insert(2)
    # tree.pre_order(tree.root)

    tree.delete(4)
    tree.delete(1)
    tree.delete(8)
    tree.pre_order(tree.root)