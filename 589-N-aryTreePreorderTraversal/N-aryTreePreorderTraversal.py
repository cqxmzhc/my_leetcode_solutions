#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.common import TreeNode, buildTestTree
import copy
import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        current_layer = [root]
        while current_layer:
            node = current_layer.pop(0)
            res.append(node.val)
            current_layer = node.children + current_layer

        return res



if __name__ == '__main__':
    pass
