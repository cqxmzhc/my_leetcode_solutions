#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

from common.common import TreeNode, buildTestTree

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float("+inf")
        max_profit = 0

        for i in prices:
            if i > min_price:
                if i - min_price > max_profit:
                    max_profit = i - min_price
            else:
                min_price = i

        return max_profit


if __name__ == '__main__':
    pass
