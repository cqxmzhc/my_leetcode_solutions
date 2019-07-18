#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

from common.common import TreeNode, buildTestTree

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0

        dp = [0] * len(cost)
        dp[0] = cost[0]
        if len(cost) >= 2:
            dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return min(dp[-1], dp[-2])

    def minCostClimbingStairs2(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0

        m1, m2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            m1, m2 = m2, min((m1 + cost[i]), m2)

        return min(m1, m2)

if __name__ == '__main__':
    pass
