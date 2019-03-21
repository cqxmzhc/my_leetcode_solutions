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
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def minimum(root, m):
            if not root:
                return m
            
            return min(root.val, minimum(root.left, root.val), minimum(root.right, root.val))
        
        if not root or not root.left:
            return -1

        if root.val == root.left.val:
            left = self.findSecondMinimumValue(root.left)
        else:
            left =  minimum(root.left, root.val)

        if root.val == root.right.val:
            right = self.findSecondMinimumValue(root.right)
        else:
            right = minimum(root.right, root.val)


        if left == -1: return right
        if right == -1: return left 

        return left if left < right else right

                
if __name__ == '__main__':
    pass
