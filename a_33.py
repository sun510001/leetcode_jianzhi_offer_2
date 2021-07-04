# -*- coding:utf-8 -*-
"""
33. 搜索旋转排序数组
整数数组 nums 按升序排列，数组中的值 互不相同 。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
示例 2：
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：
输入：nums = [1], target = 0
输出：-1

提示：
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums 中的每个值都 独一无二
题目数据保证 nums 在预先未知的某个下标上进行了旋转
-10^4 <= target <= 10^4

进阶：你可以设计一个时间复杂度为 O(log n) 的解决方案吗？
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        二分查找
        :param nums: 翻转后的增序列表
        :param target: 目标数
        :return: target在nums中的index
        """
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j) // 2  # 计算中间值
            if nums[mid] == target:
                return mid
            elif nums[i] <= nums[mid]:  # mid 落在最大值左边或等于最大值时, 如果相等时, mid要往右, 所以选 1, 结果会mid + 1
                if nums[i] <= target <= nums[mid]:  # 1. target 在 i 与 mid 之间
                    j = mid
                else:
                    i = mid + 1  # 由于地板除, mid偏向左边, 所以左边(i)加1
            else:  # mid 落在最大值右边时
                if nums[mid] <= target <= nums[j]:  # 2. target 在 mid 与 j 之间
                    i = mid + 1
                else:
                    j = mid
        return j if nums[i] == target else -1  # 返回 i 的值, 若不相等, 返回-1


if __name__ == '__main__':
    nums = [3, 1]
    target = 1
    sol = Solution()
    print(sol.search(nums, target))
