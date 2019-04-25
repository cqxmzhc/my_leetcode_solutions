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
    res = None

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            root.left = None
            self.last.right = root
            self.last = root
            inorder(root.right)

        # 结果root节点
        # 中序遍历每一个节点， self.last记录当前访问的节点，当访问下一个节点时，把当前节点的右节点指向下一个节点，下一个节点变为当前节点，依此循环
        res = self.last = TreeNode()
        inorder(root)
        return res.right


if __name__ == '__main__':
    pass
