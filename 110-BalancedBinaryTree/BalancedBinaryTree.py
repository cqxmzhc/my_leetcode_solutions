#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # import pdb
        # pdb.set_trace()
        if root == None:
            return True

        return self.treeDepth(root) != -1

    def treeDepth(self, root):
        if root == None:
            return 0

        left_sub_tree_depth = self.treeDepth(root.left)
        if left_sub_tree_depth == -1:
            return -1
        right_sub_tree_depth = self.treeDepth(root.right)

        if right_sub_tree_depth == -1:
            return -1

        if abs(left_sub_tree_depth-right_sub_tree_depth) > 1:
            return -1

        return max(left_sub_tree_depth, right_sub_tree_depth)+1

    def isBalancedIterative(self, root):
        """
        后序遍历所有节点，检查每个节点的左右是否是平衡的
        """
        # 使用栈实现后续遍历
        stack = []

        # 当前节点
        node = root

        # 上一个处理的节点
        last = None

        # 每个节点的高度
        depths = {}

        while len(stack) > 0 or node != None:
            # 后序遍历，从root节点开始先将左子树的根节点压入栈中
            if node != None:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                # 右子节点不存在或者已经被处理， 第二次经过根节点
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right = depths.get(
                        node.left, 0), depths.get(node.right, 0)
                    if abs(left-right) > 1:
                        return False
                    depths[node] = max(left, right) + 1
                    last = node
                    node = None
                else:
                    node = node.right

        return True


if __name__ == '__main__':
    root = buildTestTree([3, 9, 20, None, None, 15, 7])
    s = Solution()
    print(s.isBalanced(root))
