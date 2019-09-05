#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        质数因式分解
        """
        # dp[i]表示i个A时需要的最少步数
        # basecase 质数个元素只能通过1获取
        dp = [i for i in range(n+1)]
        dp[1] = 0

        # 状态转移方程 dp[i] = dp[j] + (i/j) if i % j == 0
        for i in range(4, n+1):
            for j in range(i-1, 1, -1):
                if i % j == 0:
                    dp[i] = dp[j] + (i/j)
                    break

        print(dp)
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    s.minSteps(12)
