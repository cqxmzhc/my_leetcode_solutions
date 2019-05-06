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
    sum_numbers = 0
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, prefix):
            if not root:
                return
            if not root.left and not root.right:
                self.sum_numbers += int(prefix + str(root.val), 2)
                return
            dfs(root.left, prefix + str(root.val))
            dfs(root.right, prefix + str(root.val))

        if not root.left and not root.right:
            # 二进制值得拼接可以通过2*x+y的形式替换
            return int(str(root.val), 2)
        # 参数为下一个节点， 以及截至父节点为止的节点值前缀
        dfs(root.left, str(root.val))
        dfs(root.right, str(root.val))

        return self.sum_numbers

if __name__ == '__main__':
    pass
