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
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        if not t1:
            return t2
        elif not t2:
            return t1
        else:
            t1.val += t2.val
            t1.left =self.mergeTrees(t1.left, t2.left)
            t1.right =self.mergeTrees(t1.right, t2.right)
            return t1

    def mergeTreesIter(self, t1, t2):
        """
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        if not t1:
            return t2
        elif not t2:
            return t1

        traverse_stack = [(t1, t2)]

        while traverse_stack:
            t1_current, t2_current = traverse_stack.pop()
            t1_current.val += t2_current.val

            if not t1_current.left:
                t1_current.left = t2_current.left
            elif t2_current.left:
                traverse_stack.append((t1_current.left, t2_current.left))

            if not t1_current.right:
                t1_current.right = t2_current.right
            elif t2_current.right:
                traverse_stack.append((t1_current.right, t2_current.right))

        return t1

if __name__ == '__main__':
    pass
