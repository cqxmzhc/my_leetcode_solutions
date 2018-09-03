#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from common.common import buildTestTree, TreeNode, levelorder

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return 0

        left_sub_tree_depth = self.isBalanced(root.left) + 1
        right_sub_tree_depth = self.isBalanced(root.right) + 1

        return abs(left_sub_tree_depth - right_sub_tree_depth) > 1


if __name__ == '__main__':
    root = buildTestTree([1, 2, 3, 4, 5])
    s = Solution()
    print(s.isBalanced(root))
