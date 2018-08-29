#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from common.common import TreeNode, Stack
from collections import queue

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        # 先序遍历左子树
        left_sub_tree_stack = Stack()
        left_sub_tree_pre_order_seq = []

        node = root.left
        while node != None or left_sub_tree_stack.length > 0:
            if node != None:
                left_sub_tree_pre_order_seq.append(node.value)
                if node.right != None:
                    left_sub_tree_stack.push(node.right)

                node = node.left
            else:
                left_sub_tree_pre_order_seq.append(None)
                node = left_sub_tree_stack.pop()

        print(left_sub_tree_pre_order_seq)

        # 相反方向遍历右子树
        right_sub_tree_stack = Stack()
        right_sub_tree_post_order_seq = []

        node = root.right
        while node != None or right_sub_tree_stack.length > 0:
            if node != None:
                right_sub_tree_post_order_seq.append(node.value)
                if node.left != None:
                    right_sub_tree_stack.push(node.left)

                node = node.right
            else:
                right_sub_tree_post_order_seq.append(None)
                node = right_sub_tree_stack.pop()

        print(right_sub_tree_post_order_seq)

        return left_sub_tree_pre_order_seq == right_sub_tree_post_order_seq

    def isSymmetricBFS(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        stack = [[root.left, root.right]]

        while len(stack) > 0:
            pair = stack.pop(0)

            left = pair[0]
            right = pair[1]

            if left == None and right == None:
                continue
            if left == None or right == None:
                return False
            if left.val == right.val:
                stack.extend([[left.left, right.right],
                              [left.right, right.left]])
            else:
                return False

        return True


def buildTestTree(level_order_seq):
    len_seq = len(level_order_seq)
    level_order_map = {}
    root = None
    for i in range(1, len_seq+1):
        if level_order_seq[i-1] == None:
            continue

        left = None
        right = None

        if 2*i-1 < len_seq:
            v = level_order_seq[2*i-1]
            if v != None:
                left = level_order_map.setdefault(
                    2*i, TreeNode(v, None, None))

        if 2*i < len_seq:
            v = level_order_seq[2*i]
            if v != None:
                right = level_order_map.setdefault(
                    2*i+1, TreeNode(v, None, None))

        if i == 1:
            root = TreeNode(level_order_seq[i-1], left, right)
        else:
            parent = level_order_map[i]
            parent.left = left
            parent.right = right

    return root


if __name__ == '__main__':
    root = buildTestTree([1, 2, 2, None, 3, None, 3])

    s = Solution()
    print(s.isSymmetric(root))
