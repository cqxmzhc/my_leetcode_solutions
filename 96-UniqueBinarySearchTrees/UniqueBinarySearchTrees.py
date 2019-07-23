#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution:
    dp = {}

    def numTrees(self, n: int) -> int:
        return self.helper(1, n)

    def helper(self, start, end):
        if (start, end) in self.dp:
            return self.dp[(start, end)]

        if start >= end:
            return 1

        res = 0
        for i in range(start, end+1):
            left_num = self.helper(start, i-1)
            right_num = self.helper(i+1, end)

            res += left_num * right_num

        self.dp[(start, end)] = res

        return res

    def helperIterate(self, n):
        # 子树的数量为0，也应该属于一种状态，所以设为1
        self.dp = [0] * (n+1)
        self.dp[0], self.dp[1] = 1, 1
        # i表示节点的数量
        for i in range(2, n+1):
            # j表示root的位置
            for j in range(1, i+1):
                # 左子树数量 * 右子树数量
                self.dp[i] += self.dp[j-1] * self.dp[i-j]

        return self.dp[-1]


if __name__ == '__main__':
    s = Solution()
    s.generateTrees(3)
