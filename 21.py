# -*- coding:utf-8 -*-
"""
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。

提示：
0 <= nums.length <= 50000
1 <= nums[i] <= 10000
"""
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        """
        双指针, 动态规划
        使i为奇偶边缘的第一个偶数下标
        j向右走
        :param nums:
        :return:
        """
        if len(nums) == 0:
            return []
        i, j = 0, 0
        while j < len(nums):
            if nums[j] % 2 != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return nums

    def exchange(self, nums: List[int]) -> List[int]:
        """
        双指针
        i开头
        j末尾
        :param nums:
        :return:
        """
        # if len(nums) == 0:
        #     return []
        # i, j = 0, len(nums)-1
        # while i < j:
        #     if nums[i] % 2 == 0 and nums[j] % 2 != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #     elif nums[i] % 2 != 0:
        #         i += 1
        #     elif nums[j] % 2 == 0:
        #         j -= 1
        #     else:
        #         i += 1
        #         j -= 1
        # return nums

        if len(nums) == 0:
            return []
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] % 2 != 0: i += 1
            while i < j and nums[j] % 2 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == '__main__':
    input = [2, 16, 3, 5, 13, 1, 16, 1, 12, 18, 11, 8, 11, 11, 5, 1]
    s = Solution()
    print(s.exchange(input))
