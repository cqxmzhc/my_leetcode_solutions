#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = (target+1) * [0]
        dp[0] = 1

        for i in range(1, target+1):
            for j in nums:
                if i - j >= 0 and dp[i-j] > 0:
                    dp[i] += dp[i-j]

        return dp[-1]


if __name__ == '__main__':
    pass
