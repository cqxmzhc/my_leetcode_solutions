#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from common.common import buildTestTree, TreeNode


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        len_nums = len(nums)

        if len_nums == 0:
            return None

        mid_index = len_nums // 2
        root = TreeNode(nums[mid_index])

        root.left = self.sortedArrayToBST(nums[0:mid_index])
        root.right = self.sortedArrayToBST(nums[mid_index+1:])

        return root


if __name__ == '__main__':
    pass
