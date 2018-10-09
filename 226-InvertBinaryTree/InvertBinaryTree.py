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
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode

        time complexity O(n)
        space complexity O(n)
        """
        if root == None:
            return None

        node_stack = [root]
        while len(node_stack) > 0:
            current_node = node_stack.pop(0)
            if current_node.left == None and current_node.right == None:
                continue
            else:
                current_node.left, current_node.right = current_node.right, current_node.left
                if current_node.left != None:
                    node_stack.append(current_node.left)
                if current_node.right != None:
                    node_stack.append(current_node.right)

        return root


if __name__ == '__main__':
    pass
