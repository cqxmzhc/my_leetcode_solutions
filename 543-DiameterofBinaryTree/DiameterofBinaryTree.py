#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from common.common import TreeNode, buildTestTree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        时间复杂度: O(N^2)
        """
        if not root:
            return 0

        depth = self.depthOfBinaryTree(root.left) + self.depthOfBinaryTree(root.right)
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter= self.diameterOfBinaryTree(root.right)

        if left_diameter > depth:
            depth = left_diameter
        if right_diameter > depth:
            depth = right_diameter

        return depth
        

    def depthOfBinaryTree(self,root):
        if not root:
            return 0

        depth_of_left_tree = self.depthOfBinaryTree(root.left)
        depth_of_right_tree = self.depthOfBinaryTree(root.right)

        depth_of_tree = depth_of_left_tree if depth_of_left_tree>depth_of_right_tree else depth_of_right_tree
        return depth_of_tree +1

    
    def diameterOfBinaryTreeBetter(self, root):
        """
        :type root: TreeNode
        :rtype: int
        时间复杂度: O(N)
        """
        # 树的直径定义为这个树中任意两个节点的之间边长度的最大值，这个值一定是以某个节点为根的子树的左右子树深度之和
        # 所以求树的直径即是遍历每个节点求得以此节点为根的树的左右子树深度之和的最大值
        self.dia = 0

        def depthOfBinaryTree(root):
            if not root:
                return 0

            depth_of_left_tree = depthOfBinaryTree(root.left)
            depth_of_right_tree = depthOfBinaryTree(root.right)

            if depth_of_left_tree + depth_of_right_tree > self.dia:
                self.dia = depth_of_left_tree + depth_of_right_tree

            return max(depth_of_left_tree, depth_of_right_tree) + 1

        depthOfBinaryTree(root)
        return self.dia

if __name__ == '__main__':
    pass
