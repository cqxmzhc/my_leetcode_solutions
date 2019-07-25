#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution:
    def minimumTotal(self, triangle) -> int:
        if len(triangle) == 0:
            return 0
        dp = triangle[-1]

        # bottom-up
        # basecase一定要有一个确定的结果，如果是top-down就找不到basecase
        # O(n^2)
        for i in range(len(triangle)-1, 0, -1):
            for j in range(0, i):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i-1][j]

        return dp[0]


if __name__ == '__main__':
    s = Solution()
    r = s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 6, 3]])
    print(r)
