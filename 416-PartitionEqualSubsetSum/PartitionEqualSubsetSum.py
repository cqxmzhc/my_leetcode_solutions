#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        sum_all = sum(nums)
        # 是否是偶数
        if sum_all & 1 == 1:
            return False
        sum_half = sum_all / 2

        # dp[i][j]表示是否能从前i个元素中算出和为j的子序列
        dp = [[False for j in range(sum_half+1)] for i in range(len(nums))]

        # base case
        # 不选择任何元素
        for i in range(len(nums)):
            dp[i][0] = True

        # 状态转移方程
        # dp[i][j] = dp[i-1][j] 不选择元素nums[i]
        # dp[i][j] = dp[i-1][j-nums[i]] 选择元素nums[i]
        for i in range(1, len(nums)):
            for j in range(1, sum_half+1):
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]

        return dp[-1][-1]

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        sum_all = sum(nums)
        # 是否是偶数
        if sum_all & 1 == 1:
            return False
        sum_half = sum_all / 2

        # dp[i][j]表示是否能从前i个元素中算出和为j的子序列
        dp = [False for _ in range(sum_half+1)]

        # base case
        # 不选择任何元素
        dp[0] = True

        # 状态转移方程
        # dp[i][j] = dp[i-1][j] 不选择元素nums[i]
        # dp[i][j] = dp[i-1][j-nums[i]] 选择元素nums[i]
        for num in nums:
            for j in range(sum_half, 0, -1):
                if j >= num:
                    dp[j] = dp[j] or dp[j-num]

        return dp[-1]


if __name__ == '__main__':
    pass
