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
        dp = [0] + [float("+inf")] * (amount)
        for i in range(1, amount+1):
            for j in coins:
                if i - j >= 0:
                    dp[i] = min(dp[i], dp[i-j]+1)

        return dp[-1] if dp[-1] != float("+inf") else -1


if __name__ == '__main__':
    pass
