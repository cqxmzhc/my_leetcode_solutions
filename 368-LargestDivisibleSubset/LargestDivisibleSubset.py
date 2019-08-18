#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        T[n]: nums[n]结尾的满足条件的子序列的最大长度
        T[n] = max(T[n-1], T[n-1] + 1: 如果nums[n]能被nums[n-1]结尾的满足条件的子序列中的最大值整除/能整除最小值)
        """
        length = len(nums)
        if length < 1:
            return nums

        nums.sort()
        import pdb
        pdb.set_trace()
        # 保存以第i个元素结尾满足条件的最大子序列长度
        dp = [1] * length
        # 保存满足条件的子序列元素在原序列中的索引关系
        parent = [-1] * length

        # 满足条件的子序列最大长度
        max_size = 0
        # 满足条件的子序列最后一个元素在原始序列中的索引
        max_size_index = 0

        for i in range(1, length):
            for j in range(i-1, -1, -1):
                # nums已经排序，只需要检查是否能被子序列中的最大值整除
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        # 子序列中的索引关系 j -> i
                        parent[i] = j

            if max_size < dp[i]:
                max_size = dp[i]
                max_size_index = i

        parent_index = max_size_index
        result = []
        while parent_index >= 0:
            result.insert(0, nums[parent_index])
            parent_index = parent[parent_index]

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.largestDivisibleSubset([3, 2, 1, 5]))
