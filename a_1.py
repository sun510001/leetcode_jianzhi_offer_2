# -*- coding:utf-8 -*-
"""
1. 两数之和
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。



示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]


提示：

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案

"""
from typing import List


class Solution:
    @classmethod
    def binary_search(self, li, left, right, val):
        while left <= right:
            mid = (left + right) // 2
            if li[mid][0] == val:
                return mid
            elif li[mid][0] > val:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return None

    @classmethod
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        #
        hashmap = [[num, i] for i, num in enumerate(nums)]
        hashmap.sort(key=lambda x: x[0])

        for i in range(len(hashmap)):
            a = hashmap[i][0]
            b = target - a  # target of binary search
            if b >= a:
                j = self.binary_search(hashmap, i+1, len(hashmap)-1, b)
            else:
                j = self.binary_search(hashmap, 0, i-1, b)
            if j:
                break
        return [hashmap[i][1], hashmap[j][1]]


if __name__ == '__main__':
    nums = [2, 7, 15, 11]
    target = 9
    out = Solution.twoSum(nums, target)
    print(out)
