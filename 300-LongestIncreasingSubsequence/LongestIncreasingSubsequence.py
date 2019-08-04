#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

from common.common import TreeNode, buildTestTree

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, float("-inf"))

    def helper(self, nums, pre):
        """
        时间复杂度: O(2^n)?
        """
        if len(nums) == 0:
            return 0

        taken = nontaken = 0
        if nums[0] > pre:
            taken = self.helper(nums[1:], nums[0]) + 1

        nontaken = self.helper(nums[1:], pre)

        return max(taken, nontaken)


if __name__ == '__main__':
    pass
