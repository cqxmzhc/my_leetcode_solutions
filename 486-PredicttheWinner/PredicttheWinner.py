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
        # return self.winner(nums, 0, len(nums)-1, 1) >= 0

        # O(n^2)
        length = len(nums)
        # # db[i][j]表示player1从数组nums[i:j]中所选数字之和与player2所选数字之和的差
        # dp = [[0 for _ in range(length)] for _ in range(length)]

        # # basecase 选取到最后一个元素
        # for i in range(length):
        #     dp[i][i] = nums[i]

        # # 选取数组中第一个或最后一个元素
        # # 状态转移方程 dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        # for k in range(1, length):
        #     i = 0
        #     j = k
        #     while i < length and j < length:
        #         dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        #         i += 1
        #         j += 1

        # return dp[0][-1] >= 0

        # 一维数组
        dp = [0] * length
        for i in range(length):
            dp[i] = nums[i]

        for k in range(1, length):
            i = 0
            for j in range(length-k):
                dp[j] = max(nums[i] - dp[j+1], nums[i+k]-dp[j])
                i += 1

        return dp[0] >= 0

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
