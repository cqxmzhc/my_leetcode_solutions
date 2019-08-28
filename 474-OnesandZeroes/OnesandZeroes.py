#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        0-1背包问题, strs数组中的数字作为物体, m和n分别作为需要被填充的背包
        """
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        print(dp)
        for num in strs:
            one_count = 0
            zero_count = 0
            for i in num:
                if i == "1":
                    one_count += 1
                else:
                    zero_count += 1

            for j in range(one_count, n+1):
                for k in range(zero_count, m+1):
                    dp[k][j] = max(dp[k][j], dp[m-k][n-j] + 1)

        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    s.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)
