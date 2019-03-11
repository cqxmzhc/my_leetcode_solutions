#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.common import TreeNode, buildTestTree
import copy
import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        时间复杂度: O(m*n)
        """
        def identical(s, t):
            if not s and not t:
                return True

            if not s or not t:
                return False

            # n次
            if s.val == t.val and identical(s.left, t.left) and identical(s.right, t.right):
                return True

            return False

        # if identical(s, t) or identical(s.left, t) or identical(s.right, t):
        #     return True

        if identical(s, t):
            return True

        # m次
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSubtreeBetter(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def identical(s, t, must_equal):
            """
            时间复杂度: O(m*n)
            """
            if not s and not t:
                return True

            if not s or not t:
                return False

            if s.val == t.val:
                return (identical(s.left, t.left, True) and identical(s.right, t.right, True)) or identical(s.left, t, False) or identical(s.right, t, False)
            elif must_equal:
                return False
            else:
                return identical(s.left, t, False) or identical(s.right, t, False)

        return identical(s, t, False)


if __name__ == '__main__':
    pass
