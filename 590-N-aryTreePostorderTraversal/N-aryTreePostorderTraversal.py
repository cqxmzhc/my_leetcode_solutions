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
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        时间复杂度:O(n)
        空间复杂度:O(n)
        """
        res = []
        if not root:
            return res

        current_layer = [root]
        while current_layer:
            node = current_layer.pop()
            res.append(node.val)
            # 从左向右的后序遍历结果与从右向左的先序遍历结果相同
            current_layer.extend(node.children)

        return res[::-1]



if __name__ == '__main__':
    pass
