#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length < 2:
            return length
        # dp[i][j] 表示s[i:j]是否是palindrom
        dp = [[False for _ in range(length)] for _ in range(length)]

        # basecase dp[i][i] = True
        for i in range(length):
            dp[i][i] = True

        # 状态转移方程
        # dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        count = 0
        for l range(2, length+1):
            for i in range(length-l+1):
                j = i+l-1
                if l == 2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        count += 1
                else:
                    if dp[i+1][j-1] and s[i] == s[j]:
                        dp[i][j] = True
                        count += 1

        return count


if __name__ == '__main__':
    pass
