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
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        g = {}
        def dfs(root, depth, parent):
            if not root:
                return
            if root.val in (x, y):
                g[root.val] = (depth,parent)
            dfs(root.left, depth + 1,root)
            dfs(root.right, depth + 1,root)

        dfs(root, 0, None)

        return g[x][0] == g[y][0] and g[x][1] != g[y][1]

    def isCousinsBfs(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        # 在某个depth中， 记录x或y的父节点
        first_parent = None
        parent = [root]

        if root.val in (x,y):
            return False

        
        while parent:
            next_depth = []
            # 遍历同一深度的节点
            for node in parent:
                for next_node in (node.left, node.right):
                    if next_node:
                        if next_node.val in (x, y):
                            # 如果first_parent已经存在， 说明x, y在同一个depth， 现在需要判断他们的父节点是否是同一个
                            if first_parent:
                                return first_parent != node
                            else:
                                # x或y中的某一个值出现在此depth所在节点中
                                first_parent = node

                        next_depth.append(next_node)

            # 此depth循环完成后， 如果first_node存在说明x, y只有一个值在这个depth中，不满足条件， 返回false
            if first_parent:
                return False

            # 开始下一循环
            parent = next_depth

            
                

            
if __name__ == '__main__':
    pass
