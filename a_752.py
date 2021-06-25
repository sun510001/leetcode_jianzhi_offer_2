# -*- coding:utf-8 -*-
"""
752. 打开转盘锁
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。
每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。


示例 1:
输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。
示例 2:
输入: deadends = ["8888"], target = "0009"
输出：1
解释：
把最后一位反向旋转一次即可 "0000" -> "0009"。
示例 3:
输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
输出：-1
解释：
无法旋转到目标数字且不被锁定。
示例 4:
输入: deadends = ["0000"], target = "8888"
输出：-1

提示：
死亡列表 deadends 的长度范围为 [1, 500]。
目标数字 target 不会在 deadends 之中。
每个 deadends 和 target 中的字符串的数字会在 10,000 个可能的情况 '0000' 到 '9999' 中产生。
"""
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        bfs
        超时
        :param deadends:
        :param target:
        :return:
        """

        def roll_all_possible(code: str) -> List[str]:
            """
            :param index: 转动的位数 [0,1,2,3] 3是个位
            :param upordown: 数字增加还是减少, up=True;down=False
            :param code: 当前密码
            :return: code
            """
            save_list = []
            for i, v in enumerate(code):
                tmp_1 = code[:i] + str((int(v) + 1) % 10) + code[i + 1:]
                tmp_2 = code[:i] + str((int(v) - 1) % 10) + code[i + 1:]
                if tmp_1 not in dead_dic:
                    save_list.append(tmp_1)
                if tmp_2 not in dead_dic:
                    save_list.append(tmp_2)
            return save_list

        dead_dic = set(deadends)
        stack = ["0000"]
        count = 0
        if "0000" in dead_dic:
            return -1
        if target == "0000":
            return 0

        while stack:
            count += 1
            size = len(stack)
            for i in range(0, size):
                cur = stack.pop(0)
                tmp_list = roll_all_possible(cur)
                for tmp in tmp_list:
                    # if tmp not in deadends:
                    dead_dic.add(tmp)
                    if tmp != target:
                        stack.append(tmp)
                        # print(tmp)
                    else:
                        return count
        return -1


if __name__ == '__main__':
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0000"
    s = Solution()
    print(s.openLock(deadends, target))
