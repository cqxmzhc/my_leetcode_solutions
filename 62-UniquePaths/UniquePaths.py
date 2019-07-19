#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

from common.common import TreeNode, buildTestTree

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        时间复杂度 O(mn)
        空间复杂度 O(mn)
        """
        dp = [[0]*m] * n
        # 只能向右到达，路径唯一
        # 行
        for i in range(0, n):
            dp[i][0] = 1

        # 只能向下到达，路径唯一
        # 列
        for j in range(0, m):
            dp[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        时间复杂度 O(mn)
        空间复杂度 O(n)
        """
        # 只需保存所求位置当前列以及前一列的数据
        curr_row = [0] * n
        # 第一列路径唯一
        pre_row = [1] * n

        # 列
        for j in range(1, m):
            # 行
            for i in range(0, n):
                if i == 0:
                    # 第一行路径唯一
                    curr_row[i] = pre_row[i]
                else:
                    curr_row[i] = pre_row[i] + curr_row[i-1]

            # swap
            pre_row, curr_row = curr_row, pre_row

        # pre, curr已经交换， pre是最后一列
        return pre_row[-1]

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        时间复杂度 O(mn)
        空间复杂度 O(n)
        """
        # 第一列路径唯一
        curr_row = [1] * n

        # 列
        for j in range(1, m):
            # 行
            for i in range(1, n):
                curr_row[i] = curr_row[i] + curr_row[i-1]

        return curr_row[-1]


if __name__ == '__main__':
    pass
