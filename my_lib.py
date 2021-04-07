# -*- coding:utf-8 -*-
import random
import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def create(input):
        """create the linked list"""
        for i in range(len(input)):
            if i == 0:
                listnode = ListNode(input[i])
                result = listnode
            else:
                result.next = ListNode(input[i])
                result = result.next
        return listnode


def cal_time(func):
    def func_wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print("\n{} spent {} sec".format(func.__name__, t2 - t1))
        return res

    return func_wrapper


class MySort:
    @cal_time
    def bubble_sort(input):
        """
        冒泡排序，两两交换
        :return:
        """
        # print(input)
        for i in range(len(input) - 1):
            for j in range(len(input) - i - 1):
                if input[j] > input[j + 1]:
                    input[j], input[j + 1] = input[j + 1], input[j]
            # print("ori->", input)
        return input

    @cal_time
    def bubble_sort_opt(input):
        # print(input)
        for i in range(len(input) - 1):
            is_done = True
            for j in range(len(input) - i - 1):
                if input[j] > input[j + 1]:
                    input[j], input[j + 1] = input[j + 1], input[j]
                    is_done = False
            # print("opt->", input)
            if is_done:
                break
        return input

    @cal_time
    def select_sort(input):
        """
        选择排序
        一趟排序记录最小的数，放到第一个位置[1,2,3,...]: [1](有序区) [2,3,..](无序区)
        :return:
        """
        # print(input)
        for i in range(len(input) - 1):
            min_index = i
            for j in range(i + 1, len(input)):
                if input[j] < input[min_index]:
                    min_index = j
            input[i], input[min_index] = input[min_index], input[i]
        # print("sel->", input)
        return input

    @cal_time
    def insert_sort(input):
        """
        插入排序
        打牌的时候理牌的逻辑
        :return:
        """
        # print(input)
        for i in range(1, len(input)):
            temp = input[i]
            j = i - 1
            while j >= 0 and temp < input[j]:
                input[j + 1] = input[j]
                j -= 1
            input[j + 1] = temp
        # print("insert->", input)
        return input

    @staticmethod
    def insert_sort_gap(input, gap):
        for i in range(1, len(input)):
            tmp = input[i]
            j = i - gap
            while j >= 0 and tmp < input[j]:
                input[j + gap] = input[j]
                j -= gap
            input[j + gap] = tmp

    @classmethod
    @cal_time
    def shell_sort(self, input):
        gap = len(input) // 2
        while gap >= 1:
            self.insert_sort_gap(input, gap)
            gap //= 2

        return input

    @cal_time
    def quick_sort(input):
        """
        快速排序
        :return:
        """

        # print(input)

        def location(input, left, right):
            tmp = input[left]
            while left < right:
                while left < right and input[right] >= tmp:
                    right -= 1
                input[left] = input[right]
                while left < right and input[left] <= tmp:
                    left += 1
                input[right] = input[left]
            input[left] = tmp
            return left

        def quick_sort_rec(input, left, right):
            if left < right:
                mid = location(input, left, right)
                quick_sort_rec(input, left, mid - 1)
                quick_sort_rec(input, mid + 1, right)

        # def quick_sort_unrec(input, left, right):
        #     record_list = []
        #     record_list.append([left, right])
        #     while left < right:
        #         point_list = []
        #         for each in record_list:
        #             mid = location(each, each[0], each[1])
        #             point_list.append(mid)
        #         record_list = []
        #         record_list = input.split(point_list)
        #         for point in point_list:
        #             record_list.append(input[:point])
        #             record_list.append(point)
        #             input = input[point+1:]
        #     input = []
        #     for each in record_list:
        #         input += each

        quick_sort_rec(input, 0, len(input) - 1)
        # print(input)
        return input


def list_in_new_memory_address(input: list) -> list:
    """
    list is one of variable types, it's memory address will not be changed by plus or append.
    It is same as copy.deepcopy()
    :param input:
    :return:
    """
    temp_list = []
    temp_list += input
    return temp_list


if __name__ == '__main__':
    # random_list = [3, 1, 5, 4, 2, 7, 6]
    random_list = list(range(1000))
    random.shuffle(random_list)
    print(random_list)
    temp_list = list_in_new_memory_address(random_list)
    MySort.bubble_sort(temp_list)
    temp_list = list_in_new_memory_address(random_list)
    MySort.bubble_sort_opt(temp_list)
    temp_list = list_in_new_memory_address(random_list)
    MySort.select_sort(temp_list)
    temp_list = list_in_new_memory_address(random_list)
    MySort.insert_sort(temp_list)
    temp_list = list_in_new_memory_address(random_list)
    MySort.shell_sort(temp_list)
    temp_list = list_in_new_memory_address(random_list)
    MySort.quick_sort(temp_list)

