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
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""

        if not t.left and not t.right:
            return str(t.val)

        if not t.left:
            return str(t.val) + "()(" + self.tree2str(t.right) + ")"

        if not t.right:
            return str(t.val) + "(" + self.tree2str(t.left) + ")"

        return str(t.val) + "(" + self.tree2str(t.left) + ")(" + self.tree2str(t.right) + ")"

    def tree2strIter(self, t):
        if not t:
            return ""

        res = ""
        layer = [t]
        while layer:
            ele = layer.pop(0)
            if ele == ")":
                res += ele
            else:
                res += "(" + str(ele.val)
                if not ele.left and ele.right:
                    res += "()"
                if ele.right:
                    layer = [ele.right, ")"] + layer
                if ele.left:
                    layer = [ele.left, ")"] + layer

        return res[1:]


if __name__ == '__main__':
    pass
