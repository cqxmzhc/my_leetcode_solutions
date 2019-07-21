#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

from common.common import TreeNode, buildTestTree

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0":
            return 0
        length = len(s)
        dp = [0] * length
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] != "0":
                dp[i] = dp[i-1]
            if s[i-1] == "0":
                continue
            v = int(s[i-1:i+1])
            if v <= 26:
                if i - 2 >= 0:
                    dp[i] = dp[i] + dp[i-2]
                else:
                    dp[i] = dp[i] + 1

        return dp[-1]

     def numDecodingsOptimize(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = [0] * len(s)+1
        # 哨兵位
        dp[0] = 1
        dp[1] = 1 if int(s[0]) > 0 else 0
        for i in range(2, len(s)+1):
            one = int(s[i-1])
            two = int(s[i-2:i])

            if one >=1:
                dp[i] += dp[i-1]
            if two >= 10 and two <=26:
                dp[i] += dp[i-2]

        return dp[-1]


if __name__ == '__main__':
    pass
