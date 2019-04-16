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
        self.univaluePath(root, False)
        return self.longest

    def univaluePath(self, root, with_parent):
        if not root:
            return 0

        left_univalue_path = 0
        right_univalu_path = 0
        if root.left:
            if root.val == root.left.val:
                left_univalue_path = 1 + self.univaluePath(root.left, True)
            else:
                self.univaluePath(root.left, False)

        if root.right:
            if root.val == root.right.val:
                right_univalu_path = 1 + self.univaluePath(root.right, True)
            else:
                self.univaluePath(root.right, False)

        tmp = left_univalue_path + right_univalu_path
        if self.longest < tmp:
            self.longest = tmp

        if with_parent:
            return left_univalue_path if left_univalue_path > right_univalu_path else right_univalu_path
        else:
            return left_univalue_path + right_univalu_path

if __name__ == '__main__':
    pass
