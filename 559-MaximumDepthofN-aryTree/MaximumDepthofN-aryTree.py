#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from common.common import TreeNode, buildTestTree


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        时间复杂度: O(N)
        空间复杂度: O(N)
        """
        if not root:
            return 0

        depth = 1

        current = root.children
        while current:
            next = []
            depth += 1
            for _ in range(0, len(current)):
                next.extend(current.pop(0).children)
            
            current = next
            

        return depth
            

if __name__ == '__main__':
    pass
