#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        row_len = len(matrix)
        if row_len == 0:
            return
        col_len = len(matrix[0])
        if col_len == 0:
            return

        self.dp = [[0 for j in range(0, col_len+1)] for i in range(0, row_len)]
        self.dp[0][0] = matrix[0][0]
        for i in range(0, row_len):
            for j in range(0, col_len):
                self.dp[i][j+1] = self.dp[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = 0
        for i in range(row1, row2+1):
            sum += self.dp[i][col2+1] - self.dp[i][col1]

        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
if __name__ == '__main__':
    pass
