#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    dp = {0: 1}

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        O(target*len(nums))
        """
        dp = (target+1) * [0]
        dp[0] = 1

        for i in range(1, target+1):
            for j in nums:
                if i - j >= 0 and dp[i-j] > 0:
                    dp[i] += dp[i-j]

        return dp[-1]

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if target in self.dp:
            return self.dp[target]

        count = 0
        for i in nums:
            if target - i > 0:
                count += self.combinationSum4(nums, target - i)
            elif target - i == 0:
                count += 1
        self.dp[target] = count

        return count


if __name__ == '__main__':
    pass
