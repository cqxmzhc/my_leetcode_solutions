#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

from common.common import TreeNode, buildTestTree

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length < 2:
            return 0

        dp = [0] * length
        dp[1] = prices[1] - prices[0]

        for i in range(2, length):
            dp[i] = max(dp[i-1], dp[i-2]+prices[-1])

        return dp[-1]


if __name__ == '__main__':
    pass
