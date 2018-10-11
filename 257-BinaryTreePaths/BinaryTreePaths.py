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
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []

        if root.left == None and root.right == None:
            return [str(root.val)]

        return self.recur(root.left, str(root.val)) + self.recur(root.right, str(root.val))

    def recur(self, root, path):
        left_path = []
        right_path = []

        if root == None:
            return []

        if root.left == None and root.right == None:
            return [path + "->" + str(root.val)]

        if root.left != None:
            left_path = self.recur(root.left, path+"->"+str(root.val))

        if root.right != None:
            right_path = self.recur(root.right, path+"->"+str(root.val))

        return left_path+right_path


if __name__ == '__main__':
    pass
