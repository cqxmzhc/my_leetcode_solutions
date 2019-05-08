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
                2. 匹配多次(这种情况的前提一定是x*中的x和原始字符串中的字符匹配上了), x*匹配多次的
        """
        
if __name__ == '__main__':
    pass
