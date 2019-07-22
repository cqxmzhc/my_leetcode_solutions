#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 保存[i-1][j]位置的值， 实时计算[i][j-1]的值
        dp = [0] * m
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                # 只能向下或向右移动，所以第一行和第一列的路径是唯一的
                # 第一列
                if j == 0:
                                        # 这里的dp[j]代表的是当前位置上一行的值
                    dp[j] = grid[i][j] + dp[j]
                # 第一行
                elif i == 0 and j > 0:
                    dp[j] = grid[i][j] + dp[j-1]
                else:
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    t = [[1, 2], [1, 1]]
    s.minPathSum(t)
