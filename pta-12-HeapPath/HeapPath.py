#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from common.common import *


def heapPath():
    min_heap = buidMinHeap([1, 2, 3, 4, 5])


if __name__ == '__main__':
    min_heap = buidMinHeap([46, 23, 26, 24, 10])
    min_heap.rootPath(5)

    # print(min_heap._value)
