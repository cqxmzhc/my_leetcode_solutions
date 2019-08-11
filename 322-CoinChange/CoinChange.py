#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = [-1] * (amount+1)
        dp[0] = -1
        dp[1] = 1 if 1 in coins else -1

        for i in range(2, amount+1):
            import pdb
            pdb.set_trace()
            min_num = float("+inf")
            for j in coins:
                if i == j:
                    dp[i] = 1
                    break
                if i - j > 0:
                    if dp[i-j] != -1 and dp[i-j] + 1 < min_num:
                        min_num = dp[i-j] + 1
            if min_num != float("+inf"):
                dp[i] = min_num

        return dp[amount]


if __name__ == '__main__':
    s = Solution()
    s.coinChange([1, 2], 2)
