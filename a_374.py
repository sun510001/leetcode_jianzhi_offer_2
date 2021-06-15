# -*- coding:utf-8 -*-
"""
374. 猜数字大小
猜数字游戏的规则如下：

每轮游戏，我都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1 或 0）：

-1：我选出的数字比你猜的数字小 pick < num
1：我选出的数字比你猜的数字大 pick > num
0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
返回我选出的数字。

示例 1：
输入：n = 10, pick = 6
输出：6

示例 2：
输入：n = 1, pick = 1
输出：1

示例 3：
输入：n = 2, pick = 1
输出：1

示例 4：
输入：n = 2, pick = 2
输出：2


提示：
1 <= n <= 231 - 1
1 <= pick <= n
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    if num < PICK:
        return 1
    elif num > PICK:
        return -1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        """
        暴力循环
        :param n:
        :return:
        """
        start = 0
        while guess(start) != 0:
            start += 1
        return start

    def guessNumber(self, n: int) -> int:
        """
        二分查找
        :param n:
        :return:
        """
        i, j = 1, n
        while i < j:
            mid = (i+j) >> 1
            if guess(mid) == -1:  # i pick mid j
                j = mid
            elif guess(mid) == 1:  # i mid pick j
                i = mid + 1
            else:
                return mid
        if i == j:
            return i


if __name__ == '__main__':
    PICK = 541234
    N = 2
    s = Solution()
    out = s.guessNumber(N)
    print(out)