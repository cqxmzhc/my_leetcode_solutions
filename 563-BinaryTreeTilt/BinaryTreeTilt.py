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
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        时间复杂度: O(N^2)
        空间复杂度: O(N^2)
        """
        if not root:
            return 0

        root_tilt = abs(self.sumOfTree(root.left)-self.sumOfTree(root.right))

        return root_tilt + self.findTilt(root.left) + self.findTilt(root.right)

    def sumOfTree(self, root):
        if not root:
            return 0

        return root.val + self.sumOfTree(root.left) + self.sumOfTree(root.right)

    
    def findTiltBetter(self, root):
        """
        :type root: TreeNode
        :rtype: int
        时间复杂度: O(N)
        空间复杂度: O(N)
        """
        self.tilt = 0
        def helper(root):
            if not root:
                return 0
                
            left = helper(root.left)
            right = helper(root.right)

            self.tilt += abs(left-right)
            return root.val + left + right
            
        helper(root)
        return self.tilt

if __name__ == '__main__':
    pass
