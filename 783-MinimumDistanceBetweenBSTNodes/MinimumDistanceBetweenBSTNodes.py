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
    min_diff = float("inf")
    cur = -float("inf")

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(node):
            if node:
                inorder(node.left)
                self.min_diff = min(node.val - self.cur, self.min_diff)
                self.cur = node.val
                inorder(node.right)

        inorder(root)
        return self.min_diff


if __name__ == '__main__':
    pass
