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
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        elif root.left == None and root.right == None and root.val == sum:
            return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum-root.val)

    def hasPathSumIterate(self, root, sum):
        """
        层序遍历
        """
        # 每行的节点与当前接待你到root的sum对应
        if root == None:
            return False
        node_array = [root]
        path_sum_array = [root.val]

        while len(node_array) > 0:
            row_path_sum = []
            row_node = []
            for i, v in enumerate(node_array):
                if v.left == None and v.right == None and path_sum_array[i] == sum:
                    return True
                if v.left != None:
                    row_node.append(v.left)
                    row_path_sum.append(path_sum_array[i]+v.left.val)
                if v.right != None:
                    row_node.append(v.right)
                    row_path_sum.append(path_sum_array[i]+v.right.val)

            node_array = row_node
            path_sum_array = row_path_sum

        return False


if __name__ == '__main__':
    pass
