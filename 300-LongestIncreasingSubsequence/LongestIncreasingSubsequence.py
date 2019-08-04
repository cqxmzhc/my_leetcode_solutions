#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    max_len = 0
    tabulation = {}

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.helper(nums, float("-inf"))
        if len(nums) < 2:
            return len(nums)

        self.helperDPT(nums, len(nums))
        return self.max_len

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

    def helperDP(self, nums, n):
        """
        L(i) = 1 + L(j) 0 < j < i
        L(i) = 1
        """
        if n == 1:
            return 1

        max_len_tmp = 1
        for i in range(1, n):
            res = self.helperDP(nums, i)
            if nums[i-1] < nums[n-1] and res + 1 > max_len_tmp:
                max_len_tmp = res+1

        self.max_len = max(self.max_len, max_len_tmp)
        return max_len_tmp

    def helperDPT(self, nums, n):
        """
        L(i) = 1 + L(j) 0 < j < i
        L(i) = 1
        """
        if n == 1:
            return 1

        if n in self.tabulation:
            return self.tabulation.get(n)

        max_len_tmp = 1
        for i in range(1, n):
            res = self.helperDP(nums, i)
            if nums[i-1] < nums[n-1] and res + 1 > max_len_tmp:
                max_len_tmp = res+1

        self.tabulation[n] = max_len_tmp
        self.max_len = max(self.max_len, max_len_tmp)
        return max_len_tmp


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([8, 1, 2, 7, 3, 8, 9]))
