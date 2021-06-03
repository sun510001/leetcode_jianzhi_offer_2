# -*- coding:utf-8 -*-
"""
525. 连续数组
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。



示例 1:

输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
示例 2:

输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。


提示：

1 <= nums.length <= 10^5
nums[i] 不是 0 就是 1

"""
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        连续的一个list中. 0和1的个数相同. 要找最长的.
        第一次0比1多k个与下一次0比1多k个的情况发生时, 中间的一段就是result,找最长的result.
        把0换成-1, 一个个相加之后等于0时就能知道数量.
        需要一个表记录sum.
        [0, 1, 0, 1, 1, 0]
            0           0
        -> index[0, 1]-1 -> 0
        -> index[0, 5]   -> 5
        T(n^2) S(1)
        超时
        :param nums:
        :return:
        """
        # record_list = []
        result = 0
        if nums[0] == 0:
            nums[0] = -1
        for i in range(1, len(nums)):
            if nums[i] == 0:
                nums[i] = -1
            nums[i] += nums[i - 1]
            if nums[i] == 0:
                result = max(result, i+1)
            elif nums[i] in nums[:i]:
                b = nums[:i].index(nums[i])
                result = max(result, i - b)
        return result

    def findMaxLength2(self, nums: List[int]) -> int:
        """
        前缀和, 0和1的数量差
        hashmap保存数量差
        T(n) S(n)
        :param nums:
        :return:
        """
        res = 0
        first_ID = dict()
        first_ID[0] = -1
        cnt0, cnt1 = 0, 0
        for i, x in enumerate(nums):
            cnt0 += (x == 0)
            cnt1 += (x == 1)
            d = cnt0 - cnt1
            if d in first_ID:
                res = max(res, i - first_ID[d])
            else:
                first_ID[d] = i
        return res


if __name__ == '__main__':
    input = [0, 1, 0, 1, 0, 1, 1, 1, 0]
    s = Solution()
    print(s.findMaxLength2(input))
