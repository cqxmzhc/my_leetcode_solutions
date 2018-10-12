#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from common.common import TreeNode, buildTree


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [root]
        res = []
        while len(stack) > 0:
            row_val = []
            row_stack = []
            for i in stack:
                row_val.append(i.val)
                row_stack += (i.children)

            res.append(row_val)
            stack = row_stack

        return res

    def levelOrder(self, root):
        stack = [root] if root else []
        res = []
        while stack:
            res.append([node.val for node in stack])
            stack = [child for node in stack for child in node.children]

        return res


if __name__ == '__main__':
    pass
