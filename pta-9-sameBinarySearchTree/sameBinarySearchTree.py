#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from common.common import *


def main():
    t1 = [3, 1, 4, 2]
    t2 = [3, 5, 1, 2]
    print(sameTree(t1, t2))


def sameTree(seq1, seq2):
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)

    if len_seq1 != len_seq2:
        return False

    if len_seq1 == 0:
        return True

    root1 = seq1[0]
    root2 = seq2[0]

    if root1 != root2:
        return False

    sub_left_seq1 = []
    sub_right_seq1 = []

    sub_left_seq2 = []
    sub_right_seq2 = []

    for i in seq1[1:]:
        if i < root1:
            sub_left_seq1.append(i)
        else:
            sub_right_seq1.append(i)

    for i in seq2[1:]:
        if i < root2:
            sub_left_seq2.append(i)
        else:
            sub_right_seq2.append(i)

    return sameTree(sub_left_seq1, sub_left_seq2) and sameTree(sub_right_seq1, sub_right_seq2)


if __name__ == '__main__':
    main()
