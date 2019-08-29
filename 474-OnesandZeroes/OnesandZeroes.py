#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        0-1背包问题, strs数组中的数字作为物体, m和n分别作为需要被填充的背包
        """
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # print(dp)
        for num in strs:
            one_count = 0
            zero_count = 0
            for i in num:
                if i == "1":
                    one_count += 1
                else:
                    zero_count += 1

            # 循环到此处表示的是我们考虑选择当前字符串
            # 对于二维数组dp， 如果更新顺序是从左上角(top left)到右下角(bottom right), 后续的元素更新会使用的前面已经被更新的元素的值(选择当前字符串已经+1), 所以会导致重复计算
            # 从右下角更新到左上角，使用的更新元素是在当前选择字符串下未被更新的值
            # for k in range(zero_count, m+1):
            #     for j in range(one_count, n+1):
            #         dp[k][j] = max(dp[k][j], dp[k-zero_count][j-one_count])

            for k in range(m, zero_count-1, -1):
                for j in range(n, one_count-1, -1):
                    dp[k][j] = max(dp[k][j], dp[k-zero_count][j-one_count] + 1)

        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    s.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)
