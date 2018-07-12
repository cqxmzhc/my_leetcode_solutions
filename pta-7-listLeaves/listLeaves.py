#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from common.common import *


def main():
    pass


if __name__ == '__main__':
    tree1, root1 = buildTree_listLeaves()

    # for i in tree1:
    #     print(i.value, i.left, i.right)
    # 层序遍历
    q = Queue()
    q.enqueue(root1)

    while q.length > 0:
        node = q.dequeue()
        # 叶子节点
        if node.left == -1 and node.right == -1:
            print(node.value)
            continue
        if node.left != -1:
            q.enqueue(tree1[node.left])
        if node.right != -1:
            q.enqueue(tree1[node.right])
