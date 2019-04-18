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
    longest = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.univaluePath(root)
        return self.longest

    def univaluePath(self, root):
        if not root:
            return 0

        left = self.univaluePath(root.left)
        right = self.univaluePath(root.right)

        arrow_left = 0
        arrow_right = 0
        if root.left and root.left.val == root.val:
            arrow_left = 1 + left
        if root.right and root.right.val == root.val:
            arrow_right = 1 + left

        self.longest = max(self.longest, arrow_left + arrow_right)

        return max(left, right)


if __name__ == '__main__':
    pass
