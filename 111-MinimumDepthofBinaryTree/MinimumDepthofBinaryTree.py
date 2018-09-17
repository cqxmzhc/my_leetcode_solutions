#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from common.common import buildTestTree, TreeNode, levelorder

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left_subtree_depth = self.minDepth(root.left)
        right_subtree_depth = self.minDepth(root.right)

        # 如果子节点为空， 不能作为最小深度计算
        return (min(left_subtree_depth, right_subtree_depth) or max(left_subtree_depth, right_subtree_depth)) + 1

    def minDepthIterate(self, root):
        """
        迭代方式，层序遍历，遇到的第一个叶子节点就是最小深度的节点
        """
        if not root:
            return 0

        queue = [root]
        min_depth = 0
        row_node_num = 1

        while row_node_num > 0:
            min_depth += 1
            while row_node_num > 0:
                current_node = queue.pop(0)
                if not current_node.left and not current_node.right:
                    return min_depth

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

                row_node_num -= 1

            row_node_num = len(queue)


if __name__ == '__main__':
    pass
