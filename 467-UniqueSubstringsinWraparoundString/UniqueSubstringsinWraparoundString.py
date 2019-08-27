#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        # 表示以每个字母结尾的唯一字符串在s中的个数
        dp = [0] * 26

        # 以某个字母结尾的在s中连续的字符串的长度(s中的个数)
        max_len = 0
        for i in range(len(p)):
            if i > 0 and (ord(p[i]) - ord(p(i-1)) == 1 or ord(p(i-1))-ord(p(i)) == 25):
                max_len += 1
            else:
                max_len = 1

            index = ord(p[i]) - ord('a')
            dp[index] = max(dp[index], max_len)

        return sum(dp)


if __name__ == '__main__':
    pass
