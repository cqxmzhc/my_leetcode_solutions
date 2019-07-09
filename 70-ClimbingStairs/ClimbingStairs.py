#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

from common.common import TreeNode, buildTestTree

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairsIteate(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        a = 1
        b = 2
        for i in range(3, n+1):
            tmp = a + b
            a = b
            b = tmp

        return tmp


if __name__ == '__main__':
    pass
