#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = pre_max = pre_min = current_min = current_max = nums[0]

        for i in range(1, len(nums)):
            # 最大值和当前值都为正，最大值和当前值都为负
            current_max = max(pre_max*nums[i], pre_min*nums[i], nums[i])
            # 最小值为负，当前值为正；最大值为正，当前值为负
            current_min = min(pre_max*nums[i], pre_min*nums[i], nums[i])

            ans = max(ans, current_max)

            pre_max = current_max
            pre_min = current_min

        return ans


if __name__ == '__main__':
    pass
