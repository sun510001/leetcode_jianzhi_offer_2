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
        self.name=name
        self.type=type
        self.children=[]
        self.parent=None


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


    # """
    # file tree
    # """
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
    a = BiTreeNode("A")
    b = BiTreeNode("B")
    c = BiTreeNode("C")
    d = BiTreeNode("D")
    e = BiTreeNode("E")
    f = BiTreeNode("F")
    g = BiTreeNode("G")

    e.lchild = a
    e.rchild = g
    a.rchild = c
    c.lchild = b
    c.rchild = d
    g.rchild = f

    root = e
    root.pre_order()
    print()
    root.in_order()
    print()
    root.post_order()
    print()
    root.level_order()
    print()
    # print(root.lchild.rchild.data)
