#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from common.common import *


def main():
    pass


def getPostOrderRecur(pre_order, in_order):
    # pre_order_len = len(pre_order)
    # if pre_order_len == 0:
    #     return

    # if pre_order_len == 1:
    #     print(pre_order[0])
    #     return

    in_order_len = len(in_order)

    if in_order_len == 0:
        return
    if len(in_order) == 2:
        pass

        # 先序的第一个节点就是某棵子树的根，在中序遍历的数组中找到这个根节点就可以把这棵树分割成左右两棵子树，递归求两棵子树的后序遍历

    root = pre_order[0]

    left_sub_tree = []
    right_sub_tree = []
    for k, v in enumerate(in_order):
        if v == root:
            left_sub_tree = in_order[0:k]
            right_sub_tree = in_order[k+1:]

    # 先序的数量和中序的数量是相同的
    # import pdb
    # pdb.set_trace()

    left_pre_order = pre_order[1:len(left_sub_tree)]
    getPostOrderRecur(left_pre_order, left_sub_tree)

    right_pre_order = pre_order[len(left_sub_tree)+1:]
    getPostOrderRecur(right_pre_order, right_sub_tree)


if __name__ == '__main__':
    getPostOrderRecur([1, 2, 3, 4, 5, 6], [3, 2, 4, 1, 6, 5])
