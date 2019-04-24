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
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(root, leafs):
            if not root.left and not root.right:
                leafs.append(root.val)
                return
            if root.left:
                dfs(root.left, leafs)
            if root.right:
                dfs(root.right, leafs)

        def dfsIterate(root, leafs):
            stack_node = [root]

            while stack_node:
                node = stack_node.pop()
                if not node.left and not node.right:
                    leafs.append(node.val)

                if node.right:
                    stack_node.append(node.right)
                if node.left:
                    stack_node.append(node.left)


        left_leafs = []
        # dfs(root1, left_leafs)
        dfsIterate(root1, left_leafs)

        right_leafs = []
        # dfs(root2, right_leafs)
        dfsIterate(root2, right_leafs)

        return left_leafs == right_leafs

            


if __name__ == '__main__':
    pass
