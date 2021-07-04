# -*- coding:utf-8 -*-
"""
645. 错误的集合
集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，
导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。
给定一个数组 nums 代表了集合 S 发生错误后的结果。
请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1：
输入：nums = [1,2,2,4]
输出：[2,3]
示例 2：
输入：nums = [1,1]
输出：[1,2]

提示：
2 <= nums.length <= 10^4
1 <= nums[i] <= 10^4
"""
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        建立长度为n的list
        遍历nums, 遍历元素在list对应index中+1
        value=0, 说明是error值
        value=1, 正常
        value=2, 重复, 也可以直接if保存

        :param nums:
        :return:
        """
        record_list = [0] * len(nums)
        deplicate = 0
        for ele in nums:
            if record_list[ele - 1] != 0:
                deplicate = ele
            else:
                record_list[ele - 1] = 1
        error = record_list.index(0)
        return [deplicate, error + 1]

    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        桶排序
        需要一次sort
        :param nums:
        :return:
        """
        dep = err = 0
        nums = sorted(nums)
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i + 1]:  # 如果元素相同
                    dep = nums[i]  # 保存重复值
                    tmp_i = i + 1  # 第二个重复值向队尾冒泡
                    while tmp_i < len(nums) - 1:
                        nums[tmp_i], nums[tmp_i + 1] = nums[tmp_i + 1], nums[1]
                        tmp_i += 1
                    break

        for j, v in enumerate(nums):  # 由于最后一个值在队尾, 当list中没有error值时, 最后一个index+1自然就是error值
            if j + 1 != v:
                err = j + 1
                break
        return [dep, err]


if __name__ == '__main__':
    nums = [1, 2, 2, 3]
    s = Solution()
    print(s.findErrorNums(nums))
