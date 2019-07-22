#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 行
        n = len(obstacleGrid)
        # 列
        m = 0 if n == 0 else len(obstacleGrid[0])
        # dp = [[0] * m] * n
        dp = [[0 for j in range(0, m)] for i in range(0, n)]
        for i in range(0, n):
            for j in range(0, m):
                # 第一行第一列路径唯一
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid[0])
        # 保存[i-1][j]位置的值， [i][j-1]的值可以实时求得
        dp = [0] * m
        # 0表示左上角起始位置
        dp[0] = 1

        for row in obstacleGrid:
            for j in range(0, m):
                if row(j) == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] = dp[j] + dp[j-1]

        return dp[-]


if __name__ == '__main__':
    s = Solution()
    g = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    s.uniquePathsWithObstacles(g)
