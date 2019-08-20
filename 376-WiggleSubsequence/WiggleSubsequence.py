#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 1:
            return 0

        up = [1] * length
        down = [1] * length

        for i in range(1, length):
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j] and up[i] < down[j] + 1:
                    up[i] = down[j] + 1
                if nums[i] < nums[j] and down[i] < up[j] + 1:
                    down[i] = up[j] + 1

        return max(up + down)


if __name__ == '__main__':
    s = Solution()
    s.wiggleMaxLength([1, 7])
