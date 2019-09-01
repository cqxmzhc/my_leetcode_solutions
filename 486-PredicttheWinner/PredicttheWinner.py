#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
   def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # O(2^n)
        return self.winner(nums, 0, len(nums)-1, 1) >= 0

    # 返回当前player所选数字的和与对方player所选数字的和之差
    def winner(self, nums, s, e, turn):
        if s == e:
            return turn * nums[s]
        left = turn * nums[s] + self.winner(nums, s+1, e, -1*turn)
        right = turn * nums[e] + self.winner(nums, s, e-1, -1*turn)

        if turn == 1:
            return max(left, right)
        else:
            return min(left, right)


if __name__ == '__main__':
    s = Solution()
    s.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)
