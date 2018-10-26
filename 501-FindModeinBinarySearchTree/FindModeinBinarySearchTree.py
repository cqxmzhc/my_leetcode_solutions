#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)
from common.common import TreeNode, buildTestTree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    modes = []
    pre_val = None
    current_count = 0
    max_count = 0

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return

        self.findMode(root.left)

        if root.val == self.pre_val:
            self.current_count += 1
        else:
            self.current_count = 1

        if self.current_count > self.max_count:
            self.max_count = self.current_count
            self.modes = [root.val]
        elif self.current_count == self.max_count:
            self.modes.append(root.val)

        self.pre_val = root.val

        self.findMode(root.right)

        return self.modes


if __name__ == '__main__':
    root = buildTestTree([1, None, 2])
    s = Solution()
    print(s.findMode(root))
