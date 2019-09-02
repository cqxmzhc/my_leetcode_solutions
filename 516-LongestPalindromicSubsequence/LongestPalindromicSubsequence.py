#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        # dp[i][j]表示子序列s[i:j]的最大palindrome数量
        dp = [[0 for _ in range(length)] for _ in range(length)]
        # basecase dp[i][i] = 1
        for i in range(length):
            dp[i][i] = 1

        # 状态转移方程
        # dp[i][j] = dp[i+1][j-1] 如果s[i]==s[j]
        # dp[i][j] = max(dp[i+1][j], dp[i][j-1]) s[i] != s[j]

        for l in range(2, length+1):
            for i in range(length-l+1):
                j = i+l-1
                if s[i] == s[j]:
                    if l == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][length-1]


if __name__ == '__main__':
    pass
