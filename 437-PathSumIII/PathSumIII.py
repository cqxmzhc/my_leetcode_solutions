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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        时间复杂度O(N)
        空间复杂度O(nlgn)
        """
        if not root:
            return 0

        stack = [(root, [])]

        count = 0
        while stack:
            row = []
            for current_node, path_sum in stack:
                path_sum = copy.copy(path_sum)
                if current_node.val == sum:
                    count += 1
                for k, v in enumerate(path_sum):
                    if current_node.val+v == sum:
                        count += 1

                    path_sum[k] += current_node.val

                path_sum.append(current_node.val)

                if current_node.left:
                    row.append((current_node.left, path_sum))
                if current_node.right:
                    row.append((current_node.right, path_sum))

            stack = row

        return count

    def pathSumRecur(self, root, sum):
        """
        如果路径a->..->b的和a.val+...+b.val==target,则路径root->...->a与路径root->...->b上的节点和满足如下关系
        (root.val+...+b.val) - (root.val+...+a.val) == target => 
        (root.val+...+b.val)[y] - target == (root.val+...+a.val)[y]
        x,y的值都可以通过递归的方式获取
        """
        path_sum_map = {0: 0}
        return self.helper(root, sum, 0, path_sum_map)

    def helper(self, root, sum, so_far, path_sum_map):
        import pdb
        pdb.set_trace()
        count = 0
        if not root:
            return count

        complement = so_far+root.val - sum
        if complement in path_sum_map:
            path_sum_map[complement] += 1
            count += 1
        else:
            path_sum_map[complement] = 0

        path_sum_map[so_far+root.val] = 0

        left_count = self.helper(root.left, sum, so_far+root.val, path_sum_map)
        path_sum_map[so_far+root.val] -= 1
        right_count = self.helper(
            root.right, sum, so_far+root.val, path_sum_map)

        # 和相同，路径不同。
        return count + left_count + right_count


if __name__ == '__main__':
    root = buildTestTree([1, -2, -3])
    print(root.val)

    s = Solution()

    print(s.pathSumRecur(root, -1))
