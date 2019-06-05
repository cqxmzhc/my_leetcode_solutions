#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

from common.common import TreeNode, buildTestTree

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        思路:
        1. pattern可以分为两种情况
            a. 无*
                只需依次匹配字符是否相同或者pattern中的字符为"."
            b. 有*
                可以继续分为两种情况
                1. 匹配0次, 即pattern中的x*(x表示任意字符,包括".")可以忽略, 用剩下的pattern匹配完整的原始字符(递归)
                2. 匹配多次(这种情况的前提一定是x*中的x和原始字符串中的某个字符匹配上了), x*匹配多次的可以继续使用x*表示, 也就是继续使用(x*....)pattern匹配剩下的字符串
        """
        # s, p可以为空
        if p == "":
            return not s

        first_match = s and p[0] in (s[0], ".")

        if len(p) >= 2 and p[1] == "*":
            return (first_match or self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    def isMatchDP(self, s, p):
        # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the table with False. The first row is satisfied.
        # table[0][j]表示p为空字符串时的匹配情况, 除了table[0][0]表示p和s都为空字符串时为true， 其他情况都为false
        table=[[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        table[0][0]=True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        # table[i][0]表示s为空字符串时的匹配情况, table[1][0]表示p只有一个字符，这种情况匹配不可能成功，所以直接跳过从2开始
        # s为空字符串时, 只有当p为[x*]+这种模式时才能匹配上
        for i in range(2, len(p) + 1):
            table[i][0]=table[i - 2][0] and p[i - 1] == '*'

        # 使用p中的每一个字符依次匹配s
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    # 这里其实就有dp的思路了: 当前位置是否匹配成功的这样一种状态可以由前一位置的匹配状态来确定
                    table[i][j]=table[i - 1][j - 1] and \
                                  (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    # 两种情况
                        # 1. 要么是(i-2)位置匹配成功, (i-1)无论是什么都能匹配成功
                        # 2. 要么(i-1)匹配成功
                    table[i][j]=table[i - 2][j] or table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    # ?
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]

if __name__ == '__main__':
    pass
