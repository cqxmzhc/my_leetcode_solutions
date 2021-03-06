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
    modes = []
    pre_val = None
    current_count = 0
    max_count = 0

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        时间复杂度O(N)
        空间复杂度O(1)
        """
        if not root:
            return

        self.findMode(root.left)

        if root.val == self.pre_val:
            self.current_count += 1
        else:
            self.current_count = 1

        if self.current_count > self.max_count:
            self.max_count = self.current_count
            self.modes = [root.val]
        elif self.current_count == self.max_count:
            self.modes.append(root.val)

        self.pre_val = root.val

        self.findMode(root.right)

        return self.modes

    def findModeIterate(self, root):
        """
        中序遍历
        """

        if not root:
            return self.modes
        stack = []

        current_node = root
        while current_node or stack:
            left_visited = False
            if not current_node:
                left_visited, current_node = stack.pop()

            # 左节点存在且没有被访问过，继续遍历左子树
            if current_node.left and not left_visited:
                stack.append((True, current_node))
                current_node = current_node.left
            # 左节点不存在或者已经被访问
            else:
                if current_node.val == self.pre_val:
                    self.current_count += 1
                else:
                    self.current_count = 1

                if self.current_count > self.max_count:
                    self.max_count = self.current_count
                    self.modes = [current_node.val]
                elif self.current_count == self.max_count:
                    self.modes.append(current_node.val)

                self.pre_val = current_node.val
                current_node = current_node.right

        return self.modes


if __name__ == '__main__':
    root = buildTestTree([1, None, 2, 2])
    s = Solution()
    print(s.findModeIterate(root))
