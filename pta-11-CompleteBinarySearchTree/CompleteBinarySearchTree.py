#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from common.common import *


def inorder(root, node_num, inorder_index):
    if root > node_num:
        return

    left_root = 2*root
    right_root = 2*root+1

    inorder(left_root)
    inorder_index.append(root)
    inorder(right_root)


def main():
    # 插入序列
    insert_seq = [1, 4, 9, 2, 99, 44, 29, 68, 10]
    node_num = len(insert_seq)

    # 根据二叉搜索树左小右大的性质，  对插入序列按从小到大排序得到的就是此树的中序遍历输出
    insert_seq.sort()

    # 完全二叉树节点之间具有这样的关系：根节点下边为i，左子树根节点为2i，右子树根节点为2i+1
    # 令目标完全二叉搜索树的根节点下标为1，对其进行中序遍历, 得到的节点下表序列与上面中序遍历的节点一一对应
    inorder_index = []
    inorder(1, node_num, inorder_index)

    # 构造一个节点下标与节点值对应的map
    node_map = dict(zip(inorder_index, insert_seq))

    # 从下表1开始
    for i in range(1, node_num+1):
        print(node_map[i])


if __name__ == '__main__':
    main()
