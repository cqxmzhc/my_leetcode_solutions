#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return length

        dp = [0] * length
        dp[0] = 1

        # 保存子序列的最后两个元素在原list中的索引
        parent = [0] * length

        maxSize = 1
        if nums[1] != nums[0]:
            maxSize = 2
            dp[1] = 2
        for i in range(2, length):
            for j in range(i-1, -1, -1):
                if (nums[i] - nums[j]) * (nums[j] - nums[parent[j]]) < 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        parent[i] = j

            if maxSize < dp[i]:
                maxSize = dp[i]

        return maxSize


if __name__ == '__main__':
    s = Solution()
    s.wiggleMaxLength([1, 7])
