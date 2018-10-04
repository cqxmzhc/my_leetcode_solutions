#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from common.common import buidMinHeap, MinHeapNode

import fileinput

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def huffmanEncoding():
        pass


def preOrder(root, code):
    if root == None:
        return

    if root.left == None and root.right == None:
        print(code+" ", end="")
        return

    preOrder(root.left, code+"0")
    preOrder(root.right, code+"1")


if __name__ == '__main__':
    count = 1
    chars = []
    for line in fileinput.input():
        o = count % 3
        if o == 2:
            line = line.strip()
            for i in line:
                chars.append(i)
        elif o == 0:
            line = line.strip()
            freq = line.split(" ")
            nodes = []
            for k, v in enumerate(chars):
                nodes.append(MinHeapNode(v, int(freq[k])))

            # 构建最小堆
            m = buidMinHeap(nodes)

            while m.length > 1:
                # 从堆中取出频率最小的两个节点
                min_1 = m.deleteMinNode(1)
                min_2 = m.deleteMinNode(1)

                # 使用这两个节点构造一个新节点
                new_node = MinHeapNode(None, min_1.freq+min_2.freq)
                # 插入堆中
                m.insert(new_node)

                new_node.left = min_1
                new_node.right = min_2

                if m.length == 1:
                    preOrder(new_node, code="")

        count += 1
