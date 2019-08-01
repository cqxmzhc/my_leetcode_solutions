#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.common import TreeNode, buildTree
import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        对于最小uglynumber: 1, 按照定义，所有的uglynumber通过与(2,3,5)任意组合的成绩得到
        因为
        1. 对于除2, 3, 5之外的可以被最终分解为(2,3,5)任意组合的数, 是包含在上述定义中的
        2. 对于除2, 3, 5之外的不能被最终分解为(2,3,5)组合的数与ublynumber的乘积是不属于uglynumber的
        """
        if n <= 0:
            return 0

        dp = [0] * n
        dp[0] = 1
        t2 = t3 = t5 = 0

        for i in range(1, n):
            dp[i] = min(2*dp[t2], 3*dp[t3], 5*dp[t5])
            if dp[i] == 2*dp[t2]:
                t2 += 1
            if dp[i] == 3*dp[t3]:
                t3 += 1
            if dp[i] == 5*dp[t5]:
                t5 += 1

        return dp[-1]
