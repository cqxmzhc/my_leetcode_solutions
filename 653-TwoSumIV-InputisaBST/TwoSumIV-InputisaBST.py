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
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        level_stack = [root]
        exists = set()
        while level_stack:
            node = level_stack.pop()
            if k - node.val in exists:
                return True
            else:
                exists.add(node.val)

            if node.left:
                level_stack.append(node.left)
            if node.right:
                level_stack.append(node.right)

        return False
                
if __name__ == '__main__':
    pass
