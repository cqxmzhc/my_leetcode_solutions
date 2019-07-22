#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

from common.common import TreeNode, buildTestTree

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1

        fib1 = 0
        fib2 = 1
        for i in range(2, N+1):
            fn = fib1 + fib2
            fib1, fib2 = fib2, fn

        return fn


if __name__ == '__main__':
    pass
