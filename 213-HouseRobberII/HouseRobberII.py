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
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2 or length == 3:
            return max(nums)

        # 任意一个房子都只有两个状态
        # 1. 没被抢： 正常处理第i+1->n个房子
        # 2. 被抢: 正常处理第i+2->n-1个房子
        return max(self.helper(nums[1:length]), nums[0]+self.helper(nums[2:length-1]))

    def helper(self, nums):
        dp0 = 0
        dp1 = nums[0]
        for i in range(1, len(nums)):
            dp0, dp1 = dp1, max(dp1, dp0+nums[i])

        return max(dp0, dp1)


if __name__ == "__main__":
    s = Solution()
    print(s.rob([2, 1, 1, 2]))
