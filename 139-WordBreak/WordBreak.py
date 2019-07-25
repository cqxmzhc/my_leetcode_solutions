#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s)+1)
        # 哨兵位， 检查整个字符串是否属于字典
        dp[0] = True
        # 长度为i的字符串是否满足条件
        dp[1] = s[0] in wordDict
        for i in range(2, len(s)+1):
            # 从第i位置依次向前检查是否属于字典中的词
            for j in range(1, i+1):
                if (dp[i-j] and s[i-j:i] in wordDict):
                    dp[i] = True
                    break

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("aaaaaaa", ["aaaa", "aaa"]))
