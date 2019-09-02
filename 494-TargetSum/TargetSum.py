#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    count = 0

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # self.helper(nums, 0, 0, S)
        # return self.count

        sum_all = sum(nums)
        if (sum_all+S) % 2 != 0:
            return 0
        return self.dp(nums, (sum_all+S)/2)

    # ??
    def helper(self, nums, index, res, S):
        if index == len(nums):
            if res == S:
                self.count += 1
        else:
            self.helper(nums, index+1, res+nums[index], S)
            self.helper(nums, index+1, res-nums[index], S)

    # dp
    def dp(self, nums, S):
        """
        ?????: ???nums???????????(s+sum(nums))/2 => 0/1????
        """
        # ????
        # dp[i][j]???i????????j?????
        dp = [[0 for _ in range(S+1)] for _ in range(len(nums)+1)]
        # basecase
        for i in range(len(nums)+1):
            dp[i][0] = 1
        for j in range(1, S+1):
            dp[0][j] = 0

        # ??????: dp[i][j] = dp[i-1][j] + dp[i][j-nums[i]]
        for i in range(1, len(nums)+1):
            for j in range(nums[i-1], S+1):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]

        return dp[-1][-1]

    def dp(self, nums, S):
        dp = [0] * (S+1)
        # ?n????????0??
        dp[0] = 1

        for i in range(len(nums)):
            for j in range(S, nums[i]-1, -1):
                dp[j] = dp[j] + dp[j-nums[i]]

        return dp[S]


if __name__ == '__main__':
    pass
