#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    dp = None

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        self.dp = [[None for i in range(0, n+1)] for j in range(0, n+1)]
        return self.helperDp(1, n)

    def helper(self, start, end):
        res = []
        if start > end:
            res.append(None)
            return res
        if start == end:
            t = TreeNode(start)
            res.append(t)
            return res

        # 递归
        # 1-n看做树的中序遍历结果，分别取每个数字当做root节点，递归遍历左边的序列得到左子树列表，递归遍历右边的序列得到右子树列表
        # 时间复杂度1(n-1) + 2(n-2) ... + (n-1)*1 = O(n^2)
        for i in range(start, end+1):
            left = self.helper(start, i-1)
            right = self.helper(i+1, end)

            for n in left:
                for m in right:
                    t = TreeNode(i)
                    t.left = n
                    t.right = m
                    res.append(t)

        return res

    def helperDp(self, start, end):
        res = []
        if start > end:
            res.append(None)
            return res

        print(start, end)
        if self.dp[start][end]:
            return self.dp[start][end]

        if start == end:
            t = TreeNode(start)
            res.append(t)

        # 递归
        # 1-n看做树的中序遍历结果，分别取每个数字当做root节点，递归遍历左边的序列得到左子树列表，递归遍历右边的序列得到右子树列表
        # 时间复杂度1(n-1) + 2(n-2) ... + (n-1)*1 = O(n^2)
        for i in range(start, end+1):
            left = self.helperDp(start, i-1)
            right = self.helperDp(i+1, end)

            for n in left:
                for m in right:
                    t = TreeNode(i)
                    t.left = n
                    t.right = m
                    res.append(t)

        self.dp[start][end] = res

        return res


if __name__ == '__main__':
    s = Solution()
    s.generateTrees(3)
