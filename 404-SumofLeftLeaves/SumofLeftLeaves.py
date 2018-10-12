#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from common.common import TreeNode, buildTree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return self.recur(root, False)

    def recur(self, root, left):
        left_tree_sum = 0
        right_tree_sum = 0

        if not root.left and not root.right and left:
            return root.val
        if root.left:
            left_tree_sum = self.recur(root.left, True)
        if root.right:
            right_tree_sum = self.recur(root.right, False)

        return left_tree_sum + right_tree_sum

    def iterate(self, root):
        if not root:
            return 0
        stack = [(root, False)]
        left_sum = 0
        while len(stack) > 0:
            current_node, left = stack.pop()
            if not current_node.left and not current_node.right and left:
                left_sum += current_node.val
            if current_node.left:
                stack.append((current_node.left, True))
            if current_node.right:
                stack.append((current_node.right, False))

        return left_sum


if __name__ == '__main__':
    pass
