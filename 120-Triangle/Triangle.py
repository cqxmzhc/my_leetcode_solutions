#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

from common.common import TreeNode, buildTestTree

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        length = len(triangle)
        if length == 0:
            return 0
        dp = [0] * length
        for i in range(1, length):
            dp1 += min(triangle[i])

        return dp1


if __name__ == '__main__':
    pass
