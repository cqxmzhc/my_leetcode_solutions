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

    def wiggleMaxLength(self, nums):
        length = len(nums)
        if length < 1:
            return length

        # 长度至少为1
        # 索引为i时最大子序列长度
        up = [1] * length
        down = [1] * length

        for i in range(1, length):
            if nums[i] > nums[i-1]:
                # 假设down[i-1] 以nums[j]结尾
                # 1. nums[j] < nums[i-1] < nums[i], up[i] = down[i-1] + 1
                # 2. nums[j] >= nums[i-1], 必然存在以nums[i-1]结尾的序列长度等于down[i-1], up[i] = down[i-1]
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
            else:
                down[i] = down[i-1]
                up[i] = up[i-1]

        return max(up + down)


if __name__ == '__main__':
    s = Solution()
    s.wiggleMaxLength([1, 7])
