#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)+1
        if length == 0:
            return 0

        dp = [0] * length
        dp[1] = nums[0]

        # odd
        if length-1 % 2 != 0:
            for i in range(2, length):
                if dp[i-1] > dp[i-2] + nums[i-1]:
                    dp[i] = dp[i-1]
                else:
                    dp[i] = dp[i-1] if i == length-1 else dp[i-2] + nums[i-1]
        else:
            for i in range(2, length):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])

        return dp[-1]
