#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return length
        # dp[i]表示以第i个元素结尾的LIS(长度, 数量)
        dp = [[1, 1] for _ in range(length)]

        # basecase: dp[i] = (1,1)

        # 状态转移方程
        # dp[i] = (dp[j][0]+1, dp[j][1]) (j < i and nums[i] > nums[j] and dp[j][0]+1 > dp[i][0])
        # dp[i] = (dp[j][0], dp[j][1] + 1) (j < i and nums[i] > nums[j] and dp[j][0] + 1 == dp[i][0])
        max_length = 1
        number = length
        for i in range(1, length):
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]

            if dp[i][0] > max_length:
                max_length = dp[i][0]
                number = dp[i][1]
            elif max_length != 1 and dp[i][0] == max_length:
                number += dp[i][1]

        return number


if __name__ == '__main__':
    s = Solution()
    s.findNumberOfLIS([2, 2, 2, 2, 2])
