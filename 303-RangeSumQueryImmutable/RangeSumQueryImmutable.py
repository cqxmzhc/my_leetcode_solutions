#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

from common.common import TreeNode, buildTestTree

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class NumArray(object):
    dp = []

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            return
        self.dp = [0] * len(nums)
        self.dp[0] = nums[0]

        if len(nums) >= 2:
            self.dp[1] = nums[0] + nums[1]

        for i in range(2, len(nums)):
            self.dp[i] = self.dp[i-1] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        tmp = 0
        if i - 1 >= 0:
            tmp = self.dp[i-1]
        return self.dp[j] - tmp


if __name__ == '__main__':
    pass
