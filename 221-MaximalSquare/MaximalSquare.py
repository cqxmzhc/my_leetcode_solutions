#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 暴力破解法
        rows = len(matrix)
        if rows == 0:
            return 0
        cols = len(matrix[0])

        maxsqlen = 0

        # 遍历每个节点
        for i in range(0, rows):
            for j in range(0, cols):
                # if i == 1 and j == 2:
                #     import pdb
                #     pdb.set_trace()
                # 判断当前节点是否为1， 以当前节点为所求正方形(square)的左上角顶点由内向外检查每条边的节点是否为1
                if matrix[i][j] == "1":
                    # 当前square的边长
                    sqlen = 1
                    # 每条边的节点都为1
                    flag = True
                    while(i+sqlen < rows and j+sqlen < cols and flag):
                        # 上边和右边
                        for k in range(i, i+sqlen+1):
                            if matrix[k][j+sqlen] == "0":
                                flag = False
                                break

                        # 左边和下边
                        for k in range(j, j+sqlen+1):
                            if matrix[i+sqlen][k] == "0":
                                flag = False
                                break

                        if flag:
                            sqlen += 1

                    if maxsqlen < sqlen:
                        maxsqlen = sqlen

        return maxsqlen * maxsqlen

    def maximalSquareDP(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 矩阵中的每个节点表示待求正方体的右下角节点
        # dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
        rows = len(matrix)
        if rows == 0:
            return 0
        cols = len(matrix[0])

        maxsqlen = 0
        dp = [[0 for j in range(0, cols)] for i in range(0, rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    # 第一行第一列的节点
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i][j-1], dp[i-1]
                                       [j-1], dp[i-1][j]) + 1

                    if dp[i][j] > maxsqlen:
                        maxsqlen = dp[i][j]

        return maxsqlen * maxsqlen

    def maximalSquareDPM(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 矩阵中的每个节点表示待求正方体的右下角节点
        # dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
        rows = len(matrix)
        if rows == 0:
            return 0
        cols = len(matrix[0])

        maxsqlen = 0
        dp_diagonal = 0
        dp = [0] * (cols+1)
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                tmp = dp[j]
                if matrix[i-1][j-1] == "1":
                    dp[j] = min(dp[j-1], dp_diagonal, dp[j])+1

                    maxsqlen = max(maxsqlen, dp[j])
                else:
                    dp[j] = 0

                dp_diagonal = tmp

        return maxsqlen * maxsqlen


if __name__ == "__main__":
    s = Solution()
    s.maximalSquareDPM([["1", "0", "1", "0"], ["1", "0", "1", "1"], [
                       "1", "0", "1", "1"], ["1", "1", "1", "1"]])
