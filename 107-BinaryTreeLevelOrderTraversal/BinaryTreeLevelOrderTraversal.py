#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from common.common import buildTestTree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root == None:
            return []

        res = []
        current_node_stack = [root]
        next_node_stack = []
        while True:
            tmp = []
            while len(current_node_stack) > 0:
                node = current_node_stack.pop(0)
                tmp.append(node.val)
                if node.left:
                    next_node_stack.append(node.left)
                if node.right:
                    next_node_stack.append(node.right)

            # import pdb
            # pdb.set_trace()
            res.insert(0, tmp)

            if len(next_node_stack) == 0:
                break
            current_node_stack = next_node_stack
            next_node_stack = []

        return res


if __name__ == '__main__':
    root = buildTestTree([1, 2, 3, 4, None, 5, 6, None, 7])
    s = Solution()
    print(s.levelOrderBottom(root))
