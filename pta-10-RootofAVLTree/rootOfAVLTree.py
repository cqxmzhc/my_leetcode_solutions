#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from common.common import *


def main():
    seq = [88, 70, 61, 96, 120]
    # seq = [88, 70, 61, 96, 120, 90, 65]
    rootOfAVLTree(seq)


def rootOfAVLTree(seq):
    len_seq = len(seq)
    if len_seq == 0:
        return None
    elif len(seq) < 3:
        return seq[1]
    else:
        tree = TreeNode(None, None, None)

        for i in seq:
            Insert(tree, i)

        PreOrderTree(tree)


if __name__ == '__main__':
    main()
