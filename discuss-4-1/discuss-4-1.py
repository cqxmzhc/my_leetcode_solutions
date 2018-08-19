#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from common.common import *


def valid_sequence(seq):
    max = None
    min = None

    len_s = len(seq)
    if len_s <= 2:
        return True

    for i in range(0, len(seq)-1):
        if seq[i+1] > seq[i]:
            min = seq[i]
            if max:
                if seq[i+1] > max:
                    return False
                else:
                    min = seq[i+1]
        else:
            if seq[i+1] < seq[i]:
                max = seq[i]
                if min:
                    if seq[i+1] < min:
                        return False
                    max = seq[i+1]

    return True


def main():
    # print(valid_sequence([39, 101, 25, 63]))
    print(valid_sequence([2, 8, 3]))


if __name__ == '__main__':
    main()
