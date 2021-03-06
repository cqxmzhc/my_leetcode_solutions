#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n):
            # import pdb
            # pdb.set_trace()
            if n in dp:
                return dp[n]

            if n < 0:
                return float("+inf")
            else:
                tmp = float("+inf")
                for i in ps:
                    s = helper(n-i)
                    if s < tmp:
                        tmp = s

                dp[n] = tmp+1
                return tmp

        ps = []
        dp = {0: 0, 1: 1, 2: 2, 3: 3}
        i = 1
        while True:
            t = i*i
            if t <= n:
                ps.append(t)
                i += 1
            else:
                break

        for i in range(1, n+1):
            helper(i)

        return dp[n]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        ps = []
        dp = {0: 0, 1: 1, 2: 2, 3: 3}
        i = 1
        while True:
            t = i*i
            if t <= n:
                ps.append(t)
                i += 1
            else:
                break

        for i in range(1, n+1):
            tmp = float("+inf")
            for num in ps:
                if i - num in dp and dp[i-num] < tmp:
                    tmp = dp[i-num]

            dp[i] = tmp+1

        return dp[n]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        广度优先
        """
        if n < 2:
            return n
        ps = None
        to_check = [n]
        while True:
            t = i*i
            if t <= n:
                ps.append(t)
                i += 1
            else:
                break

        # 层序遍历
        while to_check:
            tmp = set()
            count = 1
            for i in to_check:
                for j in ps:
                    if i == j:
                        return count
                    if i < j:
                        # 当前路径无法凑出目标值
                        break
                    tmp.append(i-j)
                    count += 1

            to_check = tmp


if __name__ == "__main__":
    s = Solution()
    s.numSquares(17)
