#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

from common.common import TreeNode, buildTestTree

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    range_sum = 0
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root:
            if root.val >= L:
                self.rangeSumBST(root.left, L, R)
            if L <= root.val <= R:
                self.range_sum += root.val
            if root.val <= R:
                self.rangeSumBST(root.right, L, R)
            return self.range_sum


if __name__ == '__main__':
    pass
