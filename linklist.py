# -*- coding:utf-8 -*-

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


def create_head(li):
    head = Node(li[0])
    for i in range(1, len(li)):
        tmp = Node(li[i])
        tmp.next = head
        head = tmp
    return head


def create_tail(li):
    for i in range(0, len(li)):
        if i == 0:
            head = Node(li[i])
            tail = head
        else:
            tmp = Node(li[i])
            tail.next = tmp
            tail = tmp
    return head


if __name__ == '__main__':
    # a = Node(1)
    # b = Node(2)
    # c = Node(3)
    #
    # a.next = b
    # b.next = c
    #
    # print(a.next.next.item)
    li = [1, 2, 3]
    out_h = create_head(li)
    out_t = create_tail(li)
    print()
