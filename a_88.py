# -*- coding:utf-8 -*-
"""
88. 合并两个有序数组
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

示例 1:
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]

示例 2:
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]

提示：
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[i] <= 10^9
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        最后检测的是nums1
        nums1后面的0是留空间用的
        双指针
        用两个指针i,j分别指向两个列表末尾非0处, 就是m-1和n-1
        大小比较, 大的保存, 指针-1, m-1=0就只替换nums2, n-1=0就break
        """
        if len(nums2) != 0:
            i = m - 1
            j = n - 1
            k = m + n - 1
            while i > -1:
                if nums2[j] >= nums1[i]:
                    nums1[k] = nums2[j]
                    j -= 1
                else:
                    nums1[k] = nums1[i]
                    i -= 1
                k -= 1
                if j == -1:
                    break
            if j != -1:
                for k in range(j + 1):
                    nums1[k] = nums2[k]
            # return nums1


if __name__ == '__main__':
    nums1 = [1, 2, 5, 6, 7, 0, 0, 0]
    m = 5
    nums2 = [3, 4, 6]
    n = 3
    sol = Solution()
    print(sol.merge(nums1, m, nums2, n))
