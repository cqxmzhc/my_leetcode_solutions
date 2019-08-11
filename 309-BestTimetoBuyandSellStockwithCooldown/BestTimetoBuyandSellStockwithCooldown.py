#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

<<<<<<< HEAD
from common.common import TreeNode, buildTestTree
=======
>>>>>>> 7eb6699f64c40ce4640d32974ee7d5f862a3508d

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
<<<<<<< HEAD
=======

        buy[i]: To make a decision whether to buy at i, we either take a rest, by just using the old decision at i - 1, or sell at/before i - 2, then buy at i, We cannot sell at i - 1, then buy at i, because of cooldown.
        sell[i]: To make a decision whether to sell at i, we either take a rest, by just using the old decision at i - 1, or buy at/before i - 1, then sell at i.
>>>>>>> 7eb6699f64c40ce4640d32974ee7d5f862a3508d
        """
        length = len(prices)
        if length < 2:
            return 0

<<<<<<< HEAD
        dp = [0] * length
        dp[1] = prices[1] - prices[0]

        for i in range(2, length):
            dp[i] = max(dp[i-1], dp[i-2]+prices[-1])

        return dp[-1]


if __name__ == '__main__':
    pass
=======
        # 第i天以buy作为结尾
        b0 = -prices[0]
        b1 = -1 * prices[0] if prices[1] > prices[0] else -1 * prices[1]
        # 第i天以sell作为结尾
        s0 = 0
        s1 = prices[1] - prices[0] if prices[1] > prices[0] else 0

        # import pdb
        # pdb.set_trace()
        for i in range(2, length):
            b2 = max(b1, s0 - prices[i])
            s2 = max(s1, b1 + prices[i])

            b0, b1 = b1, b2
            s0, s1 = s1, s2

        return s1


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([2, 1, 4]))
>>>>>>> 7eb6699f64c40ce4640d32974ee7d5f862a3508d
